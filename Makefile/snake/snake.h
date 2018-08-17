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

 #ifndef _SNAKE_SNAKE_
#define _SNAKE_SNAKE_

#include "stdio.h"
#include "stdlib.h"

#define SNAKE_HEAD_SHAPE "**"
#define SNAKE_BODY_SHAPE "▇▇"
#define SNAKE_TAIL_DELETE_SHAPE "  "
#define SNAKE_DEFAUTE_ROW 10
#define SNAKE_DEFAUTE_COLUMN 10
#define SNAKE_DEFAUTE_EAT_BEAD_NUM 0
#define SNAKE_DEFAUTE_LENGHT 5

struct snake_body_shape {
	char *snake_head_shape;
	char *snake_body_shape;
	char *snake_tail_delete_shape;
};

struct snake_position {
	unsigned int snake_row;
	unsigned int snake_column;
};

//struct listnode {
//	struct listnode *snake_list_node ; 
//};

struct snake_list_node {
	struct snake_position snake_node_position;
	struct snake_list_node* snake_node_list_after;
	struct snake_list_node* snake_node_list_before;
	unsigned int num;
};

struct snake_probe {
	struct snake_body_shape snake_shape;
	struct snake_position snake_head_init_position;
	unsigned int snake_lenght;
	unsigned int snake_eat_bead_num;
};

struct snake; 
struct snake_action {
	int (*snake_create)(struct snake *snake_adev);
};

struct snake {
	struct snake_probe probe;
	struct snake_action action;
	void *snake_list; 
	void *snake_head;
	void *snake_tail;
};

int snake_initialization(struct snake **snake_adev) ;
static int snake_list_create(struct snake *snake_adev);

#endif
