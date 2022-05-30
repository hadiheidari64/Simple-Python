##Use_case: if you need to find the live machines using Ping mechanism. add the
import subprocess

###add the last oct(1-255) here
for ping in range(1,10):
##Add the first to 3rd oct here. ex:10.10.10.
	address = "4.2.2." + str(ping)
	res = subprocess.call(['ping', address])
	if res == 0:
		print( "ping to", address, "OK")
	elif res == 2:
		print("no response from", address)
	else:
		print("ping to", address, "failed!")
