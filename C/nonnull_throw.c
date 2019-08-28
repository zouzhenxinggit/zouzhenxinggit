#include <stdio.h>

// __nonnull 参数不为空，()标识第几个参数
// 在C里面，这个宏完全没有意义。当这个头文件被C++引用时，才有意义，其意义是声明这个函数支持C++里的throw异常功能。
int fun(char *str1, char *str2) __THROW __nonnull((1));

int main()
{
	char *p = NULL;
	fun(p, NULL);
}

int fun(char * str1, char *str2) 
{
	printf("%p\n", str1);
	printf("%p\n", str2);
}
