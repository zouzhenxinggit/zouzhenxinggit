#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

/**
 *  gcc -o thread multi_thread.c -lpthread
 */

void *thread_fun1(void *arg)
{
  while (1) {
    printf("hello_word1, printf main pid\n");
    sleep(1);
  }
  // return((void*)0);
}

void *thread_fun2(void *arg)
{
  while (1) {
    printf("hello_word2, printf main pid\n");
    sleep(2);
  }
  // return((void*)0);
}

int main(int argc, char const *argv[]) {
  /* code */
  // 1.创建线程号,线程标识
  pthread_t ntid1;
  pthread_t ntid2;

  //创建线程,成功返回0
  int err;
  err = pthread_create(&ntid1, NULL, thread_fun1, NULL);
  if (err) {
    printf("thread create error! %d", strerror(err));
    return 0;
  }

  err = pthread_create(&ntid2, NULL, thread_fun2, NULL);
  if (err) {
    printf("thread create error! %d", strerror(err));
    return 0;
  }

  while (1) {
    /* code */
    sleep(1);
  }
  //printf("run");
  return 0;
}
