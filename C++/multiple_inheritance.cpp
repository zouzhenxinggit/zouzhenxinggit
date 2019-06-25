#include <iostream>

using namespace std;

class A
{
public:
	int a;
};

class B
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
	return 0;
}