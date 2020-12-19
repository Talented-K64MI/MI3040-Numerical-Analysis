#include <bits/stdc++.h>
#define  eps 1.0e-6
#define  eta 1.0e-5
#define  max 1.0e6
#define  pi  3.14159265

#include<stdio.h>
#include<math.h>

using namespace std;
double  a1,
		b1,
		step=0.00001,
		diem[100];
double N1, N2;
int     sign,m;
double f(double x)  //Nhap ham f(x)
{
	return pow(x,4)-4*pow(x,3)+1;
}
//------------------------------------------//
double f1(double x0)  //Ham tra ve f'(x0)
{
	double dy=f(x0+eps)-f(x0-eps),
		   dx=2*eps;
	return dy/dx;
}
//--------------------------------------------------------//
double fixeta(double x0)  //Ham tra ve eta hop li
{
    double etaa=eta;
    while ((f1(x0)*f1(x0+sign*etaa*f1(x0)))>=0) etaa*=2;
    while ((f1(x0)*f1(x0+sign*etaa*f1(x0)))<=0) etaa/=2;
    return etaa;

}
//-----------------------------------------------------------//
double gda(double x0)  //Gradient Desent Asent
{                     //Ham nay tra ve gia tri x*>x0 thoa man f'(x*)=0
	double x=x0;     //Cac gia tri tra ve tang dan vi x0 tang dan (i:=a->b)
	if (f1(x)==0)    return x;
	if (f1(x)<0)     sign=-1;
	else             sign= 1;
	while (abs(f1(x0))>eps)
	{
		x=x0+sign*eta*f1(x0);
		x0=x;
		if (x0>b1)   return b1;
	}
	diem[m]=x;m++;
	return x;
}
//Bubblesort
double bubblesort(double a[100], int n) {
	int i,j;
	bool haveswap=false;
	for(i=0;i<n-1;i++) {
		haveswap=false;
		for(j=0;j<n-i-1;j++) {
			if(a[j]>a[j+1]) {
				double temp=a[j];
				a[j]=a[j+1];
				a[j+1]=temp;
				haveswap=true;
			}
		}
		if(haveswap==false) {break;}
	}
	return a[100];
}

//Chuong trinh con de tinh can bac n cua so a
double canbac(double a, int n)
{
    double f;
    f=exp((1.0 / n) * log(a));
    return f;
}
//Tinh gia tri f(x) tai mot diem bang hoocne
double f(int n,double a[100], double x) {
	double b[100];
	int i;
	b[0]=a[0];
	for(i=1;i<=n;i++) b[i]=a[i]+b[i-1]*x;
	return b[n];
}
//Tim mien chua nghiem thuc
	//Tim can tren cua nghiem thuc (N1)
double timmiennghiem(int n,double a[100]) {
	int i,A,B1,B2,k1,k2,count1=0,count2=0;
	for(i=1;i<=n;i++) if(a[i]<0) {
		k1=i;
		break;
		}
	for(i=1;i<=n;i++) if(a[i]<0) count1++;
	for(i=1;i<=n;i++) {
		if(a[i]<0) B1=a[i];
		for(i=1;i<=n;i++)
		if(a[i]<0) if(-a[i]>-B1) B1=a[i];
	}
	N1=1+canbac((double)((-B1)/a[0]),k1);

	//Tim can duoi cua nghiem thuc (N2)
	for(i=0;i<=n;i++) if((i%2)==1) a[i]=-a[i];
	for(i=1;i<=n;i++) if(a[i]<0) {
		k2=i;
		break;
		}
	for(i=1;i<=n;i++) if(a[i]<0) count2++;
	for(i=1;i<=n;i++) {
		if(a[i]<0) B2=a[i];
		for(i=1;i<=n;i++)
		if(a[i]<0) if(-a[i]>-B2) B2=a[i];
	}
	N2=1+canbac((double)((-B2)/a[0]),k2);
	if(count1==0) N1=0;
	else if(count2==0) N2=0;
	printf("\nKhoang chua nghiem cua phuong trinh la (%f,%f)\n",-N2,N1);
	for(i=0;i<=n;i++) if((i%2)==1) a[i]=-a[i];
	a1=-N2;
	b1=N1;
	return -N2,N1;

}
//Nhap da thuc pn(x)
int main() {
	int n,j;
	double a[100];
	printf("Nhap bac cua da thuc: "); scanf("%d",&n);
	printf("Nhap cac he so: ");
	for(j=0;j<=n;j++) scanf("%lf",&a[j]);
	timmiennghiem(n,a);
//Tim diem cuc tri
	//--------------------------------------------------//
	map <double, double> save;
	map <double, double>::iterator k, kmin, kmax;
	double i=a1;
	//--------------------------//
	save[f(a1)]=a1,
	save[f(b1)]=b1;
    //--------------------------//
    while (i<b1)
    {
        i=gda(i);
        save[f(i)]=i;
        i+=step;
    }

    diem[m]=-N2;
    diem[m+1]=N1;
    bubblesort(diem,m+1);
    for(int p=0;p<=m+1;p++) printf("\n%lf",diem[p]);
	return 0;
	}
