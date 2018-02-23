from SevenSegment import SevenSegment

seg = SevenSegment()
seg.init()

while True:
	for i in range(0xFF):
		for j in [0,1,2,3,4]:
			seg.writeDigitRaw(j,i)
		seg.writeDisplay()
