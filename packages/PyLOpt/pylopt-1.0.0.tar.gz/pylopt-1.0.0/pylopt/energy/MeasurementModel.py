import torch
from typing import Optional
from confuse import Configuration

class MeasurementModel(torch.nn.Module):
    """
    A class, inherited from torch.nn.Module modeling the noisy measurement/observation of data.
    Observations are assumed to be a sum of a forward operator applied to the clean data and noise sampled from
    the multivariate normal distribution with zero mean and covariance matrix (noise_level ** 2) * I.
    """
    def __init__(self, 
                 u_clean: torch.Tensor, 
                 operator: Optional[torch.nn.Module]=None, 
                 noise_level: Optional[float]=None, 
                 config: Optional[Configuration]=None) -> None:
        """
        Initialisation of an object of class MeasurementModel. 

        NOTE
        ----
            > Either both, operator and noise_level, or config must be specified.

        :param u_clean: Tensor of shape [batch_size, channels, height, width]
        :param operator: PyTorch module representing the forward operator
        :param noise_level: Float in the interval (0, 1) representing the noise level
        :param config: Configuration object for the configuration of operator and noise level.
        """
        super().__init__()
        self.u_clean = torch.nn.Parameter(u_clean, requires_grad=False)

        if config is not None:
            # TODO:
            #   > extend search for operators to submodule (operators f.e.) such that custom forward operators can be used

            operator_name = config['measurement_model']['forward_operator'].get()
            self.operator = getattr(torch.nn, operator_name)()
            self.noise_level = config['measurement_model']['noise_level'].get()
        elif noise_level is not None and operator is not None:
            self.operator = operator
            self.noise_level = noise_level
        else:
            raise ValueError('Must provide config or both, operator and noise_level.')

        self.u_noisy = torch.nn.Parameter(self.make_noisy_observation(), requires_grad = False)

    def get_clean_data(self) -> torch.nn.Parameter:
        """
        Returns the clean data tensor to the caller

        :return: torch.Tensor
        """
        return self.u_clean

    def make_noisy_observation(self) -> torch.Tensor:
        obs_clean = self.operator(self.u_clean)
        return obs_clean + self.noise_level * torch.randn_like(obs_clean)

    def get_noisy_observation(self) -> torch.nn.Parameter:
        return self.u_noisy

    def forward(self, u: torch.Tensor,) -> torch.Tensor:
        """
        Computes the data fidelty of the input tensor u, i.e. the scaled 
        squared l2-norm of the difference between the input tensor 
        and a noisy observation. 

        :param u: Tensor of the same shape as clean or noisy data tensor.
        :return: Data fidelty of u
        """
        return 0.5 * torch.sum((u - self.u_noisy) ** 2) / self.noise_level ** 2


