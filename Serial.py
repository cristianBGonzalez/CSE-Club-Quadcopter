import wiringpi2
wiringpi2.wiringPiSetupGpio()
serial = wiringpi2.serialOpen('/dev/ttyAMA0',9600) // Requires device/baud and returns an ID
wiringpi2.delay(1000)
while true:
	#wiringpi2.serialPuts(serial,"hello")
	wiringpi2.delay(1)
	print(wiringpi2.serialGetchar (serial))

wiringpi2.serialClose(serial) // Pass in ID