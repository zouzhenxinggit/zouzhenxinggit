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
    pid_t pid = getpid();
    pthread_t tid = pthread_self();

    //打印线程1 pid tid
    printf("thread1 pid: %d\n", (int)pid);
    printf("thread1 tid: %u\n", (int)tid);
    sleep(1);
  }
  // return((void*)0);
}

void *thread_fun2(void *arg)
{
  while (1) {
    printf("hello_word2, printf main pid\n");
    pid_t pid = getpid();
    pthread_t tid = pthread_self();

    //打印线程2 pid tid
    printf("thread2 pid: %d\n", (int)pid);
    printf("thread2 tid: %u\n", (int)tid);
    sleep(2);
  }
  // return((void*)0);
}

int main(int argc, char const *argv[]) {
  /* code */
  // 1.创建线程号,线程标识
  pthread_t ntid1;
  pthread_t ntid2;

  //打印主线程号
  pthread_t tid = pthread_self();
  printf("main thread tid: %u\n", (int)tid);

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

  // 主线程打印子线程号
  printf("main thread ntid1: %u\n", (int)ntid1);
  printf("main thread ntid2: %u\n", (int)ntid2);

  while (1) {
    /* code */
    sleep(1);
  }
  //printf("run");
  return 0;
}
