#include <bits/stdc++.h>

using namespace std;
float a[50000];
int n;float x;int type;
float b[50000];

float C[50000];

float solve(float c)
{
    b[n]=a[n];
    for(int i=n-1;i>=1;i--)
    {
        b[i]=b[i+1]*c + a[i];
    }
    return b[1];
}

void chia(float c)
{
    b[n]=a[n];
    for(int i=n-1;i>=1;i--)
    {
        b[i]=b[i+1]*c+a[i];
    }
    printf("(");
    for(int i=n;i>=2;i--)
    {
        printf("b%dx^%d ",i-1,i-2);
        if (i>2) printf("+ ");
    }
    printf(")\n");
    for(int i=n;i>=2;i--)
    {
        printf("b%d=%f\n",i-1,b[i]);
    }
    printf("Phan du :%.4f",b[1]);
}

void nhan(float c)
{
    b[n]=a[n];
    b[0]=a[1]*(-c);
    for(int i=n-1;i>=1;i--)
    {
        b[i]=a[i+1]*(-c)+a[i];
    }

    printf("(");
    for(int i=n;i>=0;i--)
    {
        printf("b%dx^%d ",i+1,i);
        if (i>0) printf("+ ");
    }
    printf(")\n");
    for(int i=n;i>=0;i--)
    {
        printf("b%d=%f\n",i+1,b[i]);
    }
}





float daoham(float c)
{
    b[n]=a[n];
    for(int i=n-1;i>=1;i--)
    {
        b[i]=b[i+1]*c+a[i];
    }
    C[n]=b[n];
    for(int i=n-1;i>=2;i--)
    {
        C[i]=C[i+1]*c+b[i];
    }
    return C[2];
}
main()
{
    freopen("HOOCNE.inp","r",stdin);
    freopen("HOOCNE.out","w",stdout);
    cin>>n;
    n++;
    for(int i=n;i>=1;i--) cin>>a[i];
    cin>>x>>type;
    printf("Da thuc da cho:\n");
    for(int i=n;i>=1;i--)
    {

        printf("a%d.x^%d ",i,i-1);
        if (i>1) printf("+ ");
    }
    printf("\n");
    for(int i=n;i>=1;i--)
        printf("a%d = %.4f\n",i,a[i]);
    printf("\n\n");
    //solve();
    if (type==1) printf("Gia tri cua da thuc tai diem : x=%.4f la: %.4f",x,solve(x));
    if (type==2)
    {
        printf ("Da thuc thuong khi chia cho (x-c) voi c=%.4f la:\n",x);
        chia(x);
    }
    if (type==3)
    {
        printf ("Da thuc khi nhan voi (x-c) voi c=%.4f la:\n",x);
        nhan(x);
    }
    if (type==4) printf("Gia tri cua dao ham tai diem : x=%.4f la: %.4f",x,daoham(x));

}
