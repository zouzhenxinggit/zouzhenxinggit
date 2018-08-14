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

#include "stdio.h"
#include "stdlib.h"
#include "snake.h"
#include "bean.h"
#include "frame.h"

#define FRAME_LENGTH 10//150
#define FRAME_WIDTH 4//40
#define FRAME_UP_DISTANCE 8
#define FRAME_LEFT_DISTANCE 30

struct frame_config frame_default = {
	.length = FRAME_LENGTH,
	.width = FRAME_WIDTH,
	.up_distance = FRAME_UP_DISTANCE,
	.left_distance = FRAME_LEFT_DISTANCE,
};

void main(int argc, char const *argv[])
{
	system("clear");
	frame_create(frame_default);
	bean_create(&frame_default);
	//printf("\033[0;0H\n");

	while(1);
	//sleep(1);
	//while(1){
		//frame_create(frame_default);while(1);
		//sleep(1);
		//system("clear");
		//sleep(1);
	//}
}
