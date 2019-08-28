/*  Copyright (C) <2019-08-28>  <zouzhenxing>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    You can also contact me by email <zouzhenxing.it@foxmail.com>.  */

#include <stdio.h>
#include <pthread.h>


//pthread_rwlock_t rwlock = PTHREAD_RWLOCK_INITIALIZER;
pthread_rwlock_t rwlock;
pthread_t ntid1;
pthread_t ntid2;

int rw_data;


void *pthread_write(void* arg) {
  int i;

  for (i = 0; i < 10; ++i) {
    sleep(1);
    printf("pthread_write, tid = %d\n", (int)pthread_self());
  }
}

void *pthread_read(void* arg) {
  int i;

  for (i = 0; i < 10; ++i) {
    sleep(1);
    printf("pthread_read, tid = %d\n", (int)pthread_self());
  }
}

int main(int argc, char const *argv[]) {
  int status = 0;

  status = pthread_rwlock_init(&rwlock, NULL);
  if (status) {
    printf("pthread_rwlock_init wrong: %d\n", strerror(status));
  }

  status = pthread_create(&ntid1, NULL, pthread_write, NULL);
  if (status) {
    printf("pthread_create ntid1 wrong: %d\n", strerror(status));
  }

  status = pthread_create(&ntid2, NULL, pthread_read, NULL);
  if (status) {
    printf("pthread_create ntid2 wrong: %d\n", strerror(status));
  }

  status = pthread_join(ntid1, NULL);
  if (status) {
    printf("pthread_join ntid1 wrong: %d\n", strerror(status));
  }

  status = pthread_join(ntid2, NULL);
  if (status) {
    printf("pthread_join ntid2 wrong: %d\n", strerror(status));
  }

  status = pthread_rwlock_destroy(&rwlock);
  if (status) {
    printf("pthread_rwlock_destory: %d\n", strerror(status));
  }

  return 0;
}

/* build: gcc pthread_rwlock_init.c -o thread -lpthread */
