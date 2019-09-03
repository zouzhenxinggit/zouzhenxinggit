/*
 * pthread_cond.c
 *
 * The windows message processing methods.
 *
 * Copyright (c) 1999-2000 Pawel W. Olszta. All Rights Reserved.
 * Written by Pawel W. Olszta, <olszta@sourceforge.net>
 * Creation date: Fri Dec 3 1999
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included
 * in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
 * OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
 * PAWEL W. OLSZTA BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
 * IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

/* -- GLOBAL VARIABLES ----------------------------------------------------- */

struct ListNode {
  int num;
  struct ListNode *node;
} *head = NULL;

struct RwStackList {
  pthread_mutex_t mutex;
  pthread_cond_t cond;
  pthread_t ntid1;
};

static struct RwStackList rw_list = {
  .mutex = PTHREAD_MUTEX_INITIALIZER,
  .cond = PTHREAD_COND_INITIALIZER,
};

/* -- PRIVATE FUNCTIONS ---------------------------------------------------- */

void PthreadClean(void *arg) {
  printf("PthreadClean: %s\n", (char *)arg);
}

void* PthreadFun1(void *arg) {
  int i = 0;
  struct ListNode *p = NULL;

  pthread_cleanup_push(PthreadClean, "clean push 1 run");
  while (1) {
    pthread_mutex_lock(&(rw_list.mutex));
    while (NULL == head) {
      pthread_cond_wait(&(rw_list.cond), &(rw_list.mutex));
    }
    p = head;
    printf("read stack list: %d\n", p->num);
    head = head->node;
    free(p);
    pthread_mutex_unlock(&(rw_list.mutex));
  }
  pthread_cleanup_pop(1);
}

int main(int argc, char const *argv[]) {
  int status = 0;
  int i = 0;
  struct ListNode *p = NULL;

  status = pthread_create(&(rw_list.ntid1), NULL, PthreadFun1, NULL);
  if (status) {
    printf("pthread_create ntid1 is wrong: %d\n", strerror(status));
  }

  /* add node to stack list and send siganl
   */
  for (i = 0; i < 10; i++) {
    p = (struct ListNode *)malloc(sizeof(struct ListNode));
    pthread_mutex_lock(&(rw_list.mutex));
    p->node = head;
    head = p;
    p->num = i;

    printf("write stack list is ok, count: %d\n", i + 1);
    pthread_cond_signal(&(rw_list.cond));
    pthread_mutex_unlock(&(rw_list.mutex));
    sleep(2);
  }

  status = pthread_cancel(rw_list.ntid1);
  if (status) {
    printf("pthread_cancel ntid1 is wrong: %d\n", strerror(status));
  }

  status = pthread_join(rw_list.ntid1, NULL);
  if (status) {
    printf("pthread_join ntid1 is wrong: %d\n", strerror(status));
  }
  return 0;
}

/* build: gcc -o thread pthread_cond.c -lpthread */
