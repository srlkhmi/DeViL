#include<stdio.h>
#include<string.h>
#include<unistd.h>

int print(int a)
{
	if(a>0)
	 {
	 	printf("\033[1;31m");
     	printf("\t\t Detected! \n");
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

int main()
{
	
	int i,a;
	a=hv_bit();
	printf("\t [*] Checking Hypervisor bit from CPUID instruction \n");
	print(a);
	
	printf("\t [*] Checking VMEXIT through CPUID instruction \n");
	a=vmexit_cpuid();
	print(a);
	return 0;  

}
