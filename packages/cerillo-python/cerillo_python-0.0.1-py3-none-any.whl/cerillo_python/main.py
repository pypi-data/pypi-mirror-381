from cerillo_python import StratusReader


reader = StratusReader(port="/dev/ttyUSB0")
reader.connect()
reader.read_absorbance(450)
