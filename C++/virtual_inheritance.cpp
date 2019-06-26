#include <iostream>

using namespace std;

class ALL
{
public:
	int all;
};

class A: virtual public ALL
// class A: public ALL
{
public:
	int a;
};

class B: virtual public ALL
// class B: public ALL
{
public:
	int a;
};

class C: public A, public B
{
public:
	int c;
};



int main(int argc, char const *argv[])
{
	C c;
	c.A::a = 10;
	c.B::a = 20;

	cout << c.A::a << endl;
	cout << c.B::a << endl;

	//虚继承
	c.all = 10;

	cout << sizeof(A) <<endl;

	return 0;
}
