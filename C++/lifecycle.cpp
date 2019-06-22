#include <iostream>

using namespace std;

class A
{
public:
	friend class B;
	friend void modify(A & ptr, int a);
	A(){}
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
private:
	int a;

protected:
};

class B
{
public:
	B(int a): objectA(a)
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
private:
	A objectA;
protected:
	
};
void modify(A & ptr, int a)
{
	ptr.a = a;
}

int main(int argc, char const *argv[])
{

	A a = (56);
	cout << a.get_a() <<endl;

	modify(a, 99);
	cout << a.get_a() <<endl;

	//////////////////////////////////////
	B b(74);
	cout << b.get_objectA().get_a() << endl;

	b.setobjectA(89);
	cout << b.get_objectA().get_a() << endl;
	
	/////////////////////////////////////
	b.setAprivate(a, 77);
	cout << a.get_a() <<endl;
	return 0;	
}

// A56
// 56
// 99
// A74
// B
// copy A74
// 74
// ~A74
// copy A89
// 89
// ~A89
// 77
// ~B
// ~A89
// ~A77