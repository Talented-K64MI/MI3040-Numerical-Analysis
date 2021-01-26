#include <bits/stdc++.h>
#define  eps  1.0e-6
#define  eta  1.0e-4
#define  step 1.0e-3
#define  pi   3.14159265
#define e   2.718281828459
using namespace std;
double  a=-6,
         b=6;
int     sign, dem=0;
map    <double, double> save;
map    <double, double>::iterator k, kmax, kmin;
//----------------------------------//
double f(double x)  //Nhap ham f(x)
{
    return sin(x) + x - x*x;
}
//------------------------------------------//
double f1(double x0)  //Ham tra ve f'(x0)
{
	double dy=f(x0+eps)-f(x0-eps),
		   dx=2*eps;
	return dy/dx;

	//githello
}
//-----------------------------------------------------------------------------------------//
double gda(double x0)  //Gradient Desent Asent
{                     //Ham nay tra ve gia tri x*>x0 thoa man f'(x*)=0
                     //Cac gia tri tra ve tang dan vi x0 tang dan (i:=a->b)
    double x=x0;
    if (f1(x0)==0)  return x0;
	if (f1(x0)<0)     sign=-1;
	else              sign= 1;
	while (abs(f1(x0))>eps)
	{
	    x=x0+sign*eta*f1(x0);
		x0=x;
		if (x0>b)   return b;
		dem++;
	}
	return x;
}
//----------------------------------------------------------------------------------//
void luutru()   //Luu cac x* f(x*), a f(a), b f(b) vao map
{
	double i=a;
	save[a]=f(a),
	save[b]=f(b);
    while (i<b)
    {
        i=gda(i);
        save[i]=f(i);
        do
        {
            i+=step;
            if (i>=b) break;
        }
        while ((f1(i)*sign>0) && (abs(f1(i) > f1(i+step))));
    }
}
//--------------------------------------------------//
void xuat1()  //Xuat cac diem toi han
{
	cout<<"Cac diem toi han lan luot la: "<<endl;
	for (k=save.begin(); k!=save.end(); k++)
	{
	    printf("(%5.5f,%5.5f)\n",k->first,k->second);
	}
}
//--------------------------------------------------//
void xuat2() //Tim va xuat max min
{
    kmax=kmin=save.begin();
	for (k=save.begin(); k!=save.end(); k++)
	{
	    if (k->second > kmax->second) kmax=k;  // tim f(x) max
	    if (k->second < kmin->second) kmin=k; //  tim f(x) min
	}
	printf("Min cua f(x) trong khoang [%5.2f,%5.2f] tai: m (%5.5f,%5.5f)\n",a,b,kmin->first,kmin->second);
	printf("Max cua f(x) trong khoang [%5.2f,%5.2f] tai: M (%5.5f,%5.5f)\n",a,b,kmax->first,kmax->second);
	printf("So buoc lap cua GDA la: %d",dem);
}
//----------------------------//
int main()
{
    luutru();
	xuat1();
	xuat2();
}
