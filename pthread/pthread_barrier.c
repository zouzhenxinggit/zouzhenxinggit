/*
 * pthread_barrier.c
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

#include <stdio.h>
#include <pthread.h>

/* -- DEFINITIONS ---------------------------------------------------------- */

#define BARRIER_NUMBER    3

/* -- GLOBAL VARIABLES ----------------------------------------------------- */

/*
 * pthread variable
 */
pthread_barrier_t barrier;
pthread_t ntid1;
pthread_t ntid2;

/* -- PRIVATE FUNCTIONS ---------------------------------------------------- */

void *threadFun1(void *arg) {
  pthread_barrier_wait(&barrier);
  while(1) {
    printf("-threadFun1-\n");
    sleep(1);
  }
}

void *threadFun2(void *arg) {
  pthread_barrier_wait(&barrier);
  while(1) {
    printf("-threadFun2-\n");
    sleep(1);
  }
}

int main(int argc, char const *argv[]) {
  int status;

  /* create pthread barrier
   */
  status = pthread_barrier_init(&barrier, NULL, BARRIER_NUMBER);
  if (status) {
    printf("pthread_barrier_init wrong! %d", strerror(status));
    return -1;
  }

  /* create pthread
   */
  status = pthread_create(&ntid1, NULL, threadFun1, NULL);
  if (status) {
    printf("thread1 create wrong! %d", strerror(status));
    return -1;
  }
  status = pthread_create(&ntid2, NULL, threadFun2, NULL);
  if (status) {
    printf("thread2 create wrong! %d", strerror(status));
    return -1;
  }

  /* open barrier, destroy barrier
   */
  pthread_barrier_wait(&barrier);
  status = pthread_barrier_destroy(&barrier);
  if (status) {
    printf("pthread_barrier_destroy wrong! %d", strerror(status));
    return -1;
  }

  /* main thread wait other thread stop
   */
  status = pthread_join(ntid1, NULL);
  if (status) {
    printf("pthread_join ntid1 wrong: %d\n", strerror(status));
    return -1;
  }
  status = pthread_join(ntid2, NULL);
  if (status) {
    printf("pthread_join ntid2 wrong: %d\n", strerror(status));
    return -1;
  }
  return 0;
}

/* build: gcc pthread_spinlock.c -o thread -lpthread */
