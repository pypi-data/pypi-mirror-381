from abc import ABC, abstractmethod
from typing import Callable
import torch

from pylopt.data import SolverResult

class IterativeLinearSystemSolver(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def solve(self, linear_operator: Callable, b: torch.Tensor, x0: torch.Tensor = None) -> SolverResult:
        pass