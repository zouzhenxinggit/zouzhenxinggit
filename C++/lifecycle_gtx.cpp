#include <iostream>

using namespace std;

class A
{
public:
	friend class B;
	friend void modify(A & ptr, int a);

public:
	static void print_mem() { //类的静态成员函数只能访问类的静态属性因为静态二字，是类共有的
		cout << sta << endl;
	}

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
	B(int a, int b): A(b),  objectA(a) //先初始化父类的内存 在初始化自己的内存 如果不加继承初始化列表, 那么父类A没机会调用自己的拷贝构造函数
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
	void chengefatherstaticmem() //静态变量遵循类的访问控制符
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
