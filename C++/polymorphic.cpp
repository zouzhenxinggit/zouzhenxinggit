#include <iostream>

using namespace std;

class father
{
public:
  /* data */
  int a;

public:
  father (int a)
  {
    this->a = a;
  }

  ~father ()
  {

  }

public:
  void printf(/* arguments */)
  {
    cout << "i'm father" << endl;
  }
};


class child : public father
{
public:
  int a;

public:
  child (int a) : father (a / 2)
  {
    this->a = a;
  }

  ~child ()
  {

  }

public:
  void printf(/* arguments */)
  {
    cout << "i'm child" << endl;
  }
};


int main(int argc, char const *argv[]) {
  /* code */
  father f(6);
  child c(10);

  cout << c.father::a << endl;
  cout << c.child::a << endl;

  c.a = 7;
  c.printf();
  c.father::printf();

  cout << c.father::a << endl;
  cout << c.child::a << endl;

// 说明了没有多态，父类指针指向子类对象的父类部分
  father *p = NULL;
  p = &f;
  p->printf();

  p = &c;
  p->printf();

// 子类对象是一种特殊的父类
// 父类可不是特殊的子类
// 没有虚函数，父类指针和父类引用只指向子类的父类部分
// 没有虚函数，子类指针和父类引用只指向子类的子类部分

  child *pc = NULL;
  pc = &c;
  cout << sizeof(*pc) << endl;
  pc.printf();

// 父类引用父类，子类对象
// 只能引用自己类型的内存
  father &p1 = f;
  p1.printf();

  father &p2 = c;
  p2.printf();

  child &p3 = c;
  p3.printf();

  return 0;
}
