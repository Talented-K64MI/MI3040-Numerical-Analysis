#include <bits/stdc++.h>
#define  delta  1.0e-6
#define  eps  1.0e-5
double epsilon=1.0e-9;
using namespace std;
double a,b,xo,q;
//-----------------------------------------------------------------------------------------------------------------------------------------------------------//
double g(double x) // nhap ham g(x)
{
	double mu=(double) 1/3;
	double t=3*x+2;
	if (t<0) return -exp((log(-t)*mu));
	else
		return exp((log(t)*mu));
}
//-----------------------------------------------------------------------------------------------------------------------------------------------------------//
double abs_g_phay(double x) // khoi tao ham |g'(x)|
{
	double dy=g(x+delta)-g(x-delta),dx=2*delta;
	return fabs(dy/dx);
}
//-----------------------------------------------------------------------------------------------------------------------------------------------------------//
double max_abs_g_phay(double a, double b) // khoi tao ham tim q = max|g'(x)| tren [a,b]
{
	double max=abs_g_phay(a),i=a+eps;
	do
	{
		if (abs_g_phay(i) > max) max=abs_g_phay(i);
		i+=eps;
	}
	while (i<=b);
	return max;
}
//-----------------------------------------------------------------------------------------------------------------------------------------------------------//
int kiemtra(double a,double b,double xo) // check input
{
	if (a>=b) printf("Dau vao khong hop le! Yeu cau can duoi < can tren (a<b)\n");
	else if ((xo<a)||(xo>b)) printf ("Xo nam ngoai [a,b]. Yeu cau nhap lai\n");
		 else return 0;
	printf("Nhap lai can duoi a=");scanf("%lf",&a);
	printf("Nhap lai can tren b=");scanf("%lf",&b);
	printf("Nhap lai xap xi dau xo=");scanf("%lf",&xo);
	kiemtra(a,b,xo);
}
//-----------------------------------------------------------------------------------------------------------------------------------------------------------//
double lapdontiennghiem(double xo, double q,double epsilon)
{
	double x=g(xo);
	if (x==xo) printf("Tinh theo cong thuc sai so tien nghiem, nghiem cua phuong trinh chinh la xo= %.15lf\n",xo);
	else 
	{
		int i,n;
		epsilon*=(1-q);
		double step=ceil(log(fabs(epsilon/(x-xo)))/log(q));
		n=(int) step;
		printf("Theo cong thuc sai so tien nghiem-----------------------------------------------------------------\n");
		printf("X1= %.15lf\n",x);
		for (i=2;i<=n;i++)
		{
			x=g(x);
			printf("X%d= %.15lf\n",i,x);
		}
		printf("So lan lap : %d\n",n);
		printf("Nghiem gan dung X= %.15lf\n",x);
	}	
}
//-----------------------------------------------------------------------------------------------------------------------------------------------------------//
double lapdonhaunghiem(double xo,double q,double epsilon)
{
	double x=g(xo);
	if (x==xo) printf("Tinh theo cong thuc sai so hau nghiem, nghiem cua phuong trinh chinh la xo= %.15lf\n",xo);
	else 
	{
		int step=1;
		double del=fabs(x-xo);
		epsilon=epsilon*(1-q)/q;
		printf("Theo cong thuc sai so hau nghiem-----------------------------------------------------------------\n");
		printf("X1= %.15lf\n",x);
		while (del > epsilon)
		{
			xo=x;
			x=g(x);
			del=fabs(x-xo);
			step+=1;
			printf("X%d= %.15lf\n",step,x);
		}
		printf("So lan lap : %d\n",step);
		printf("Nghiem gan dung X= %.15lf",x);
	}
}
//-----------------------------------------------------------------------------------------------------------------------------------------------------------//
int dieu_kien_co(double q) // kiem tra dieu kien co 
{
	if ((q<=0)||(q>=1)) 
	{
		printf("Ham g(x) khong thoa man dieu kien anh xa co\n");
		printf("Ban co muon chuong trinh van chay hay khong?\n");
		printf("Neu co hay go 1\n");
		printf("Luu y! Chuong trinh co the van ra ket qua hoac khong vi dieu kien co chi la dieu kien du\n");
		printf("Luc nay, qua trinh lap co hoi tu hay khong phu thuoc rat lon vao xap xi dau Xo ma ta chon\n");
		int k;scanf("%d",&k);
		if (k==1) {
				lapdontiennghiem(xo,q,epsilon);
				lapdonhaunghiem(xo,q,epsilon);
		      	}
	else return 0;
	}
	else 
	{
		printf("Ham g(x) thoa man dieu kien co\n");
		lapdontiennghiem(xo,q,epsilon);
		lapdonhaunghiem(xo,q,epsilon);
	}
}
//-----------------------------------------------------------------------------------------------------------------------------------------------------------//
int main()
{
	printf("Nhap can duoi a=");scanf("%lf",&a);
	printf("Nhap can tren b=");scanf("%lf",&b);
	printf("Nhap xap xi dau Xo=");scanf("%lf",&xo);
	kiemtra(a,b,xo);
	q=max_abs_g_phay(a,b);
	dieu_kien_co(q);
}


