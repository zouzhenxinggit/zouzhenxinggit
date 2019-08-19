#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

/**
 *  gcc -o thread multi_thread.c -lpthread
 */

void *thread_fun1(void *arg)
{
  int i = 0;

  printf("hello_word1, printf main pid\n");

  for(i; i < 5; i++) {
    printf("-%d-\n", i);
    sleep(1);
  }

//pthread_exit是当前退出线程, 释放线程的栈空间.(只要线程结束, 线程栈空间都会被释放掉)
//但是不用join的话, 父线程中子线程的维护信息不会被释放, 创建很多线程的话,父类的栈空间会满
//join等待其他线程结束, 并释放父线程中子线程的维护信息
  pthread_exit(NULL);
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

  return 0;
}
