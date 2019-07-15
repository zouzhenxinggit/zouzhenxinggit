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
    printf();
  }

  ~father ()
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
    printf();
  }

  ~child () // virtual子类可省略
  {
    cout << "~child" << endl;
  }

public:
  virtual void printf()
  {
    cout << "i'm child not acc" << endl;// virtual子类可省略
  }
};

#include <stdio.h>

int main(int argc, char const *argv[])
{
  child c(10);

  cout << sizeof(c) << endl;

  return 0;
}
