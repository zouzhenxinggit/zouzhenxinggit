#include <stdio.h>
#include <pthread.h>

pthread_t ntid1;
pthread_t ntid2;
void *retval;

void pthread_fun1(char *arg)
{
  int i;
  printf("pthread_fun1 start\n");

  for (i = 0; i < 5; i++) {
    printf("%s\n", arg);
    sleep(1);
  }

  pthread_cancel(ntid2);
}

void pthread_fun2(char *arg)
{
  printf("pthread_fun2 start\n");

  while (1) {
    printf("%s\n", arg);
    sleep(1);
  }
}

int main(int argc, char const *argv[]) {

  int err; //true

  char* arg1 = "pthread1...";
  char* arg2 = "pthread2...";

  err = pthread_create(&ntid1, NULL, (void *)&pthread_fun1, arg1);
  if (err) {
    printf("pthread_create 1 err\n");
  }

  err = pthread_create(&ntid2, NULL, (void *)&pthread_fun2, arg2);
  if (err) {
    printf("pthread_create 2 err\n");
  }

  while (1) {
    sleep(1);
  }
  return 0;
}
