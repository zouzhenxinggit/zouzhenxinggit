#include <iostream>

using namespace std;

class ALL
{
public:
	int all;
};

class A:    public virtual ALL
{
public:
	int a;
};

class B:    public virtual ALL
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

class E: public virtual  A,  public   B
{
public:
	int e;
};

#include <stdio.h>
int main(int argc, char const *argv[])
{

// cout << sizeof(A) << endl;
// cout << sizeof(B) << endl;
// cout << sizeof(C) << endl;
cout << sizeof(E) << endl;
// cout << sizeof(D) << endl;
// cout << sizeof(E) << endl;
E c;
c.a = 1;
c.b = 2;

c.e = 4;
// c.c = 4;
c.all = 5;

int *p = (int*)&c;
while(getchar())
{
	cout << *p << endl;
	p++;
}


return 0;
}