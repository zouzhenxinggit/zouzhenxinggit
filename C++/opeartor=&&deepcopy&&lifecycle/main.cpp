#include "deepcopy.h"

#include <iostream>
#include <string.h>

int main(int argc, char const *argv[])
{
	DeepCopy cases1((char*)"123", strlen("123"));
	DeepCopy cases2((char*)"45678", strlen("45678"));

	DeepCopy cases3 = (cases1 = cases2);

	DeepCopy cases4(cases1);
	cases4 = cases1;

	cases4 = cases1 = cases2;
	return 0;
}
