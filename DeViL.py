# !/usr/bin/env python

__author__ = 'Sreelakshmi ( srlkhmi@gmail.com )'


import os
import sys
import subprocess
import sys

vendor_names={'VMware','Vbox','Phoenix Technologies LTD','KVM'}

def flags():
	if 'hypervisor' in open("/proc/cpuinfo").read():
		print '\t\t [-]\033[1;31mDetected\033[1;m'
	else:
		print '\t\t \033[1;32mNo!\033[1;m'
		
def scsi():
	flag=0
	read=open("/proc/scsi/scsi").read().split(" ")
	
	
	if any("VMw" in s for s in read):
		print '\t\t [-]\033[1;31mDetected\033[1;m'
		flag=1
	if any("VBOX" in s for s in read):
		print '\t\t [-]\033[1;31mDetected\033[1;m'
		flag=1

	if(flag==0):
		print '\t\t \033[1;32mNo!\033[1;m'

def mac():
	
	mac=['00:05:69','00:0c:29','00:0C:29','00:1C:14','00:1c:14','00:50:56','08:00:27']
	
	try:
		addr= open("/sys/class/net/eth0/address").read()
		address=addr[0:8]
		#print address
		
		for i in mac:
			#print i
			if (i==address):
				print "\t\t[--]\033[1;31mDetected\033[1;m"
			
	except IOError as e:
		#print "\t\t I/O error({0}): {1}".format(e.errno, e.strerror)
		if(e.errno==2):
			print '\t\t \033[1;32mNo!\033[1;m'
    	
				

def presence():
	
	list_dir=os.listdir('/usr/bin/')
	if any("vmware-" in s for s in list_dir):
		print "[--]\033[1;31mVMware Detected\033[1;m"
		flag=1
	if any("VBox" in s for s in list_dir):
		print "[--]\033[1;31mVirtualBox Detected\033[1;m"
		flag=1
		
	if flag==0:
		print '\t\t \033[1;32mNo!\033[1;m'

def bios_vendor():
	name=open("/sys/class/dmi/id/bios_vendor").read()
	print name
	

def product_vendor():
	name=open("/sys/class/dmi/id/product_name").read()	
	print name
	
def sys_vendor():
	name=open("/sys/class/dmi/id/sys_vendor").read()
	for i in vendor_names:
		if i==name:
			print yes
	
			


def main():
	os.system('toilet -F metal -f bigascii12 DeViL')
        #print "\t\twww.github.com/srlkhmi/DeViL "
	print "\n\n"
	
	
	print "[*]Distribution : ", open("/proc/sys/kernel/ostype").read()
	print "[*]OS: ", open("/etc/lsb-release").read()[85:103]
	print "[*]Kernel Version :", open("/proc/sys/kernel/osrelease").read()
	
	
	
	print "[*]System Vendor :",open("/sys/class/dmi/id/sys_vendor").read()
	print "[*]Hypervisor: ", open("/sys/class/dmi/id/bios_vendor").read()
	print "[*]Board Vendor : ",open("/sys/class/dmi/id/board_vendor").read()
	
	print "[*]Host name: ",open("/proc/sys/kernel/hostname").read()
	
	print "[*]Presence of Virtual Machine: "
	presence()
	print "\n"
	
	print "VM Detection Techniques"
	
	print "\t [*] Hypervisor Flag"
	flags()
	
	print "\t [*] Checking SCSI "
	scsi()
	
	print "\t [*] Checking MAC Address "
	mac()
	
	print "\t [*] Checking bi0s Vendor "
	bios_vendor()
	
	print "\t [*] Checking Product Name "
	product_vendor()
	
	print "\t [*] Checking System Vendor "
	sys_vendor()

if __name__ == "__main__":
	main()
