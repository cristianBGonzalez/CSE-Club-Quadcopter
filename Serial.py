import wiringpi2
	#wiringpi2.wiringPiSetupGpio()
serial = wiringpi2.serialOpen('/dev/ttyAMA0',38400) # Requires device/baud and returns an ID
if serial == -1:
	print('error')
wiringpi2.delay(1000)
while 1:
#while wiringpi2.serialDataAvail(): # this while condition might work better
	#wiringpi2.serialPuts(serial,"hello")
	print(wiringpi2.serialGetchar(serial))

wiringpi2.serialClose(serial)
