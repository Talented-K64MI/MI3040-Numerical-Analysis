#include "MyMath.h"
using namespace Hieu;
int main()
{
    Matrix a(2,2);
    Matrix b(2,2);
    a.setVal(1,1,3);
    a.setVal(2,1,5);
    b.setVal(1,1,4);
    b.setVal(2,2,1);
    Matrix c(2,2);
    c=a+b;
    std::cout<<c.getVal(1,1);
    return 0;
}
