#include <bits/stdc++.h>
#define  eps 1.0e-6
#define  eta 1.0e-4
#define  max 1.0e6
#define  pi  3.14159265222222

#include<stdio.h>
#include<math.h>

using namespace std;
int 	n;
double 	a[100];
double  a1,
		b1,
		step=0.01,
		diem[100];
double N1, N2;
int     sign,m;
double ff(double x)  //Nhap ham f(x)
{
	return x*x*x+3*x*x+3*x+1;
}
//------------------------------------------//
double f1(double x0)  //Ham tra ve f'(x0)
{
	double dy=ff(x0+eps)-ff(x0-eps),
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
double bubblesort(double b[100], int aa) {
	int i,j;
	bool haveswap=false;
	for(i=0;i<aa-1;i++) {
		haveswap=false;
		for(j=0;j<aa-i-1;j++) {
			if(b[j]>b[j+1]) {
				double temp=b[j];
				b[j]=b[j+1];
				b[j+1]=temp;
				haveswap=true;
			}
		}
		if(haveswap==false) {break;}
	}
	return b[100];
}

//Chuong trinh con de tinh can bac n1 cua so a
double canbac(double a, int n1)
{
    double f;
    f=exp((1.0 / n1) * log(a));
    return f;
}
//Tinh gia tri f(x) tai mot diem bang hoocne
double f(double x) {
	double b[100];
	int i;
	b[0]=a[0];
	for(i=1;i<=n;i++) b[i]=a[i]+b[i-1]*x;
	return b[n];
}
//Tim mien chua nghiem thuc
	//Tim can tren cua nghiem thuc (N1)
double timmiennghiem() {
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
	if(count2==0) N2=0;
	printf("\nKhoang chua nghiem cua phuong trinh la (%f,%f)\n",-N2,N1);
	for(i=0;i<=n;i++) if((i%2)==1) a[i]=-a[i];
	a1=-N2;
	b1=N1; 
	return -N2,N1;
	
}
//Thuat toan chia doi
double bisection(double a, double b) {
	double c=(a+b)/2;
	if(f(c)==0||fabs(f(c))<eps) printf("\n%lf",c);
	else {
		if(f(c)*f(a)<0) b=c;
		else a=c;
		bisection(a,b);
	}
	return c;
}
//Nhap da thuc pn(x)
int main() {
	int j;
	printf("Nhap bac cua da thuc: "); scanf("%d",&n);
	printf("Nhap cac he so: ");
	for(j=0;j<=n;j++) scanf("%lf",&a[j]);
	timmiennghiem();
//Tim diem cuc tri 
	//--------------------------------------------------//
	map <double, double> save;
	map <double, double>::iterator k, kmin, kmax;
	double i=a1;
	//--------------------------//
	save[ff(a1)]=a1,
	save[ff(b1)]=b1;
    //--------------------------//
    while (i<b1)
    {
        i=gda(i);
        save[ff(i)]=i;
        i+=step;
    }
    
    diem[m]=-N2;
    diem[m+1]=N1;
    bubblesort(diem,m+1);
    for(int p=0;p<=m;p++) {
		if(f(diem[p])==0||fabs(f(diem[p]))<eps) {printf("\n%lf",diem[p]); p++;}
		if(f(diem[p])*f(diem[p+1])<0) 
			{
			bisection(diem[p],diem[p+1]);
			p++;
			}
	}
	return 0;
}

