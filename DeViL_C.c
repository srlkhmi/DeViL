#include<stdio.h>
#include<string.h>
#include<unistd.h>
#include<errno.h>
#include<stdlib.h>

#define VMWARE_HYPERVISOR_MAGIC 0x564D5868 
#define VMWARE_HYPERVISOR_PORT  0x5658  
#define VMWARE_PORT_CMD_GETVERSION      10 
#define UINT_MAX 0xFFFFFFFF 

extern int errno;

int print(int a)
{
	if(a>0)
	 {
	 	printf("\033[1;31m");
     	printf("\t\t[-] Detected! \n");
     	printf("\033[0m");
	 }
	 else
	 {
	 	printf("\033[1;32m");
	 	printf("\t\t No! \n");
	 	printf("\033[0m");
	 }
	return 0;
}

int hv_bit()
{

	int ecx=0;
	__asm__ volatile("cpuid" \
			: "=c"(ecx) \
			: "a"(0x01));
   return (ecx >> 31) & 0x1;
   
}

int hv_vendor()
{
	char vendor[13];
	//char strings[3]={"VMwareVMware",""}
	int ecx=0,ebx=0,edx=0;
	__asm__ volatile("cpuid" \
			: "=b"(ebx),"=c"(ecx),"=d"(edx) \
			: "a"(0x40000000));
   	sprintf(vendor  , "%c%c%c%c", ebx, (ebx >> 8), (ebx >> 16), (ebx >> 24));
	sprintf(vendor+4, "%c%c%c%c", ecx, (ecx >> 8), (ecx >> 16), (ecx >> 24));
	sprintf(vendor+8, "%c%c%c%c", edx, (edx >> 8), (edx >> 16), (edx >> 24));
	vendor[12] = 0x00;
	
   
}


int rdtsc_diff() {
	unsigned long long ret, ret2;
	unsigned eax, edx;
	__asm__ volatile("rdtsc" : "=a" (eax), "=d" (edx));
	ret  = ((unsigned long long)eax) | (((unsigned long long)edx) << 32);
	/* vm exit forced here. it uses: eax = 0; cpuid; */
	__asm__ volatile("cpuid" : /* no output */ : "a"(0x00));
	/**/
	__asm__ volatile("rdtsc" : "=a" (eax), "=d" (edx));
	ret2  = ((unsigned long long)eax) | (((unsigned long long)edx) << 32);
	return ret2 - ret;
}

int vmexit_cpuid()
{

	int avg=0,sum=0,sub,i;
	for (i = 0; i < 10; i++) {
		sub = rdtsc_diff();
		sum=+ sub;
		sleep(1);
	}
	avg=sum/10;
	
	if(avg>0 && avg<750)
	{
		return 0;
	}
	return 1;
}

int in()
{
	int eax=0,ebx=0,ecx=0,edx=0,ebx_val=0;
	__asm__ volatile("inl (%%dx)" 
			: "=a"(eax),"=c"(ecx),"=d"(edx),"=b"(ebx)\
			: "a"(VMWARE_HYPERVISOR_MAGIC),	"c" ( VMWARE_PORT_CMD_GETVERSION),"d"(VMWARE_HYPERVISOR_PORT), "b"(UINT_MAX)
			);
	printf(" Value of errno: %d\n ", errno);
	if(ebx==0x564D5868)
	{
		return 1;
	}
	
	return 0;

} 
int main()
{
	
	int i,a;
	a=hv_bit();
	printf("\t [*] Checking Hypervisor bit from CPUID instruction \n");
	print(a);
	
	printf("\t [*] Checking VMEXIT through CPUID instruction \n");
	a=vmexit_cpuid();
	print(a);
	
	a=hv_vendor();
	printf("\t [*] Checking Virtualization vendor string from CPUID instruction \n");
	//print(a);
	
	//printf("\t [*] Checking IN instruction \n");
	//a=in();
	//print(a);
	return 0;  

}
