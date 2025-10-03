import copy

from cellsepi.backend.main_window.expert_mode.module import Module
from typing import List

IMMUTABLES = (int, float, str, bool, type(None))

def copy_data(value):
    """
    To take care that no references are transferred between the modules.
    """
    if isinstance(value, IMMUTABLES):
        return value

    return copy.deepcopy(value)

class Pipe:
    """
    Transfers the data from one module to another.
    """
    def __init__(self,source_module: Module,target_module: Module, ports: List[str]):
        """
        Raises:
            ValueError: If the source and target modules do not different.
        """
        if source_module.module_id == target_module.module_id:
            raise ValueError(f"Source and target modules must be different!")
        if ports is None or len(ports) == 0:
            raise ValueError(f"Ports must be non empty!")
        self.source_module = source_module
        self.target_module = target_module
        self.ports = ports

    def run(self):
        """
        Transfers the data from source modules outputs to target modules inputs.
        Raises:
            KeyError: If the source and target modules not have the ports in the outputs/inputs.
            TypeError: If the types of the port on the source and target modules do not match.
        """
        for port in self.ports:
            if port not in self.source_module.outputs:
                raise KeyError(f"'{port}' is not in the outputs of Module '{self.source_module.module_id}'")
            if port not in self.target_module.inputs:
                raise KeyError(f"'{port}' is not in the inputs of Module '{self.target_module.module_id}'")
            out_port = self.source_module.outputs[port]
            in_port = self.target_module.inputs[port]

            if out_port.data_type != in_port.data_type:
                raise TypeError(
                    f"Type mismatch on port '{port}', source_module provided {out_port.data_type.__name__}, output_module provided {in_port.data_type.__name__}!")

            in_port.data = copy_data(out_port.data)

    def __str__(self):
        return f"source: '{self.source_module.module_id}', target: '{self.target_module.module_id}', ports: {self.ports}"

    def to_dict(self):
        """
        Translates the pipe into a dictionary.
        """
        return {
            "source": self.source_module.module_id,
            "target": self.target_module.module_id,
            "ports": self.ports,
        }