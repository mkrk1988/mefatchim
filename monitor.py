import os
import time

os.system('mkdir /home/moshe/mefathim/pcaps')
wait = int(input("please enter the time of every cycle (Minutes)")) 
interfaces = os.listdir('/sys/class/net')
print(interfaces)

while True:
	localtime = time.localtime()
	result = time.strftime("%I:%M:%S", localtime)
	print(result)
	for i in interfaces:
		cmd = f'sudo tcpdump -i {i} -s 65535 -w /home/moshe/mefathim/pcaps/pcap_{i}_{result}.pcap'
		os.popen(cmd)
	time.sleep(wait)

