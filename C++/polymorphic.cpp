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

  virtual ~father ()
  {
    cout << "~father" << endl;
  }

public:
  virtual void printf()
  {
    cout << "i'm father, not acc" << endl;
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

  virtual ~child () // virtual子类可省略
  {
    cout << "~child" << endl;
  }

public:
  virtual void printf()
  {
    cout << "i'm child not acc" << endl;// virtual子类可省略
  }
};

void stage(father* &p)
{
  delete p;
  while (1) {
    /* code */
  }
}

int main(int argc, char const *argv[]) {

  // 1.继承
  // 2.需函数重写(参数个数，类型相同)
  // 3.父类指针或引用指向父类对象或子类对象 会有不同的调用方式

  /* code */
  father f(6);
  child c(10);

  father *pf = &f;
  pf->printf();

  father *pc = &c;
  pc->printf();

  // 虚析构函数
  father *nf = new child(10);
  stage(nf);
  return 0;
}
