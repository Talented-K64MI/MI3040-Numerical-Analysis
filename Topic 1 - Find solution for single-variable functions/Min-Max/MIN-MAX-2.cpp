#include <bits/stdc++.h>
#define  step 1.0e-5
using namespace std;
//--------------------------//
double f( double x)
{
    return  pow(x,4)+3*pow(x,3)-11*x*x-3*x+10;
}
//-----------------------------------------------//
double x( double a, double b, string s)
{
    double i, xmax, xmin;
    xmax=a; xmin=a; i=a;
    do
    {
        if (f(i) < f(xmin))
            {
                xmin=i;
            }
        if (f(i) > f(xmax))
            {
                xmax=i;
            }
        i+=step;
    }
    while (i<=b);

    if    (s=="max") return xmax;
    else             return xmin;
}
//-----------------------------------------------//
double fx( double a, double b, string s)
{
    double i, fxmax, fxmin;
    fxmax=f(a); fxmin=f(a); i=a;
    do
    {
        if (f(i) < fxmin)
            {
                fxmin=f(i);
            }
        if (f(i) > fxmax)
            {
                fxmax=f(i);
            }
        i+=step;
    }
    while (i<=b);

    if    (s=="max") return fxmax;
    else             return fxmin;
}
//----------------------------------------------//
int main()
{
    double a=-5, b=5;
    printf("Min cua f(x) trong khoang [%3.2f,%2.2f] tai: (%2.5f, %2.5f)\n",a,b,x(a,b,"min"),fx(a,b,"min"));
    printf("Max cua f(x) trong khoang [%3.2f,%2.2f] tai: (%2.5f, %2.5f)\n",a,b,x(a,b,"max"),fx(a,b,"max"));

}
