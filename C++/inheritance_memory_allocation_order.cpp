#include <iostream>

using namespace std;

class A
{
	int a;
public:
	A(int a)
	{
		cout << "A" << endl;
		a = a;
	}
	~A()
	{
		cout << "~A" << endl;
	
	}
};



class B : public  A
{
	int b;
public:
	B() : A(2)
	{
		cout << "B" << endl;
	
	}
	~B()
	{
		cout << "~B" << endl;
	
	}
};

class C : public  B
{
	int c;
public:
	C() 
	{
		cout << "C" << endl;
	
	}
	~C()
	{
		cout << "~C" << endl;
	
	}
};

int main(int argc, char const *argv[])
{
	C c;
	return 0;
}
