#include <stdio.h>


// # define DEBUG


void main(int argc, char const *argv[])
{
	
#ifdef DEBUG

	printf("1");
#else

	printf("2");
#
	
	printf("3");
	return;
}