import pytest
from cerillo_python import RayoReader, MotorStepCommand


class TestRayoSimulation:
    """Test suite for Stratus reader in simulation mode"""

    def test_initialization(self):
        """Test that Stratus reader initializes correctly in simulation mode"""
        reader = RayoReader(simulate=True, has_motor=True)
        reader.connect()
        assert reader.simulate is True
        step_command = MotorStepCommand(steps=100)
        reader.move_motor(step_command)
        reader.disconnect()


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])
