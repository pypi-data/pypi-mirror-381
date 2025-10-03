"""
Implements various conventional membership functions (CMFs) by inheriting from FuzzySet.
"""

from typing import Union

import numpy as np
import sympy
import torch

from ..abstract import FuzzySet
from ..membership import Membership


class NoOp(FuzzySet):
    """
    Implementation of the NoOp membership function, written in PyTorch.
    """

    def __init__(self, n_elements, membership: float, device: torch.device):
        centers = np.zeros(n_elements, dtype=np.float32)[:, np.newaxis]
        widths = np.zeros(n_elements, dtype=np.float32)[:, np.newaxis]
        self.membership = membership  # the flat membership degree of the NoOp fuzzy set
        super().__init__(centers=centers, widths=widths, device=device)

    @staticmethod
    def internal_calculate_membership(
        observations: torch.Tensor,
        centers: torch.Tensor,
        widths: torch.Tensor,
        membership_degree: float,
    ) -> torch.Tensor:
        """
        Calculate the membership of the observations to the NoOp fuzzy set.
        This is a static method, so it can be called without instantiating the class.
        This static method is particularly useful when animating the membership function.

        Warning: This method is not meant to be called directly, as it does not take into account
        the mask that likely should exist. Use the calculate_membership method instead.

        Args:
            observations: The observations to calculate the membership for.
            centers: The centers of the NoOp fuzzy set.
            widths: The widths of the NoOp fuzzy set.
            membership_degree: The membership degree of the NoOp fuzzy set.

        Returns:
            The membership degrees of the observations for the NoOp fuzzy set.
        """
        return (
            (torch.ones_like(centers) * membership_degree)
            .unsqueeze(0)
            .repeat(observations.shape[0], 1, 1)
        )  # repeat for each observation

    @classmethod
    @torch.jit.ignore
    def sympy_formula(cls) -> sympy.Expr:
        # centers (c), widths (sigma) and observations (x)
        pass

    def calculate_membership(self, observations: torch.Tensor) -> torch.Tensor:
        """
        Calculate the membership of the observations to the NoOp fuzzy set.

        Args:
            observations: The observations to calculate the membership for.

        Returns:
            The membership degrees of the observations for the NoOp fuzzy set.
        """
        return NoOp.internal_calculate_membership(
            observations=observations,
            centers=self.get_centers(),
            widths=self.get_widths(),
            membership_degree=self.membership,
        )

    def forward(self, observations) -> Membership:
        if observations.ndim == self.get_centers().ndim:
            observations = observations.unsqueeze(dim=-1)
        # we do not need torch.float64 for observations
        degrees: torch.Tensor = self.calculate_membership(observations.float())

        # assert (
        #     not degrees.isnan().any()
        # ), "NaN values detected in the membership degrees."
        # assert (
        #     not degrees.isinf().any()
        # ), "Infinite values detected in the membership degrees."

        return Membership(
            # elements=observations.squeeze(dim=-1),  # remove the last
            # dimension
            degrees=degrees.to_sparse() if self.use_sparse_tensor else degrees,
            mask=self.get_mask(),
        )


class GeneralizedGuassian(FuzzySet):
    """
    Implementation of the Generalized Gaussian membership function, written in PyTorch.
    """

    def __init__(
        self,
        centers,
        widths,
        device: torch.device,
        width_multiplier: float = 2.0,
        slope_multiplier: float = 1.0,
    ):
        super().__init__(centers=centers, widths=widths, device=device)
        if width_multiplier < 0.0:
            raise ValueError(
                f"The width multiplier must be greater than zero, but got {self.width_multiplier}."
            )
        self._width_multiplier = torch.nn.ParameterList(
            [self.make_parameter(width_multiplier * np.ones_like(centers))]
        )
        self._slope_multiplier = torch.nn.ParameterList(
            [self.make_parameter(slope_multiplier * np.ones_like(centers))]
        )

    def get_width_multiplier(self) -> torch.Tensor:
        """
        Get the concatenated width multipliers of the fuzzy set from its
        corresponding ParameterList.

        Returns:
            The concatenated width multipliers of the fuzzy set.
        """
        return torch.cat(list(self._width_multiplier), dim=-1)

    def get_slope_multiplier(self) -> torch.Tensor:
        """
        Get the concatenated slope multipliers of the fuzzy set from its
        corresponding ParameterList.

        Returns:
            The concatenated slope multipliers of the fuzzy set.
        """
        return torch.cat(list(self._slope_multiplier), dim=-1)

    @staticmethod
    def internal_calculate_membership(
        observations: torch.Tensor,
        centers: torch.Tensor,
        widths: torch.Tensor,
        width_multiplier: torch.Tensor,
        slope_multiplier: torch.Tensor,
    ) -> torch.Tensor:
        """
        Calculate the membership of the observations to the Log Gaussian fuzzy set.
        This is a static method, so it can be called without instantiating the class.
        This static method is particularly useful when animating the membership function.

        Warning: This method is not meant to be called directly, as it does not take into account
        the mask that likely should exist. Use the calculate_membership method instead.

        Args:
            observations: The observations to calculate the membership for.
            centers: The centers of the Log Gaussian fuzzy set.
            widths: The widths of the Log Gaussian fuzzy set.
            width_multiplier: The width multiplier of the Log Gaussian fuzzy set.

        Returns:
            The membership degrees of the observations for the Log Gaussian fuzzy set.
        """
        vals = -1.0 * torch.pow(
            (torch.pow(observations - centers, 2) / torch.pow(width_multiplier, 2)),
            slope_multiplier,
        )
        # this works pretty well -- but does cause NaNs later on
        # vals = (
        #     -1.0 * torch.pow(observations - centers, 2) / torch.pow(width_multiplier, 2)
        # )
        return vals

    @classmethod
    @torch.jit.ignore
    def sympy_formula(cls) -> sympy.Expr:
        # centers (c), widths (sigma) and observations (x)
        pass

    def calculate_membership(self, observations: torch.Tensor) -> torch.Tensor:
        """
        Calculate the membership of the observations to the Log Gaussian fuzzy set.

        Args:
            observations: The observations to calculate the membership for.

        Returns:
            The membership degrees of the observations for the Log Gaussian fuzzy set.
        """
        return GeneralizedGuassian.internal_calculate_membership(
            observations=observations,
            centers=self.get_centers(),
            widths=self.get_widths(),
            width_multiplier=self.get_width_multiplier(),
            slope_multiplier=self.get_slope_multiplier(),
        )

    def forward(self, observations) -> Membership:
        if observations.ndim == self.get_centers().ndim:
            observations = observations.unsqueeze(dim=-1)
        # we do not need torch.float64 for observations
        degrees: torch.Tensor = self.calculate_membership(observations.float())

        # assert (
        #     not degrees.isnan().any()
        # ), "NaN values detected in the membership degrees."
        # assert (
        #     not degrees.isinf().any()
        # ), "Infinite values detected in the membership degrees."

        return Membership(
            # elements=observations.squeeze(dim=-1),  # remove the last
            # dimension
            degrees=degrees.to_sparse() if self.use_sparse_tensor else degrees,
            mask=self.get_mask(),
        )


class LogGaussian(FuzzySet):
    """
    Implementation of the Log Gaussian membership function, written in PyTorch.
    This is a modified version that helps when the dimensionality is high,
    and TSK product inference engine will be used.
    """

    def __init__(
        self,
        centers,
        widths,
        device: torch.device,
        width_multiplier: float = 2.0,
        # in fuzzy logic, convention is usually 1.0, but can be 2.0
    ):
        super().__init__(centers=centers, widths=widths, device=device)
        self.width_multiplier = width_multiplier
        if int(self.width_multiplier) not in [1, 2]:
            raise ValueError(
                "The width multiplier must be either 1.0 or 2.0, but got {self.width_multiplier}."
            )

    # @property
    # @torch.jit.ignore
    # def sigmas(self) -> torch.Tensor:
    #     """
    #     Gets the sigma for the Gaussian fuzzy set; alias for the 'widths' parameter.
    #
    #     Returns:
    #         torch.Tensor
    #     """
    #     return self.widths
    #
    # @sigmas.setter
    # @torch.jit.ignore
    # def sigmas(self, sigmas) -> None:
    #     """
    #     Sets the sigma for the Gaussian fuzzy set; alias for the 'widths' parameter.
    #
    #     Returns:
    #         None
    #     """
    #     self.widths = sigmas

    @staticmethod
    def internal_calculate_membership(
        observations: torch.Tensor,
        centers: torch.Tensor,
        widths: torch.Tensor,
        width_multiplier: float,
    ) -> torch.Tensor:
        """
        Calculate the membership of the observations to the Log Gaussian fuzzy set.
        This is a static method, so it can be called without instantiating the class.
        This static method is particularly useful when animating the membership function.

        Warning: This method is not meant to be called directly, as it does not take into account
        the mask that likely should exist. Use the calculate_membership method instead.

        Args:
            observations: The observations to calculate the membership for.
            centers: The centers of the Log Gaussian fuzzy set.
            widths: The widths of the Log Gaussian fuzzy set.
            width_multiplier: The width multiplier of the Log Gaussian fuzzy set.

        Returns:
            The membership degrees of the observations for the Log Gaussian fuzzy set.
        """
        return (
            -1.0
            * (
                torch.pow(
                    observations - centers,
                    2,
                )
                / (width_multiplier * torch.pow(widths, 2) + 1e-32)
            )
        ).clamp(
            min=-10, max=0  # was -50 for visualization
        )  # force values very close to zero to be zero

    @classmethod
    @torch.jit.ignore
    def sympy_formula(cls) -> sympy.Expr:
        # centers (c), widths (sigma) and observations (x)
        center_symbol = sympy.Symbol("c")
        width_symbol = sympy.Symbol("sigma")
        input_symbol = sympy.Symbol("x")
        return sympy.sympify(
            f"-1.0 * pow(({input_symbol} - {center_symbol}), 2) / (2.0 * pow({width_symbol}, 2))"
        )

    def calculate_membership(self, observations: torch.Tensor) -> torch.Tensor:
        """
        Calculate the membership of the observations to the Log Gaussian fuzzy set.

        Args:
            observations: The observations to calculate the membership for.

        Returns:
            The membership degrees of the observations for the Log Gaussian fuzzy set.
        """
        return LogGaussian.internal_calculate_membership(
            observations=observations,
            centers=self.get_centers(),
            widths=self.get_widths(),
            width_multiplier=self.width_multiplier,
        )

    def forward(self, observations) -> Membership:
        if observations.ndim == self.get_centers().ndim:
            observations = observations.unsqueeze(dim=-1)
        # we do not need torch.float64 for observations
        degrees: torch.Tensor = self.calculate_membership(observations.float())

        # assert (
        #     not degrees.isnan().any()
        # ), "NaN values detected in the membership degrees."
        # assert (
        #     not degrees.isinf().any()
        # ), "Infinite values detected in the membership degrees."

        return Membership(
            # elements=observations.squeeze(dim=-1),  # remove the last
            # dimension
            degrees=degrees.to_sparse() if self.use_sparse_tensor else degrees,
            mask=self.get_mask(),
        )


class Gaussian(LogGaussian):
    """
    Implementation of the Gaussian membership function, written in PyTorch.
    """

    @staticmethod
    def internal_calculate_membership(
        observations: torch.Tensor,
        centers: torch.Tensor,
        widths: torch.Tensor,
        width_multiplier: float = 1.0,
        # in fuzzy logic, convention is usually 1.0, but can be 2.0
    ) -> torch.Tensor:
        """
        Calculate the membership of the observations to the Gaussian fuzzy set.
        This is a static method, so it can be called without instantiating the class.
        This static method is particularly useful when animating the membership function.

        Warning: This method is not meant to be called directly, as it does not take into account
        the mask that likely should exist. Use the calculate_membership method instead.

        Args:
            observations: The observations to calculate the membership for.
            centers: The centers of the Gaussian fuzzy set.
            widths: The widths of the Gaussian fuzzy set.
            width_multiplier: The width multiplier of the Gaussian fuzzy set.

        Returns:
            The membership degrees of the observations for the Gaussian fuzzy set.
        """
        return torch.exp(
            -1.0
            * (
                torch.pow(
                    observations - centers,
                    2,
                )
                / (width_multiplier * torch.pow(widths, 2) + 1e-32)
            )
        )
        # return LogGaussian.internal_calculate_membership(
        #     centers=centers,
        #     widths=widths,
        #     width_multiplier=width_multiplier,
        #     observations=observations,
        # ).exp()

    @classmethod
    @torch.jit.ignore
    def sympy_formula(cls) -> sympy.Expr:
        return sympy.exp(LogGaussian.sympy_formula())

    def calculate_membership(self, observations: torch.Tensor) -> torch.Tensor:
        return Gaussian.internal_calculate_membership(
            observations=observations,
            centers=self.get_centers(),
            widths=self.get_widths(),
            width_multiplier=1.0,
        )

    def forward(self, observations) -> Membership:
        if observations.ndim == self.get_centers().ndim:
            observations = observations.unsqueeze(dim=-1)
        # we do not need torch.float64 for observations
        degrees: torch.Tensor = self.calculate_membership(observations.float())

        # assert (
        #     not degrees.isnan().any()
        # ), "NaN values detected in the membership degrees."
        # assert (
        #     not degrees.isinf().any()
        # ), "Infinite values detected in the membership degrees."

        return Membership(
            # elements=observations.squeeze(dim=-1),  # remove the last
            # dimension
            degrees=degrees.to_sparse() if self.use_sparse_tensor else degrees,
            mask=self.get_mask(),
        )


class Lorentzian(FuzzySet):
    """
    Implementation of the Lorentzian membership function, written in PyTorch.
    """

    @property
    @torch.jit.ignore
    def sigmas(self) -> torch.Tensor:
        """
        Gets the sigma for the Lorentzian fuzzy set; alias for the 'widths' parameter.

        Returns:
            torch.Tensor
        """
        return self.widths

    @sigmas.setter
    @torch.jit.ignore
    def sigmas(self, sigmas) -> None:
        """
        Sets the sigma for the Lorentzian fuzzy set; alias for the 'widths' parameter.

        Returns:
            None
        """
        self.widths = sigmas

    @staticmethod
    def internal_calculate_membership(
        observations: torch.Tensor, centers: torch.Tensor, widths: torch.Tensor
    ) -> torch.Tensor:
        """
        Calculate the membership of the observations to the Lorentzian fuzzy set.
        This is a static method, so it can be called without instantiating the class.
        This static method is particularly useful when animating the membership function.

        Warning: This method is not meant to be called directly, as it does not take into account
        the mask that likely should exist. Use the calculate_membership method instead.

        Args:
            observations: The observations to calculate the membership for.
            centers: The centers of the Lorentzian fuzzy set.
            widths: The widths of the Lorentzian fuzzy set.

        Returns:
            The membership degrees of the observations for the Lorentzian fuzzy set.
        """
        return 1 / (1 + torch.pow((centers - observations) / (0.5 * widths), 2))

    @classmethod
    @torch.jit.ignore
    def sympy_formula(cls) -> sympy.Expr:
        # centers (c), widths (sigma) and observations (x)
        center_symbol = sympy.Symbol("c")
        width_symbol = sympy.Symbol("sigma")
        input_symbol = sympy.Symbol("x")
        return sympy.sympify(
            f"1 / (1 + pow(({center_symbol} - {input_symbol}) / (0.5 * {width_symbol}), 2))"
        )

    def calculate_membership(self, observations: torch.Tensor) -> torch.Tensor:
        """
        Calculate the membership of the observations to the Lorentzian fuzzy set.

        Args:
            observations: The observations to calculate the membership for.

        Returns:
            The membership degrees of the observations for the Lorentzian fuzzy set.
        """
        return Lorentzian.internal_calculate_membership(
            observations=observations,
            centers=self.get_centers(),
            widths=self.get_widths(),
        )

    def forward(self, observations) -> Membership:
        if observations.ndim == self.get_centers().ndim:
            observations = observations.unsqueeze(dim=-1)
        # we do not need torch.float64 for observations
        degrees: torch.Tensor = self.calculate_membership(observations.float())

        assert (
            not degrees.isnan().any()
        ), "NaN values detected in the membership degrees."
        assert (
            not degrees.isinf().any()
        ), "Infinite values detected in the membership degrees."

        return Membership(
            # elements=observations.squeeze(dim=-1),  # remove the last
            # dimension
            degrees=degrees.to_sparse() if self.use_sparse_tensor else degrees,
            mask=self.get_mask(),
        )


class LogisticCurve(torch.nn.Module):
    """
    A generic torch.nn.Module class that implements a logistic curve, which allows us to
    tune the midpoint, and growth of the curve, with a fixed supremum (the supremum is
    the maximum value of the curve).
    """

    def __init__(
        self,
        midpoint: float,
        growth: float,
        supremum: float,
        device: Union[str, torch.device] = "cpu",
    ):
        super().__init__()
        if isinstance(device, str):
            device = torch.device(device)
        self.device: torch.device = device
        self.midpoint = torch.nn.Parameter(
            torch.as_tensor(midpoint, dtype=torch.float16, device=self.device),
            requires_grad=True,  # explicitly set to True for clarity
        )
        self.growth = torch.nn.Parameter(
            torch.as_tensor(growth, dtype=torch.float16, device=self.device),
            requires_grad=True,  # explicitly set to True for clarity
        )
        self.supremum = torch.nn.Parameter(
            torch.as_tensor(supremum, dtype=torch.float16, device=self.device),
            requires_grad=False,  # not a parameter, so we don't want to track it
        )

    def forward(self, tensors: torch.Tensor) -> torch.Tensor:
        """
        Calculate the value of the logistic curve at the given point.

        Args:
            tensors:

        Returns:

        """
        return self.supremum / (
            1 + torch.exp(-1.0 * self.growth * (tensors - self.midpoint))
        )


class Triangular(FuzzySet):
    """
    Implementation of the Triangular membership function, written in PyTorch.
    """

    def __init__(
        self,
        centers=None,
        widths=None,
        device: Union[str, torch.device] = torch.device("cpu"),
    ):
        super().__init__(centers=centers, widths=widths, device=device)

    @staticmethod
    def internal_calculate_membership(
        centers: torch.Tensor, widths: torch.Tensor, observations: torch.Tensor
    ) -> torch.Tensor:
        """
        Calculate the membership of the observations to the Triangular fuzzy set.
        This is a static method, so it can be called without instantiating the class.
        This static method is particularly useful when animating the membership function.

        Warning: This method is not meant to be called directly, as it does not take into account
        the mask that likely should exist. Use the calculate_membership method instead.

        Args:
            centers: The centers of the Triangular fuzzy set.
            widths: The widths of the Triangular fuzzy set.
            observations: The observations to calculate the membership for.

        Returns:
            The membership degrees of the observations for the Triangular fuzzy set.
        """
        return torch.max(
            1.0 - (1.0 / widths) * torch.abs(observations - centers),
            torch.tensor(0.0),
        )

    @classmethod
    @torch.jit.ignore
    def sympy_formula(cls) -> sympy.Expr:
        # centers (c), widths (w) and observations (x)
        center_symbol = sympy.Symbol("c")
        width_symbol = sympy.Symbol("w")
        input_symbol = sympy.Symbol("x")
        return sympy.sympify(
            f"max(1.0 - (1.0 / {width_symbol}) * abs({input_symbol} - {center_symbol}), 0.0)"
        )

    def calculate_membership(self, observations: torch.Tensor) -> torch.Tensor:
        """
        Forward pass of the function. Applies the function to the input elementwise.

        Args:
            observations: Two-dimensional matrix of observations,
            where a row is a single observation and each column
            is related to an attribute measured during that observation.

        Returns:
            The membership degrees of the observations for the Triangular fuzzy set.
        """
        return Triangular.internal_calculate_membership(
            observations=observations,
            centers=self.get_centers(),
            widths=self.get_widths(),
        )

    def forward(self, observations) -> Membership:
        if observations.ndim == self.get_centers().ndim:
            observations = observations.unsqueeze(dim=-1)
        # we do not need torch.float64 for observations
        degrees: torch.Tensor = self.calculate_membership(observations.float())

        assert (
            not degrees.isnan().any()
        ), "NaN values detected in the membership degrees."
        assert (
            not degrees.isinf().any()
        ), "Infinite values detected in the membership degrees."

        return Membership(
            # elements=observations.squeeze(dim=-1),  # remove the last
            # dimension
            degrees=degrees.to_sparse() if self.use_sparse_tensor else degrees,
            mask=self.get_mask(),
        )
