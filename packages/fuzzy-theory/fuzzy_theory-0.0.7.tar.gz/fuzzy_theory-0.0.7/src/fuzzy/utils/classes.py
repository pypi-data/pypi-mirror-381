"""
This module contains classes that are reserved more for the internal use of the fuzzy package.
"""

import inspect
import pickle
from abc import abstractmethod
from pathlib import Path
from typing import Any, Callable, Dict, List, MutableMapping, Set, Tuple

import torch
from natsort import natsorted
from torch.nn.modules.module import _forward_unimplemented

from fuzzy.utils.functions import all_subclasses, get_object_attributes


class TimeDistributed(torch.nn.Module):
    """
    A wrapper class for PyTorch modules that allows them to operate on a sequence of data.
    """

    # https://discuss.pytorch.org/t/any-pytorch-function-can-work-as-keras-timedistributed/1346/4
    def __init__(self, module: torch.nn.Module, batch_first: bool = False):
        """
        Initialize the TimeDistributed wrapper class.

        Args:
            module: A PyTorch module.
            batch_first: Whether the batch dimension is the first dimension.
        """
        super().__init__()
        self.module = module
        self.batch_first = batch_first

    def forward(self, input_data: torch.Tensor) -> torch.Tensor:
        """
        Forward pass of the TimeDistributed wrapper class.

        Args:
            input_data: The input data.

        Returns:
            The output of the module on the input sequence of data.
        """
        if len(input_data.size()) <= 2:
            return self.module(input_data)

        # squash samples and timesteps into a single axis
        reshaped_input_data = input_data.contiguous().view(
            -1, input_data.size(-1)
        )  # (samples * timesteps, input_size)

        module_output = self.module(reshaped_input_data)

        # reshape the output back to the original shape
        output_dim = 1
        if module_output.ndim == 2:
            output_dim = module_output.size(-1)
        if self.batch_first:
            module_output = module_output.contiguous().view(
                input_data.size(0), input_data.size(1), output_dim
            )  # (samples, timesteps, output_size)
        else:
            module_output = module_output.view(
                input_data.size(1), input_data.size(0), output_dim
            )  # (timesteps, samples, output_size)

        return module_output


class NestedTorchJitModule(torch.nn.Module):
    """
    A NestedTorchJitModule is a torch.nn.Module that contains other torch.nn.Module objects as
    attributes. This class is used to save and load the torch.nn.Module object to and from a
    directory, respectively.
    """

    forward: Callable[..., Any] = (
        _forward_unimplemented  # unsure of forward signature yet
    )

    def save(self, path: Path) -> None:
        """
        Save the torch.nn.Module object to a directory.

        Note: This does not preserve ParameterList structures, but rather concatenates the
        parameters into a single tensor, which is then saved to a file.

        Returns:
            None
        """
        if "." in path.name:
            raise ValueError(
                f"The path to save the {self.__class__} must not have a file extension, "
                f"but got {path.name}"
            )
        # get the attributes that are local to the class, but not inherited
        # from the super class
        local_attributes_only = get_object_attributes(self)

        # save a reference to the attributes (and their values) so that when iterating over them,
        # we do not modify the dictionary while iterating over it (which would cause an error)
        # we modify the dictionary by removing attributes that have a value of torch.nn.ModuleList
        # because we want to save the modules in the torch.nn.ModuleList
        # separately
        local_attributes_only_items: List[Tuple[str, Any]] = list(
            local_attributes_only.items()
        )
        for attr, value in local_attributes_only_items:
            if isinstance(
                value, torch.nn.ModuleList
            ):  # e.g., attr may be self.modules_list
                for idx, module in enumerate(value):
                    subdirectory = path / attr / str(idx)
                    subdirectory.mkdir(parents=True, exist_ok=True)
                    if isinstance(module, TorchJitModule):
                        # save the fuzzy set using the fuzzy set's special
                        # protocol
                        module.save(
                            path / attr / str(idx) / f"{module.__class__.__name__}.pt"
                        )
                    else:
                        # unknown and unrecognized module, but attempt to save
                        # the module
                        torch.save(
                            module,
                            path / attr / str(idx) / f"{module.__class__.__name__}.pt",
                        )
                # remove the torch.nn.ModuleList from the local attributes
                del local_attributes_only[attr]

        # save the remaining attributes
        with open(path / f"{self.__class__.__name__}.pickle", "wb") as handle:
            pickle.dump(local_attributes_only, handle, protocol=pickle.HIGHEST_PROTOCOL)

    @classmethod
    def load(cls, path: Path, device: torch.device) -> "NestedTorchJitModule":
        """
        Load the torch.nn.Module from the given path.

        Args:
            path: The path to load the NestedTorchJitModule from.
            device: The device to load the NestedTorchJitModule to.

        Returns:
            The loaded NestedTorchJitModule.
        """
        modules_list = []
        local_attributes_only: Dict[str, Any] = {}
        for file_path in path.iterdir():
            if ".pickle" in file_path.name:
                # load the remaining attributes
                with open(file_path, "rb") as handle:
                    local_attributes_only.update(pickle.load(handle))
            elif file_path.is_dir():
                for subdirectory in natsorted(file_path.iterdir()):
                    if subdirectory.is_dir():
                        module_path: Path = list(subdirectory.glob("*.pt"))[0]
                        # load the fuzzy set using the fuzzy set's special
                        # protocol
                        class_name: str = module_path.name.split(".pt")[0]
                        try:
                            modules_list.append(
                                TorchJitModule.get_subclass(class_name).load(
                                    module_path, device=device
                                )
                            )
                        except ValueError:
                            # unknown and unrecognized module, but attempt to
                            # load the module
                            modules_list.append(
                                torch.load(module_path, weights_only=False)
                            )
                    else:
                        raise UserWarning(
                            f"Unexpected file found in {file_path}: {subdirectory}"
                        )
                local_attributes_only[file_path.name] = modules_list

        # of the remaining attributes, we must determine which are shared between the
        # super class and the local class, otherwise we will get an error when trying to
        # initialize the local class (more specifically, the torch.nn.Module __init__ method
        # requires self.call_super_init to be set to True, but then the attribute would exist
        # as a super class attribute, and not a local class attribute)
        shared_args: Set[str] = set(
            inspect.signature(cls).parameters.keys()
        ).intersection(local_attributes_only.keys())

        # create the GroupedFuzzySet object with the shared arguments
        # (e.g., modules_list, expandable)
        grouped_fuzzy_set: NestedTorchJitModule = cls(
            **{
                key: value
                for key, value in local_attributes_only.items()
                if key in shared_args
            }
        )

        # determine the remaining attributes
        remaining_args: Dict[str, Any] = {
            key: value
            for key, value in local_attributes_only.items()
            if key not in shared_args
        }

        # set the remaining attributes
        for attr, value in remaining_args.items():
            try:
                setattr(grouped_fuzzy_set, attr, value)
            except AttributeError:
                # the attribute is not a valid attribute of the class (e.g.,
                # property)
                continue
        return grouped_fuzzy_set


class TorchJitModule(torch.nn.Module):
    """
    A TorchJitModule is a torch.nn.Module that can be saved and loaded to and from a file. It is
    also expected that the class that inherits from TorchJitModule will have subclasses of its own.
    """

    @abstractmethod
    @torch.jit.ignore
    def save(self, path: Path) -> MutableMapping[str, Any]:
        """
        Save the torch.nn.Module object to a file.

        Note: This does not preserve ParameterList structures, but rather concatenates the
        parameters into a single tensor, which is then saved to a file.

        Returns:
            A dictionary containing the state of the torch.nn.Module object.
        """

    @classmethod
    @abstractmethod
    @torch.jit.ignore
    def load(cls, path: Path, device: torch.device) -> "TorchJitModule":
        """
        Load the class object from a file and put it on the specified device.

        Returns:
            None
        """

    @classmethod
    @torch.jit.ignore
    def get_subclass(cls, class_name: str) -> "TorchJitModule":
        """
        Get the subclass of TorchJitModule with the given class name.

        Args:
            class_name: The name of the subclass to find.

        Returns:
            A subclass implementation of TorchJitModule with the given class name.
        """
        fuzzy_set_class = None
        for subclass in all_subclasses(cls):
            if subclass.__name__ == class_name:
                fuzzy_set_class = subclass
                break
        if fuzzy_set_class is None:
            raise ValueError(
                f"The class {class_name} was not found in the subclasses of "
                f"{cls}. Please ensure that {class_name} is a subclass of {cls}."
            )
        return fuzzy_set_class
