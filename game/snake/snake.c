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

//#define DEBUG
#include "snake.h"

struct snake snake_example= {
	.probe = {
		.snake_shape = {
			.snake_head_shape = SNAKE_HEAD_SHAPE,
			.snake_body_shape = SNAKE_BODY_SHAPE,
			.snake_tail_delete_shape = SNAKE_TAIL_DELETE_SHAPE,
		},
		//snake_row - 1; snake_column -1;
		.snake_head_init_position = {
				.snake_row = SNAKE_DEFAUTE_ROW,
				.snake_column = SNAKE_DEFAUTE_COLUMN,
		},
		.snake_lenght = SNAKE_DEFAUTE_LENGHT,
		.snake_eat_bead_num = SNAKE_DEFAUTE_EAT_BEAD_NUM,
	},
	.action = {
		.snake_create = snake_list_create,
		.snake_list_move = snake_list_move,
		.snake_list_tail_add =  snake_list_tail_add,
	},
	.snake_list = NULL,
	.snake_head = NULL,
	.snake_before_tail = {
		.snake_row = SNAKE_DEFAUTE_ROW - 2 + 5,
		.snake_column = SNAKE_DEFAUTE_COLUMN -1,
	},
	.snake_move_direction = RIGHT_TO_LEFT,
};

int snake_initialization(struct snake **snake_adev) 
{
	*snake_adev = &snake_example;

#ifdef DEBUG
	printf("snake_initialization%s\n",  (**snake_adev).probe.snake_shape.snake_head_shape);
	printf("snake_initialization%s\n",  snake_example.probe.snake_shape.snake_body_shape);
	printf("snake_initialization%s\n",  snake_example.probe.snake_shape.snake_tail_delete_shape);
#endif

	return 0;
}

static int snake_list_create(struct snake *snake_adev)
{
	int i;
	struct snake_list_node *p_snake_head = NULL;
	struct snake_list_node *p_snake_node = NULL;
	struct snake_list_node * p_tmp;
	int tmp_snake_row;
	int tmp_snake_column;

	p_snake_head = (struct snake_list_node*)malloc(sizeof(struct snake_list_node));
	if (NULL == p_snake_head) {
		printf("snake_list_create: error: Failed to allocate memory !\n");
		return -1;
	}

	//The default location of the header node.
	p_snake_head->snake_node_position.snake_row = \
		snake_adev->probe.snake_head_init_position.snake_row -1;
	p_snake_head->snake_node_position.snake_column = \
		snake_adev->probe.snake_head_init_position.snake_column - 1;

	//node number
	p_snake_head->num = 1;
	p_snake_head->snake_node_list_before = NULL;

#ifdef DEBUG
	printf("%d\n", p_snake_head->snake_node_position.snake_row);
	printf("%d\n", p_snake_head->snake_node_position.snake_column);
	printf("%d\n\n\n\n", p_snake_head->num);
#endif
	p_tmp = p_snake_head;

	for (i = 1; i < snake_adev->probe.snake_lenght; ++i) {
		p_snake_node = (struct snake_list_node*)malloc(sizeof(struct snake_list_node));
		if (NULL == p_snake_node) {
			printf("snake_list_create: error: Failed to allocate memory !\n");
		return -1;
	}

		p_tmp->snake_node_list_after = p_snake_node;
		p_snake_node->snake_node_list_before = p_tmp;

		p_snake_node->snake_node_position.snake_row = \
			p_tmp->snake_node_position.snake_row + 1;
		p_snake_node->snake_node_position.snake_column = \
			p_tmp->snake_node_position.snake_column;

		p_snake_node->num = p_tmp->num + 1;
		p_tmp = p_snake_node;

#ifdef DEBUG
		printf("snake_list_create:%d\n", p_snake_node->snake_node_position.snake_row);
		printf("snake_list_create:%d\n", p_snake_node->snake_node_position.snake_column);
		printf("snake_list_create%d\n\n\n\n", p_tmp->num);
#endif
	}
	p_tmp->snake_node_list_after = NULL;
	snake_adev->snake_head = p_snake_head;
	snake_adev->snake_tail = p_tmp;
	snake_adev->snake_list = p_snake_head;

#ifdef DEBUG
		printf("---------------------------------------\n");
		printf("snake_list_create%d\n",
			 ((struct snake_list_node*)snake_adev->snake_tail)->snake_node_position.snake_row);
		printf("snake_list_create%d\n", 
			((struct snake_list_node*)snake_adev->snake_tail)->snake_node_position.snake_column);
		printf("snake_list_create%d\n\n\n\n", 
			((struct snake_list_node*)snake_adev->snake_tail)->num);
#endif
		snake_list_print_defaute(snake_adev);
	return 0;
}

int snake_list_tail_add(struct snake *snake_adev)
{
	struct snake_list_node *p_snake_tail = (struct snake_list_node *)snake_adev->snake_tail;
	
	struct snake_list_node * p_tmp = NULL;

	p_tmp = (struct snake_list_node *)malloc(sizeof(struct snake_list_node));
	if (NULL == p_tmp) {
			printf("snake_list_tail_add: error: Failed to allocate memory !\n");
		return -1;
	}

	p_tmp->snake_node_position.snake_row = \
		snake_adev->snake_before_tail.snake_row;
	p_tmp->snake_node_position.snake_column = \
		snake_adev->snake_before_tail.snake_column;
	
	p_tmp->num =  snake_adev->probe.snake_lenght += 1;
	snake_adev->probe.snake_eat_bead_num += 1;

#ifdef DEBUG
	printf("%d\n", p_tmp->num);
	printf("%d\n", snake_adev->probe.snake_lenght);
	printf("%d\n", snake_adev->probe.snake_eat_bead_num);
	printf("%d\n", ((struct snake_list_node *)snake_adev->snake_tail)->snake_node_position.snake_row);
	printf("%d\n", ((struct snake_list_node *)snake_adev->snake_tail)->snake_node_position.snake_column);
	printf("%d\n", snake_adev->snake_before_tail.snake_row);
	printf("%d\n", snake_adev->snake_before_tail.snake_column);
#endif	

	p_snake_tail->snake_node_list_after = p_tmp;
	p_tmp->snake_node_list_before = p_snake_tail;
	p_tmp->snake_node_list_after = NULL;

	snake_adev->snake_tail = p_tmp;

	snake_list_print_update(snake_adev, 
	 										 p_tmp,
	 										  snake_adev->probe.snake_shape.snake_tail_delete_shape); 
	snake_list_print_update(snake_adev, 
	 										 p_tmp,
	 										  snake_adev->probe.snake_shape.snake_head_shape); 
}


void snake_list_move(struct snake *snake_adev)
{
	int i;
	struct snake_list_node *p_snake_tail = (struct snake_list_node *)snake_adev->snake_tail;

	p_snake_tail->snake_node_list_before->snake_node_list_after = NULL;
	p_snake_tail->snake_node_list_after = NULL;

	//delete snake tail
	snake_list_print_update(snake_adev, 
	 										  ((struct snake_list_node *)snake_adev->snake_tail),
	 										  snake_adev->probe.snake_shape.snake_tail_delete_shape);
	//save before tail
	snake_adev->snake_before_tail.snake_row = \
		((struct snake_list_node *)snake_adev->snake_tail)->snake_node_position.snake_row;
	snake_adev->snake_before_tail.snake_column = \
		((struct snake_list_node *)snake_adev->snake_tail)->snake_node_position.snake_column;

#ifdef DEBUG
	printf("%d\n", snake_adev->snake_before_tail.snake_row);
	printf("%d\n", snake_adev->snake_before_tail.snake_column);
#endif	
	//updata snake head befor position
	snake_list_print_update(snake_adev,
	 										  ((struct snake_list_node *)snake_adev->snake_head),
	 										  snake_adev->probe.snake_shape.snake_body_shape);

	p_snake_tail->snake_node_position.snake_row = \
		((struct snake_list_node *)snake_adev->snake_head)->snake_node_position.snake_row;
	p_snake_tail->snake_node_position.snake_column = \
		((struct snake_list_node *)snake_adev->snake_head)->snake_node_position.snake_column;

	p_snake_tail->snake_node_list_after = \
		((struct snake_list_node *)snake_adev->snake_head)->snake_node_list_after;
//change
	((struct snake_list_node *)snake_adev->snake_head)->snake_node_list_after->snake_node_list_before = \
	p_snake_tail;

	//Snakes move from right to left by default, Can't change direction directly
	switch(snake_adev->snake_move_direction)
	{
	case LEFT_TO_RIGHT:
	{
		((struct snake_list_node *)snake_adev->snake_head)->snake_node_position.snake_row += 1;
		break;
	}
	case RIGHT_TO_LEFT:
	{
		((struct snake_list_node *)snake_adev->snake_head)->snake_node_position.snake_row -= 1;
		break;
	}
	case UP_TO_BACK:
	{
		((struct snake_list_node *)snake_adev->snake_head)->snake_node_position.snake_column += 1;
		break;
	}
	case BACK_TO_UP:
	{
		((struct snake_list_node *)snake_adev->snake_head)->snake_node_position.snake_column -=1;
		break;
	}
	default:
		break;
	}

 	((struct snake_list_node *)snake_adev->snake_head)->snake_node_list_after = p_snake_tail;

	//tail node front move
	snake_adev->snake_tail = \
		((struct snake_list_node *)snake_adev->snake_tail)->snake_node_list_before;

	 p_snake_tail->snake_node_list_before = ((struct snake_list_node *)snake_adev->snake_head);

	//updata snake head  position
	snake_list_print_update(snake_adev,
	 										  ((struct snake_list_node *)snake_adev->snake_head),
	 										  snake_adev->probe.snake_shape.snake_head_shape);
}

void snake_list_print_defaute(struct snake *snake_adev)
{
	int i;
	struct snake_list_node * p_tmp = NULL;

	printf("\033[%d;%dH",
		 ((struct snake_list_node *)snake_adev->snake_list)->snake_node_position.snake_column + 8 + 2,
		 2 * ((struct snake_list_node *)snake_adev->snake_list)->snake_node_position.snake_row + 30 + 1);
	printf("%s", snake_adev->probe.snake_shape.snake_head_shape);
	printf("\033[0;0H\n");

	p_tmp = ((struct snake_list_node *)snake_adev->snake_list)->snake_node_list_after;
	for (i = 0; i < SNAKE_DEFAUTE_LENGHT - 1; ++i) {
		printf("\033[%d;%dH",
		 p_tmp->snake_node_position.snake_column + 8 + 2,
		 2 * p_tmp->snake_node_position.snake_row + 30 + 1);
		printf("%s", snake_adev->probe.snake_shape.snake_body_shape);
		printf("\033[0;0H\n");

		p_tmp = p_tmp->snake_node_list_after;
	}
}

void snake_list_print_update(struct snake *snake_adev,
												   struct snake_list_node* snake_node,
												   const char* snake_shape)
{
	printf("\033[%d;%dH",
		 ((struct snake_list_node *)snake_adev->snake_head)->snake_node_position.snake_column + 8 + 2,
		 2 * ((struct snake_list_node *)snake_adev->snake_head)->snake_node_position.snake_row + 30 + 1);
	printf("%s", snake_adev->probe.snake_shape.snake_head_shape);
	printf("\033[0;0H\n");

	printf("\033[%d;%dH",
		 snake_node->snake_node_position.snake_column + 8 + 2,
		 2 * snake_node->snake_node_position.snake_row + 30 + 1);
	printf("%s", snake_shape);
	printf("\033[0;0H\n");
}
