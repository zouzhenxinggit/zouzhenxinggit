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

#include "key.h"

void get_key_value(void)
{
  int res = 0;
  struct input_event key_probe;

  res = open ("/dev/input/event3", O_RDONLY);
  if (res <= 0) {
     printf ("open /dev/input/event3 device error!\n");
     //return -1;
  }
while(1){
  if (read (res, &key_probe, sizeof (key_probe)) == sizeof (key_probe)) {
    if (key_probe.type == EV_KEY) {
      if (key_probe.value == 0)
      {
        printf ("key = %d\n", key_probe.code);
        //close (res);
       //return key_probe.code;
      }
    }
  }
}
  close (res);
}

