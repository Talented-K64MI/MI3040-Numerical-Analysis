#include <bits/stdc++.h>
#define NN 5000

using namespace std;
double ma[NN][NN],kq1[NN];
double f[NN],a[NN],kq[NN];
int n;
double F[NN],A[NN];
int N,dem;

void printmatrix()
{
    cout<<"Khoi tao ma tran Vandemonde:"<<endl;
    for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n+1;j++)
            printf("%.4f     ",ma[i][j]);
            printf("\n");
        }
}

void creatematrix()
{
    for(int i=1;i<=n;i++)

    {
        ma[i][1]=1;
        ma[i][n+1]=f[i];
        for(int j=2;j<=n;j++)
        {
            ma[i][j]=ma[i][j-1]*a[i];
        }
    }
}


void Solve()
{
    double b;
    for(int j=1; j<=n; j++) {
      for(int i=1; i<=n; i++) {
         if(i!=j) {
            b=ma[i][j]/ma[j][j];
            for(int k=1; k<=n+1; k++) {
               ma[i][k]=ma[i][k]-b*ma[j][k];
            }
         }
      }
   }
}

void checkdata()
{
    for(int i=1;i<=N;i++)
    {
        bool check=1;
        for(int j=1;j<i;j++)
            if (A[i]==A[j]) check=false;
        if (check)
            {
                a[++n]=A[i];
                f[n]=F[i];
            }
        else ++dem;
    }

}

void printresult()
{
    printf("He so cua da thuc noi suy:\n");
    for(int i=1;i<=n;i++)
    {
        printf("a%d.x^%d ",i,i-1);
        if (i<n) printf("+ ");
    }

    printf("\n");
    for(int i=1;i<=n;i++)
    {
        //cout<<ma[n+1][i]<<" "<<ma[i][i]<<endl;
        printf("a%d = %.4f\n",i,kq[i]=ma[i][n+1]/ma[i][i]);
    }
}

double Hoocne(double c)
{
    double p=kq[n];
    for(int i=n-1;i>=1;i--)
    {
        p=p*c+kq[i];
    }
    return p;
}
main()
{
    freopen("Solve.inp","r",stdin);
    freopen("Solve.out","w",stdout);
    /*scanf("%d",&N);
    for(int i=1;i<=N;i++)
    {
        scanf("%f%f",&A[i],&F[i]);
    }
    checkdata();
    creatematrix();*/
    cin>>m>>n;
    for(int i=1;i<=m;i++) for(int j=1;j<=n;j++) cin>>a[i][j];
    Solve();
    //printf("So moc noi suy bo di la: %d\n",dem);
    printresult();
    /*printf("Kiem tra ket qua:\n");
    for(int i=1;i<=n;i++)
        printf("x=%.4f    f[x]=%.4f\n",a[i],Hoocne(a[i]));
        */
}
