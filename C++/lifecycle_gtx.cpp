#include <iostream>

using namespace std;

class A
{
public:
	friend class B;
	friend void modify(A & ptr, int a);

public:
	A(int a)
	{
		this->a = a;
		cout << "A" << this->a << endl;
	}

	A(const A &  a) 
	{
		this->a = a.get_a();
		cout << "copy A" << this->a << endl;
	}
	~A()
	{
		cout << "~A" << this->a << endl;
	}
	int get_a() const
	{
		return this->a;
	}
protected:
	static int sta;
private:
	int a;

protected:
};

class B : public A
{
public:
	B(int a, int b): A(b),  objectA(a)
	{
		cout << "B" << endl;
	}
	~B()
	{
		cout << "~B"  << endl;
	}
	void setobjectA(int a)
	{
		objectA.a = a;
	}
	A get_objectA()
	{
		return this->objectA;	//这里调用拷贝构造函数返回匿名对象
	}
	void setAprivate(A & p, int a)
	{
		p.a = a;
	}
	void chengefatherstaticmem()
	{
		cout << A::sta << endl;
		A::sta = 1;
		cout << A::sta << endl;
	}
private:
	A objectA;
protected:
	
};
void modify(A & ptr, int a)
{
	ptr.a = a;
}

int A::sta = 0;

int main(int argc, char const *argv[])
{

	B b(2, 3);
	b.chengefatherstaticmem();
	return 0;	
}
