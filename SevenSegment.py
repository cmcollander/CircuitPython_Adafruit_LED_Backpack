import board
import busio

class SevenSegment:
	displaybuffer = None
	i2c = None

	def init(self):
		self.displaybuffer = [0x00] * 8
		self.i2c = busio.I2C(board.SCL,board.SDA)
		while not self.i2c.try_lock():
			pass
		self.i2c.writeto(0x70,bytes([0x21,0x81,0xEF]),stop=False)
		self.i2c.writeto(0x70,bytes([0x81]),stop=False)

	# Functions
	def writeDisplay(self):
		values = [0x00]
		for i in range(8):
			values.append(self.displaybuffer[i] & 0xFF)
			values.append(self.displaybuffer[i] >> 8)
		self.i2c.writeto(0x70,bytes(values),stop=False)

	def writeDigitRaw(self,loc,bitmask):
		self.displaybuffer[loc] = bitmask

	def writeColon(self,val):
		if val==True:
			self.writeDigitRaw(2,0xFF)
		else:
			self.writeDigitRaw(2,0x00)

	def clear(self):
		for i in range(8):
			displaybuffer[i] = 0x00
