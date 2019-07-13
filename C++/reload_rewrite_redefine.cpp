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
  void printf()
  {
    cout << "i'm father, not acc" << endl;
  }

  void printf(int x, int y, int z)
  {
    cout << "i'm father, there acc" << endl;
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
  void printf()
  {
    cout << "i'm child not acc" << endl;
  }

  void printf(int x)
  {
    cout << "i'm child one acc" << endl;
  }

  void printf(char x)
  {
    cout << "i'm child one acc" << endl;
  }


  void printf(int x, int y)
  {
    cout << "i'm child two acc" << endl;
  }
};


int main(int argc, char const *argv[]) {
  /* code */
  father f(6);
  child c(10);

  // 重载，发生在同一函数内
  c.printf();
  c.printf(1);
  c.printf('a');
  c.printf(1, 2);

  //需函数重写引发多态
  // 以后说

  cout << c.father::a << endl;
  cout << c.child::a << endl;

  // 重定义，子类"屏蔽"父类同名成员
  c.a = 7;
  c.printf();
  c.father::printf();

  cout << c.father::a << endl;
  cout << c.child::a << endl;
  // c.printf(1, 2, 3); 被屏蔽，无法调用用域作用符号


  // 父类指针 优先调用父类成员
  // 子类指针 优先调用子类成员
  // 不只是指针，引用也是
  // 这就是指针作用域的问题

  father *p = NULL;
  p = &f;
  p->printf();

  p = &c;
  p->printf();

  child *pc = &c;
  pc->father::printf();
  pc->printf();


  return 0;
}
