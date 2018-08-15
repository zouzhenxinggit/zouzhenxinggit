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

#define DEBUG
#include "bean.h"



int rand_create(unsigned int *start,
							unsigned int *end,
							struct frame_config *frame_params)
{
	if (NULL == start || NULL == end || NULL == frame_params) {
#ifdef DEBUG
		printf("error: Illegal parameter\n");
 #endif
		return -1;
	}

	*start = rand()%((*frame_params).length / 2);
	*end = rand()%((*frame_params).width);
	return 0;
}

int bean_initialization(struct bean_config **bean_adev)
{
	struct bean_config *bean_tmp = NULL;

	srand((unsigned)time(NULL));

	bean_tmp = (struct bean_config*) malloc (sizeof(struct bean_config));

	if (NULL == bean_tmp){
#ifdef DEBUG
		printf("error: Failed to allocate memory !\n");
 #endif
		return -1;
	}

	bean_tmp->bean_shape_params.bean_make = BEAN_MAKE;
	bean_tmp->bean_shape_params.bean_del = BEAN_DEL;

	*bean_adev = bean_tmp;

	return 0;
}

int bean_create(struct frame_config *frame_params,
						   struct bean_config *bean_adev)
{ 
	int bean_row, bean_column, res = 0;

	if (rand_create(&bean_row, &bean_column, frame_params) != 0){
#ifdef DEBUG
		printf("error: Random number failure !\n");
 #endif
		return -1;
	}

	bean_adev->row = bean_row;
	bean_adev->column = bean_column;
	
	printf("\033[%d;%dH", (*bean_adev).column + 8 + 2, 2 * (*bean_adev).row + 30 + 1);
	printf("%s", bean_adev->bean_shape_params.bean_make);
	printf("\033[0;0H\n");
	sleep(1);

	return 0;
}

void bean_delete(struct bean_config *bean_adev)
{ 
	printf("\033[%d;%dH", (*bean_adev).column + 8 + 2, 2 * (*bean_adev).row + 30 + 1);
	printf("%s", bean_adev->bean_shape_params.bean_del);
	printf("\033[0;0H\n");
}
