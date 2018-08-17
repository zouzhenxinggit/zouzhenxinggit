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
#include "frame.h"
#define ROW_DOWN "¯"
static struct map_config map_default = {
	.limit = {
		.row_up = MAP_ROW_UP,
		.row_down = ROW_DOWN,
		.column = MAP_COLUMN,
	},
	.outside = MAP_OUTSIDE,
	.space = MAP_SPACE,
	.change_line = MAP_CHANGE_LINE,
};

int frame_create(struct frame_config frame_params)
{
	unsigned int i, j;

	if (frame_params.length < 5 || frame_params.width <  5) {
		printf("error: space too small !\n");
		return -1;
	}
	
	loop_output(i, frame_params.up_distance - 1)
		printf("%c", map_default.change_line);

	loop_output(i, frame_params.left_distance - 2)
		printf("%c", map_default.space);
	
	loop_output(i, frame_params.length + 4)
		printf("%c", map_default.outside);
	
	printf("%c", map_default.change_line);

	loop_output(i, frame_params.left_distance - 2)
		printf("%c", map_default.space);
	
	printf("%c", map_default.outside);
	printf("%c", map_default.space);

	loop_output(i, frame_params.length)
		printf("%c", map_default.limit.row_up);
		
	printf("%c", map_default.space);
	printf("%c", map_default.outside);
	printf("%c", map_default.change_line);

	loop_output(j, frame_params.width) {
		loop_output(i, frame_params.left_distance - 2)
			printf("%c", map_default.space);
		
		printf("%c", map_default.outside);
		printf("%c", map_default.limit.column);

		loop_output(i, frame_params.length)
			printf("%c", map_default.space);

		printf("%c", map_default.limit.column);
		printf("%c", map_default.outside);
		printf("\n");
	}

	loop_output(i, frame_params.left_distance - 2)
		printf("%c", map_default.space);
	
	printf("%c", map_default.outside);
	printf("%c", map_default.space);

	loop_output(i, frame_params.length)
		printf("%s", map_default.limit.row_down);
		
	printf("%c", map_default.space);
	printf("%c", map_default.outside);
	printf("%c", map_default.change_line);

	loop_output(i, frame_params.left_distance - 2)
		printf("%c", map_default.space);

	loop_output(i, frame_params.length + 4)
		printf("%c", map_default.outside);

	printf("%c\a", map_default.change_line);

	return 0;
}
