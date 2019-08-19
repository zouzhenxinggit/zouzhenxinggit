#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

pthread_t ntid1;

void pthread_clean(void *arg)
{
  printf("pthread_clean: %s\n", (char *)arg);
}

/**
 * void pthread_cleanup_push(void (*routine)(void *),
 *                                void *arg);
 * void pthread_cleanup_pop(int execute);
 */
void *pthread_fun(void *arg)
{
  pthread_cleanup_push(pthread_clean, "clean push 1 run");
  pthread_cleanup_push(pthread_clean, "clean push 2 run");

  printf("thread_fun start\n");
  sleep(1);
  printf("thread_fun stop\n");

  //execute = 0 取消对应的入栈， 清理函数取消
  //非分离的话是不会调用线程清理函数的
  pthread_cleanup_pop(0);
  pthread_cleanup_pop(1);

  pthread_exit((void *)0);
}

int main(int argc, char const *argv[])
{
  int err;

  err = pthread_create(&ntid1, NULL, pthread_fun, NULL);
  if (err) {
    printf("pthread_create: %d\n", strerror());
    return 0;
  }

  pthread_join(ntid1, NULL);
  return 0;
}
