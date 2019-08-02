#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

/**
 *  gcc -o thread multi_thread.c -lpthread
 */
 /* code */
 // 1.创建线程号,线程标识

pthread_t ntid1;
pthread_t ntid2;
void * retval;

void thread_fun1(char *pstr)
{
  while(1) {
    printf("-%s-\n", pstr);
    sleep(1);
  }
}

void thread_fun2(char *pstr)
{
  int i = 0;
  for(i; i < 10; i++) {
    printf("-%s-\n", pstr);
    sleep(1);
  }
}

int main(int argc, char const *argv[])
{
  char *p1 = "thread1";
  char *p2 = "thread2";

  //创建线程,成功返回0
  int err;
  err = pthread_create(&ntid1, NULL, (void*)&thread_fun1, p1);
  if (err) {
    printf("thread create error! %d", strerror(err));
    return 0;
  }

  err = pthread_create(&ntid2, NULL, (void *)&thread_fun2, p2);
  if (err) {
    printf("thread create error! %d", strerror(err));
    return 0;
  }

  //挂起当前线程，等待其他线程运行完毕后，恢复当前线程
  //hang current thread, wait other thread run after, restore current thread.
  pthread_join(ntid2, &retval);
  printf("ssssss\n");printf("ssssss\n");printf("ssssss\n");
  return 0;
}
