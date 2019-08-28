#include <stdio.h>


int f (int *__restrict x, int * __restrict y)
{
	*x = 0;
	*y = 1;
	return *x; //--->> optimize return 0;
}

int main(void)
{
	int n = 8;
	int m = 8;
	f(&n, &n);
	printf("%d\n", n);
}
