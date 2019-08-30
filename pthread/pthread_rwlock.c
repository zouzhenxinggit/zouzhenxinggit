/*
 * pthread_rwlock.c
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

/* -- GLOBAL VARIABLES --------------------------------------------- */

/*
 * pthread variable
 */
pthread_rwlock_t rwlock;
// pthread_rwlock_t rwlock = PTHREAD_RWLOCK_INITIALIZER;
pthread_t ntid1;
pthread_t ntid2;

int rw_data = 8;

/* -- PRIVATE FUNCTIONS ---------------------------------------------------- */

/*
 * write pthread
 */
void *pthreadWrite(void* arg) {
  int i;

  for (i = 0; i < 10; ++i) {
    sleep(1);

    pthread_rwlock_wrlock(&rwlock);
    rw_data = i;
    pthread_rwlock_unlock(&rwlock);

    printf("pthread_write, tid = %d\n", (int)pthread_self());
  }
}

/*
 * read pthread
 */
void *pthreadRead(void* arg) {
  int i;

  for (i = 0; i < 10; ++i) {
    sleep(2);

    pthread_rwlock_rdlock(&rwlock);
    printf("%d\n", rw_data);
    pthread_rwlock_unlock(&rwlock);

    printf("pthread_read, tid = %d, rw_data\n", (int)pthread_self());
  }
}

/*
 * pthread_rwlock_wrlock && pthread_rwlock_rdlock
 * readlock - readlock Only one can be read at a time
 * writelock - writelock Only one can be write at a time
 * readlock - writelock priority write > read
 * writelock - not readlock, may be incomplete error
 */
int main(int argc, char const *argv[]) {
  int status = 0;

  status = pthread_rwlock_init(&rwlock, NULL);
  if (status) {
    printf("pthread_rwlock_init wrong: %d\n", strerror(status));
    return -1;
  }

  status = pthread_create(&ntid1, NULL, pthreadWrite, NULL);
  if (status) {
    printf("pthread_create ntid1 wrong: %d\n", strerror(status));
    return -1;
  }
  status = pthread_create(&ntid2, NULL, pthreadRead, NULL);
  if (status) {
    printf("pthread_create ntid2 wrong: %d\n", strerror(status));
    return -1;
  }

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

  status = pthread_rwlock_destroy(&rwlock);
  if (status) {
    printf("pthread_rwlock_destory: %d\n", strerror(status));
    return -1;
  }
  return 0;
}

/* build: gcc pthread_rwlock.c -o thread -lpthread */
