#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

pthread_t ntid1;

void *pthread_fun(void *arg)
{
  while (1) {
    printf("thread_fun\n");
    sleep(1);
  }
}

int main(int argc, char const *argv[])
{
  int err;

  err = pthread_create(&ntid1, NULL, pthread_fun, NULL);
  if (err) {
    printf("pthread_create: %d\n", strerror());
    return 0;
  }
  else {
    //succeed
    pthread_detach(ntid1);
  }

  //分离的等不了
  // pthread_join(ntid1, NULL);
  // printf("pthread_create:");

  pthread_exit(NULL);
  return 0;
}
