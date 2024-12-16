import board
import busio
from digitalio import DigitalInOut
from pmw3901 import PMW3901

rotation = 0
spi = board.SPI()
# spi = busio.SPI(board.GP2, board.GP3, board.GP4)
cs = DigitalInOut(board.A0)
flo = PMW3901(spi, cs)
flo.set_rotation(rotation)
tx = 0
ty = 0
while True:
	try:
		x, y = flo.get_motion()
	except RuntimeError:
		continue
	tx += x
	ty += y
	print("Motion: {:03d} {:03d} x: {:03d} y {:03d}".format(x, y, tx, ty))
	time.sleep(0.01)
