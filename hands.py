import os


def str_substring(string, sub_str):
    if (string.find(sub_str) == -1):
        return 0
    else:
        return 1

def list_substring(lists,sub_str):
	if any(sub_str in s for s in lists):
		return 1
	else:
		return 0	

def presence():
	
	test=0
	list_dir=os.listdir('/usr/bin/')
	lists={"vmware-","vbox","qemu"}
	for i in lists:
		flag=list_substring(list_dir,i)
		if(flag==1):
			print "[--]\033[1;31m"+i+" Detected\033[1;m"
			test=test+1
	if test==0:
		print '\t\t \033[1;32mNo!\033[1;m'
			
def flags():
	if 'hypervisor' in open("/proc/cpuinfo").read():
		print '\t\t [-]\033[1;31mDetected\033[1;m'
	else:
		print '\t\t \033[1;32mNo!\033[1;m'
		
def scsi():
	test=0
	list_dir=open("/proc/scsi/scsi").read().split(" ")
	lists={"VMware","VBOX"}
	
	for i in lists:
		flag=list_substring(list_dir,i)
		if(flag==1):
			print '\t\t [-]\033[1;31m'+i+'Detected\033[1;m'
			test=test+1
	
	if test==0:
		print '\t\t \033[1;32mNo!\033[1;m'

def mac():

	flag=0
	test=0
	flag=vbox_mac()
	if(flag==0):
		test=vmware_mac()
	if(test==0):
		print '\t\t \033[1;32mNo!\033[1;m'
		
	

		
def vmware_mac():
	
	mac=['00:05:69','00:0c:29','00:0C:29','00:1C:14','00:1c:14','00:50:56'] 
	
	try:
		addr= open("/sys/class/net/ens33/address").read()
		address=addr[0:8]
		
		for i in mac:
			#print i
			if (i==address):
				print "\t\t[-]\033[1;31mVMWare Detected\033[1;m"
			
	except IOError as e:
		#print "\t\t I/O error({0}): {1}".format(e.errno, e.strerror)
		if(e.errno==2):
			return 0

def vbox_mac():
	try:
		
		addr1= open("/sys/class/net/enp0s3/address").read() 
		address1=addr[0:8]
		#print address
		flag=str_substring(addr1, "08:00:27")
		if(flag==1):
			print "\t\t[-]\033[1;31mVirtualBox Detected\033[1;m"
		
			
	except IOError as e:
		#print "\t\t I/O error({0}): {1}".format(e.errno, e.strerror)
		if(e.errno==2):
			return 0

def bios_vendor():
	name=open("/sys/class/dmi/id/bios_vendor").read()
	test=0
	lists={"vmware","vbox","Phoenix","innotek"}
	for i in lists:
		flag=str_substring(name,i)
		if(flag==1):
			print "\t\t[-]\033[1;31mDetected\033[1;m"
			test=test+1
	if test==0:
		print '\t\t \033[1;32mNo!\033[1;m'
	
	
	

def product_vendor():
	name=open("/sys/class/dmi/id/product_name").read()	
	test=0
	lists={"VMware","VirtualBox","Phoenix","innotek"}
	for i in lists:
		flag=str_substring(name,i)
		if(flag==1):
			print "\t\t[-]\033[1;31mDetected\033[1;m"
			test=test+1
	if test==0:
		print '\t\t \033[1;32mNo!\033[1;m'
	
def sys_vendor():
	name=open("/sys/class/dmi/id/sys_vendor").read()
	test=0
	lists={"VMware","VirtualBox","Phoenix","innotek"}
	for i in lists:
		flag=str_substring(name,i)
		if(flag==1):
			print "\t\t[-]\033[1;31mDetected\033[1;m"
			test=test+1
	if test==0:
		print '\t\t \033[1;32mNo!\033[1;m'
	
def board_vendor():
	name=open("/sys/class/dmi/id/board_vendor").read()
	test=0
	lists={"VMware","VirtualBox","Phoenix","innotek","Oracle"}
	for i in lists:
		flag=str_substring(name,i)
		if(flag==1):
			print "\t\t[-]\033[1;31mDetected\033[1;m"
			test=test+1
	if test==0:
		print '\t\t \033[1;32mNo!\033[1;m'
