#include <iostream>

using namespace std;

class A
{
public:
	A(int a)
	{
		this->a = a;
		cout << "A" << endl;
	}
	~A()
	{
		cout << "~A" << endl;
	}
	int get_a()
	{
		return this->a;
	}
private:
	int a;
protected:
};


//先执行 被组合对象的构造函数
//析构函数的调用顺序与构造相反 类似栈
class B
{
public:
	B(int a, int m, int n) : a2(m), a1(n), c(n)	//跟定义顺序有关，与书写位置无关
	{
		this->a = a;
		cout << "B" << endl;
	}
	~B()
	{
		cout << "~B" << endl;
	}
	int get_a()
	{
		return this->a;
	}
	int get_A_a1_a()
	{
		return (this->a1).get_a();
	}
	int get_A_a2_a()
	{
		return (this->a2).get_a();
	}
	int get_c() const
	{
		return this->c;
	}
protected:
private:
	int a;
	int b;
	A a1;		//定义之后 没有机会调用类A的有参构造函数 (拿来的参数啊,A无参构造是可以通过的)
	A a2;
	const int c;
};



int main(int argc, char const *argv[])
{
	B b(10, 2, 4);

	cout << b.get_a() <<endl;
	cout << b.get_A_a1_a() <<endl;
	cout << b.get_A_a2_a() <<endl;

	cout << b. get_c() << endl;
	return 0;
}