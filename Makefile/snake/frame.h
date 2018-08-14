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

#ifndef _SNAKE_FRAME_
#define _SNAKE_FRAME_

#include "stdio.h"

#define loop_output(num, end) \
    for (num = 0; num < end; ++num)

struct frame_config {
	unsigned int length;
	unsigned int width;
	unsigned int up_distance;
	unsigned int left_distance;
}; 

struct ranks {
	char* row_down;
	char row_up;
	char column;	
};

struct map_config {
	struct ranks limit;
	char outside;
	char space;
	char change_line;
	//add..
}; 

enum {
	MAP_OUTSIDE = '/',
	MAP_SPACE = ' ',
	MAP_CHANGE_LINE = '\n',
	MAP_ROW_UP = '_',
	MAP_COLUMN = '|',
};

void frame_create(struct frame_config frame_params);

#endif
