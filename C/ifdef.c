#include <stdio.h>


#define __DEBUG


void main(int argc, char const *argv[])
{

#ifdef __DEBUG

	printf("1");
#else

	printf("2");

#endif
	printf("3");
	return;
}
