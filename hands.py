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

def print_val(val):
	if(val==0):
		print '\t\t[-]\033[1;31mDetected!\033[1;m'
	else:
		print '\t\t \033[1;32mNo!\033[1;m'

def print_sval(name):
	print '\t\t[-]\033[1;31m'+name+' Detected!\033[1;m'
	

def presence():
	
	test=0
	list_dir=os.listdir('/usr/bin/')
	lists={"vmware-","vbox","qemu"}
	for i in lists:
		flag=list_substring(list_dir,i)
		if(flag==1):
			print_sval(i)
			test=test+1
	if test==0:
		print '\t\t \033[1;32mNo!\033[1;m'
			
def flags():
	if 'hypervisor' in open("/proc/cpuinfo").read():
		print_val(0)
	else:
		print_val(1)
		
def scsi():
	test=0
	list_dir=open("/proc/scsi/scsi").read().split(" ")
	lists={"VMware","VBOX"}
	
	for i in lists:
		flag=list_substring(list_dir,i)
		if(flag==1):
			print_sval(i)
			test=test+1
	
	if test==0:
		print_val(1)

def mac():

	flag=0
	test=0
	flag=vbox_mac()
	if(flag==0):
		test=vmware_mac()
	if(test==0 and flag==0):
		print_val(1)
		
	

		
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
		address1=addr1[0:8]
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
		print_val(1)
	
	
	

def product_vendor():
	name=open("/sys/class/dmi/id/product_name").read()	
	test=0
	lists={"VMware","VirtualBox","Phoenix","innotek"}
	for i in lists:
		flag=str_substring(name,i)
		if(flag==1):
			print_val(0)
			test=test+1
	if test==0:
		print_val(1)
	
def sys_vendor():
	name=open("/sys/class/dmi/id/sys_vendor").read()
	test=0
	lists={"VMware","VirtualBox","Phoenix","innotek"}
	for i in lists:
		flag=str_substring(name,i)
		if(flag==1):
			print_val(0)
			test=test+1
	if test==0:
		print_val(1)
	
def board_vendor():
	name=open("/sys/class/dmi/id/board_vendor").read()
	test=0
	lists={"VMware","VirtualBox","Phoenix","innotek","Oracle"}
	for i in lists:
		flag=str_substring(name,i)
		if(flag==1):
			print_val(0)
			test=test+1
	if test==0:
		print_val(1)
		
def kernel_modules():
	name=open("/proc/modules").read()
	test=0
	list1={"vmw_balloon","vmwfgx"}
	list2={"vboxvideo","vboxguest"}
	for i in list1:
		flag=str_substring(name,i)
		if(flag==1):
			print_sval("VMWare ")
			test=test+1
			break
	for i in list2:
		flag=str_substring(name,i)
		if(flag==1):
			print_sval("VirtualBox")
			test=test+1
			break
	if test==0:
		print_val(1)
