#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 创建随机数数组 */
void create_rand_array(int **array/*out*/, int array_len/*in*/)
{
	int i = 0;
	int *tmp = (int *)malloc(sizeof(int) * array_len);

	for (i = 0; i < array_len; ++i)
		tmp[i] = rand()%10;
	*array = tmp;
}

/* 选择排序 */
void sort_array_choose(int **array_in/*in out*/, int array_len/*in*/)
{
	int *tmp = *array_in;
	int value = 0, index = 0;

	if (NULL == array_in)
	{	
		printf("%s\n", "sort_array_choose : error : array_in is null");
		return;
	}

	int i = 0, j = 0;
	for (i = 0; i < array_len; ++i)
	{
		index = i;
		for (j = i+1; j < array_len; ++j)
		{
			if (tmp[j] < tmp[index])
				index = j;
		}
		if (!(i == index))
		{
			value = tmp[index];
			tmp[index] = tmp[i];
			tmp[i] = value;
		}
		
	}
}


/* 冒泡排序 */
void sort_array_bubbling(int **array_in/*in out*/, int array_len/*in*/)
{
	int *tmp = *array_in;
	int value = 0;

	if (NULL == array_in)
	{	
		printf("%s\n", "sort_array_bubbling : error : array_in is null");
		return;
	}

	int i = 0, j = 0;
	for (i = 0; i < array_len; ++i)
	{
		for (j = 0; j < array_len-1-i; ++j)
		{
			if (tmp[j] > tmp[j+1])
			{
				value = tmp[j];
				tmp[j] = tmp[j+1];
				tmp[j+1] = value;
			}
		}
	}
}

int print_array(int *array_in/*in*/, int array_len/*in*/)
{
	if (NULL == array_in)
	{	
		printf("%s\n", "print_array : error : array_in is null");
		return -1;
	}
	int i = 0;
	for (i = 0; i < array_len; ++i)
		printf("%d\n", array_in[i]);
	return 0;
}

/* 二分法排序 */
// 1 2 3 3 5 5 6 6 7 9
// 0 1 2 3 4 5 6 7 8 9
int binary_search(int *array/*in*/, int len/*in*/, int value/*in*/)
{
	int *tmp = array;
	int head = 0, end = len -1;
	int mid = 0;

	if (NULL == array)
	{	
		printf("%s\n", "binary_search : error : array is null");
		return -1;
	}
	while(head <= end)
	{
		mid  = (head + end)/2;
		if (value < tmp[mid])
		{
			end = mid - 1;
		}
		else if (value > tmp[mid])
		{
			head = mid + 1;
		}
		else if (value == tmp[mid])
			return mid;
	}
	return -1;
}


int main(int argc, char const *argv[])
{
	int *array_value = NULL;
	int result;

	create_rand_array(&array_value, 10);
	// print_array(array_value, 10);

	// sort_array_bubbling(&array_value, 10);
	sort_array_choose(&array_value, 10);
	print_array(array_value, 10);

	result = binary_search(array_value, 10, 3);
	printf("***********\n");
	printf("%d\n", result);

	return 0;
}
