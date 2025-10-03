import pytest
from cerillo_python import StratusReader


class TestStratusSimulation:
    """Test suite for Stratus reader in simulation mode"""

    def test_initialization(self):
        """Test that Stratus reader initializes correctly in simulation mode"""
        reader = StratusReader(simulate=True)
        reader.connect()
        assert reader.simulate is True
        assert reader.plate_type == "96-well"
        reader.disconnect()


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])
