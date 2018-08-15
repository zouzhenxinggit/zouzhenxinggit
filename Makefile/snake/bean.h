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

#ifndef _SNAKE_BEAN_
#define _SNAKE_BEAN_

#include "time.h"
#include "stdio.h"
#include "frame.h"
#include "stdlib.h"

#define BEAN_MAKE "㊉"
#define BEAN_DEL "  "

struct bean_shape {
	char* bean_make;
	char* bean_del;
};

struct bean_config {
	unsigned int row;
	unsigned int column;
	struct bean_shape bean_shape_params;
};

int rand_create(unsigned int *start/* out */,
							unsigned int *end/* out */,
							struct frame_config *frame_params/* in */);

int bean_initialization(struct bean_config **bean_adev);

int bean_create(struct frame_config *frame_params,
						   struct bean_config *bean_adev);

void bean_delete(struct bean_config *bean_adev);

#endif
