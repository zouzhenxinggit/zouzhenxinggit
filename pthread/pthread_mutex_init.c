// #include <cutils/log.h>

#include <stdio.h>
#include <pthread.h>

static pthread_mutex_t write_mutex;
static pthread_once_t write_lock_init = PTHREAD_ONCE_INIT;
pthread_t ntid1;
pthread_t ntid2;

void ThreadLockInit() {
  int error_lock_init = 0;

  error_lock_init = pthread_mutex_init(&write_mutex, NULL);
  if (error_lock_init) {
    printf("创建线程锁错误\n");
  } else {
    printf("创建线程锁成功\n");
  }
}

void* pthread1_start(void* arg) {
  while (1) {
    sleep(1);
    printf("1\n");
  }
}

void* pthread2_start(char* arg) {
  while (1) {
    sleep(1);
    printf("%s\n", arg);
  }
}

void CreateThreadFramework() {
  int error_create_pthread = 0;
  int error_pthread_once = 0;

  //The first call to pthread_once() by any thread in a process,
  error_pthread_once = pthread_once(&write_lock_init, ThreadLockInit);
  if (error_pthread_once) {
    printf("创建线程锁错误\n");
  } else {
    printf("创建线程锁成功\n");
  }

  error_create_pthread = pthread_create(&ntid1, NULL,
                                        pthread1_start, NULL);
  if (error_create_pthread) {
    printf("创建线程1错误\n");
  } else {
    printf("创建线程1成功\n");
  }

  error_create_pthread = pthread_create(&ntid2, NULL,
                                        (void *) &pthread2_start, "2");
  if (error_create_pthread) {
    printf("创建线程2错误\n");
  } else {
    printf("创建线程2成功\n");
  }
}

int main(int argc, char const *argv[]) {
  int error_pthread_join = 0;

  CreateThreadFramework();

  error_pthread_join = pthread_join(ntid1, NULL);
  if (error_pthread_join) {
    printf("等待线程1就结束错误\n");
  } else {
    printf("等待线程1就结束成功\n");
  }

  error_pthread_join = pthread_join(ntid2, NULL);
  if (error_pthread_join) {
    printf("等待线程2就结束错误\n");
  } else {
    printf("等待线程2就结束成功\n");
  }
  return 0;
}
