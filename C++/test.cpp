#include <iostream>

using namespace std;

// class A
// {
// public:
// 	A(){}
// 	A(int a)
// 	{
// 		this->a = a;
// 		cout << "A" << this->a << endl;
// 	}

// 	A(const A &  a) 
// 	{
// 		this->a = a.get_a();
// 		cout << "copy A" << this->a << endl;
// 	}
// 	~A()
// 	{
// 		cout << "~A" << this->a << endl;
// 	}
// 	int get_a() const
// 	{
// 		return this->a;
// 	}
// private:
// 	int a;
// protected:
// };


// A fun(){
// // int * const fun() { 自动+＆  用的时候自动+＊
// 	A a(65);
// 	return a;
// }

// void fun1(A a)
// {

// }


// // A5
// // A65
// // ~A65
// // ~A65

// int main(int argc, char const *argv[])
// {
	
// 	A a = fun();

// 	// cout <<  "55555555555555555555" <<endl;
// 	// a = u;
	
// 	return 0;
// }



#include <iostream>

using namespace std;

class A
{
public:
	A() {
	}

	A(int a) {
		this->a = a;
		cout << "A" << endl;
	}

	A(const A &a) {
		this->a = a.a;
		cout << "copy is run" << endl;
	}

	~A() {
		cout << "~A" << endl;
	}

	int & get_value() {
		return this->a;
	}
	
public:
	int a;
};


A fun()
{
	A a(20);
	return a; 	//这里调用a的拷贝构造函数创建匿名对象  在析构函数掉a 因为a的生命周期没了
}


int main(int argc, char const *argv[])
{
	a(10);

	while(1);
	return 0;
}
