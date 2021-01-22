#include <bits/stdc++.h>
#define  step 1.0e-5
#define  pi   3.14159265
#define e   2.718281828459
using namespace std;
//--------------------------//
int dem=0;
double f( double x)
{
    return sin(x) + x - x*x;
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
        dem++;
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
    printf("So lan duyet: %d",dem);
}
