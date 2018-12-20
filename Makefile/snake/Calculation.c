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
#include "conio.h"
#include "stdlib.h"
#include "snake.h"
#include "bean.h"
#include "frame.h"
#include "key.h"

#define FRAME_LENGTH 150 //150
#define FRAME_WIDTH 40//40
#define FRAME_UP_DISTANCE 8
#define FRAME_LEFT_DISTANCE 30

static struct frame_config frame_default = {
	.length = FRAME_LENGTH,
	.width = FRAME_WIDTH,
	.up_distance = FRAME_UP_DISTANCE,
	.left_distance = FRAME_LEFT_DISTANCE,
};

static struct bean_config *bean_dev = NULL;
static struct snake *snake_dev = NULL;

void main(int argc, char const *argv[])
{
	int res = 0;
///while(1) { //!sleep(1)
		
		/*if(get_key_value(1) == 108){
			snake_dev->action.snake_list_move(snake_dev);
		}*/
		///get_key_value();
		//printf("%d\n", res);

		//sleep(1);
		
		//break;
///	}

	system("clear");

	snake_initialization(&snake_dev);

	res = bean_initialization(&bean_dev);
	if (res < 0)
		goto done;

	res = frame_create(frame_default);
	if (res < 0)
		goto done;
		
	res = bean_create(&frame_default, bean_dev);
	if (res < 0)
		goto done;

	snake_dev->action.snake_create(snake_dev);

//start :
	while(1){

	snake_dev->snake_move_direction = RIGHT_TO_LEFT;
		 //printf ("open /dev/input/event3 device error!\n");
		
		sleep(1);snake_dev->action.snake_list_move(snake_dev);
		sleep(1);
		snake_dev->action.snake_list_tail_add(snake_dev);
		snake_dev->action.snake_list_move(snake_dev);

}

	while(1);
done :
	printf("done, stop running !\n");
}
