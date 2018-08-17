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
	},
	.snake_list = NULL,
	.snake_head = NULL,
};

int snake_initialization(struct snake **snake_adev) 
{
	*snake_adev = &snake_example;

#ifdef DEBUG
	printf("%s\n",  (**snake_adev).probe.snake_shape.snake_head_shape);
	printf("%s\n",  snake_example.probe.snake_shape.snake_body_shape);
	printf("%s\n",  snake_example.probe.snake_shape.snake_tail_delete_shape);
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

		p_tmp->snake_node_list_after = p_snake_node;
		p_snake_node->snake_node_list_before = p_tmp;

		p_snake_node->snake_node_position.snake_row = \
			p_tmp->snake_node_position.snake_row + 1;
		p_snake_node->snake_node_position.snake_column = \
			p_tmp->snake_node_position.snake_column;

		p_snake_node->num = p_tmp->num + 1;
		p_tmp = p_snake_node;

#ifdef DEBUG
		printf("%d\n", p_snake_node->snake_node_list_before->snake_node_position.snake_row);
		printf("%d\n", p_snake_node->snake_node_list_before->snake_node_position.snake_column);
		printf("%d\n\n\n\n", p_tmp->num);
#endif
	}
	p_tmp->snake_node_list_after = NULL;
	snake_adev->snake_head = p_snake_head;
	snake_adev->snake_tail = p_tmp;
	snake_adev->snake_list = p_snake_head;

#ifdef DEBUG
		printf("---------------------------------------\n");
		printf("%d\n", ((struct snake_list_node*)snake_adev->snake_tail)->snake_node_position.snake_row);
		printf("%d\n", ((struct snake_list_node*)snake_adev->snake_tail)->snake_node_position.snake_column);
		printf("%d\n\n\n\n", ((struct snake_list_node*)snake_adev->snake_tail)->num);
#endif
	return 0;
}

/*
void snake_list_tail_add(struct snake *snake_adev,
									struct snake_position* snake_pos)
{
	struct snake_list_node *p_snake_tail = (struct snake_list_node *)snake_adev->snake_tail;
	struct snake_list_node *p_snake_node = NULL;
	struct snake_list_node * p_tmp;


}*/

//
void snake_list_front_move(struct snake *snake_adev)
{
	struct snake_list_node *p_snake_tail = (struct snake_list_node *)snake_adev->snake_tail;

	p_snake_tail->snake_node_list_before->snake_node_list_after = NULL;
	p_snake_tail->snake_node_list_after = NULL;

	p_snake_tail->snake_node_position.snake_row = \
		((struct snake_list_node *)snake_adev->snake_head)->snake_node_position.snake_row;
	p_snake_tail->snake_node_position.snake_column = \
		((struct snake_list_node *)snake_adev->snake_head)->snake_node_position.snake_column;

	p_snake_tail->snake_node_list_after = \
		((struct snake_list_node *)snake_adev->snake_head)->snake_node_list_after;

	snake_adev->snake_head->snake_node_position.snake_row -= 1;
	//snake_adev->snake_head->snake_node_position.snake_column
 	snake_adev->snake_head->snake_node_list_after = p_snake_tail;

	//尾节点变成之前的了
	snake_adev->snake_tail = snake_adev->snake_tail->snake_node_list_before;
}




void snake_list_for_each(void) 
{

}

// head - > node -> node _> tail_node 
//head ->  tail_node -> node -> new _tail_node
//head ->left node -> node _> tail_node 

void snake_list_move(void)
{

}

void snake_list_turn_left(void)
{

}

void snake_list_turn_right(void)
{

}



/* 
int snake_initialization(struct snake_config **snake_adev);
 


2 创建链表 初始化节点2个 方块当蛇身体 这个链表要有头指针


 
3 并挂载自己实现的向左 向右 函数

4.snake run ()



	


在链表上添加尾巴

向左边 链表头节点计算

向右边


蛇移动  链表尾巴移动到头指针后



struct snake {
	蛇的头和身体的字符串
	蛇的当前长度
	蛇吃的掉的豆子number


	蛇的初始位置


	蛇头的横竖坐标的链表
	蛇头移动函数
	蛇行进的速度
	

	得到头要移动的下一个位置
} 

初始化bena的时候失败需要释放内存 

主函数只是传一个指针 其他的放在snake里面就好。

打印字符串形式的枚举的变量
*/