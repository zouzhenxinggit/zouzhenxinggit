#include <iostream>

using namespace std;

class ALL
{
public:
	int all;
};

class A: virtual public ALL
{
public:
	int a;
};

class B: virtual public ALL
{
public:
	int b;
};

class C: public A, public B
{
public:
	int c;
};

class CC: public C
{
public:
int cc;
};

class D: public virtual A, public virtual B
{
public:
	int d;
};

 // class E: public  B, public virtual A
  class E: public virtual A, public  B
{
public:
	int e;
};

#include<stdio.h>

int main(int argc, char const *argv[])
{
	// E c;
	// c.e = 1;
	// c.a = 2;
	// c.b = 3;
	// c.all = 4;

	// int *p = (int*)&(c);

	// while(1) {
	// 	cout << *p << endl;
	// 	p++;
	// 	getchar();
	// }

	// cout << sizeof(C) << endl;
	// cout << sizeof(CC) << endl;
	// cout << sizeof(D) << endl;
	cout << sizeof(E) << endl;
	return 0;
}

