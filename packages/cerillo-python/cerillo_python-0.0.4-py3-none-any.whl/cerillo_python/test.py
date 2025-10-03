from cerillo_python import RayoReader, MotorNamedCommand, MotorStepCommand

rayo = RayoReader(port="/dev/ttyUSB0", has_motor=True, simulate=True)
open_lid_command = MotorNamedCommand(named_command="o")
step_command = MotorStepCommand(steps=-100)

print(open_lid_command)
print(step_command)
rayo.move_motor(open_lid_command)
