#include <stdio.h>
#include <stdlib.h>

unsigned int hash(char *hash_value, unsigned int value)
{
	int i = 0;
	int s = 0;
	for (; i < strlen(hash_value); ++i)
		s += hash_value[i];
	return s / value;
}

int main(void)
{
	char *p = "abcdefg";

	printf("%d",hash(p, 10));
	return 0;
}