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

struct hw_module_methods_t;


typedef struct hw_module_methods_t {
    /** Open a specific device */
    void(*open)(void);

} hw_module_methods_t;






#endif
