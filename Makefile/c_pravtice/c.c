/* Copyright (c) 2015-2018, The Linux Foundation. All rights reserved.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 and
 * only version 2 as published by the Free Software Foundation.
 *  
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
*/

#include <stdio.h>
#include <stdlib.h>

int Array_create(int **Array, int number)
{
  int res = 0, i = 0;
  int num = number;
  int* Array_tmp = NULL;

  Array_tmp = (int *)malloc(sizeof(int) * num);
  if (NULL == Array_tmp) {
    printf("create malloc is error");
    return -1;
  }

  for (i; i < num; ++i)
    scanf("%d",&Array_tmp[i]);
    //printf("%d\n", Array_tmp[i]);

  *Array = Array_tmp;
  return res;
}

int Array_printf(int *Array, int num)
{
  int i = 0;

  if (NULL == Array) {
    printf("Array_printf: Array is NULL");
    return -1;
  }

  for (i; i < num; ++i)
    printf("%d\n", Array[i]);

  return 0;
}

int Array_Sort(int *Array, int num)
{
  int i = 0, j = 0;
  int tmp = 0;

  if (NULL == Array) {
    printf("Array_Sort: Array is NULL");
    return -1;
  }

  for (i; i < num; ++i) {
    for (j = i + 1; j < num; ++j)
    {
      if (Array[i] > Array[j]) {
        tmp = Array[i];
        Array[i] = Array[j];
        Array[j] = tmp;
      }
    }
  }
  return 0;
}


void main(int argc, char const *argv[])
{
  int res = 0;
  int number = 5;
  int *Array = NULL;

  //create
  res = Array_create(&Array, number);
	if (res < 0) {
    printf("Array_create is error \n");
    return;
  }

  //work
  res = Array_Sort(Array, number);
  if (res < 0) {
    printf("Array_Sort is error \n");
    return;
  }

  //printf sort after
  res = Array_printf(Array, number);
  if (res < 0) {
    printf("Array_printf is error \n");
    return;
  }

  printf("%s\n", "okokok...");
	while(1);
	return;
} 
