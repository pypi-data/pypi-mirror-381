from typing import Dict, Any, List, Optional, Union
from .base_plate_reader import CerilloBasePlateReader
from .cdcl.cdcl import CDCLCommand
from dataclasses import dataclass


@dataclass
class MotorStepCommand(CDCLCommand):
    """Motor step command"""
    steps: int = 0
    command: str = "M"  # Fixed prefix for motor commands
    command_id: Optional[str] = None

    def __post_init__(self):
        # Set the params to contain the steps value
        self.params = [str(self.steps)]
        # Call parent's __post_init__ to generate raw_message
        super().__post_init__()


@dataclass
class MotorNamedCommand(CDCLCommand):
    """Motor named command"""
    named_command: str = "s"
    command: str = "M"  # Fixed prefix for motor commands
    command_id: Optional[str] = None

    def __post_init__(self):
        # Set the params to contain the command string
        self.params = [str(self.named_command)]
        # Call parent's __post_init__ to generate raw_message
        super().__post_init__()


MotorCommand = Union[MotorStepCommand, MotorNamedCommand]


class RayoReader(CerilloBasePlateReader):
    """Rayo Plate Reader Implementation"""
    has_motor: bool = False

    # TODO should this use a has_motor param or should that be gleaned from the model number?
    def __init__(self, port: str = '/dev/ttyUSB0', has_motor: bool = False,  **kwargs):
        super().__init__(port, baudrate=250000, **kwargs)
        self.has_motor = has_motor

    def move_motor(self, motorCommand: MotorCommand) -> bool:
        if (not self.has_motor):
            return False
        self.send_command(motorCommand)
        if (self.simulate):
            self.log_serial(direction="receive", message="M ok")
