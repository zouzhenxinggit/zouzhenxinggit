#include <stdio.h>
#include <pthread.h>

static pthread_mutex_t write_malloc_mutex;
static pthread_once_t write_malloc_lock_init = PTHREAD_ONCE_INIT;

int p_frequent_operator_var = 0;

void ThreadLockInit() {
  int status = 0;

  status = pthread_mutex_init(&write_malloc_mutex, NULL);
  if (status) {
    printf("pthread_mutex_init error\n");
  }
}

void* Pthread1Start(void* arg) {
  int i = 0;

  for ( i; i < 50000; i++) {
    pthread_mutex_lock(&write_malloc_mutex);
    p_frequent_operator_var++;
    pthread_mutex_unlock(&write_malloc_mutex);
  }
}

void* Pthread2Start(char* arg) {
  int i = 0;

  for ( i; i < 50000; i++) {
    pthread_mutex_lock(&write_malloc_mutex);
    p_frequent_operator_var++;
    pthread_mutex_unlock(&write_malloc_mutex);
  }
}

void CreateThreadFramework() {
  int status = 0;

  //The first call to pthread_once() by any thread in a process,
  status = pthread_once(&write_malloc_lock_init, ThreadLockInit);
  if (status) {
    printf("pthread_once error\n");
  }

  status = pthread_create(&ntid1, NULL, Pthread1Start, NULL);
  if (status) {
    printf("pthread_create1 error\n");
  }

  status = pthread_create(&ntid2, NULL, (void *) &Pthread2Start, "2");
  if (status) {
    printf("pthread_create2 error\n");
  }
}

int main(int argc, char const *argv[]) {
  int status = 0;
  pthread_t ntid1;
  pthread_t ntid2;

  CreateThreadFramework();

  status = pthread_join(ntid1, NULL);
  if (status) {
    printf("pthread_create2 error\n");
  }

  status = pthread_join(ntid2, NULL);
  if (status) {
    printf("pthread_create2 error\n");
  }

  printf("end resulf = %d\n", p_frequent_operator_var);
  return 0;
}
