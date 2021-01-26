#include <bits/stdc++.h>
using namespace std;
int main()
{
 int i,j,k,n,l,m,p=1;
 float A[20][20],c,x[20],sum=0.0;
//Nhap du lieu tu file  
FILE *f = fopen("D:\\Matran.txt", "rt");
   fscanf(f,"%d %d",&m,&n);
   for (i=1;i<=m;++i)
	for (j=1;j<=n+1;j++)
	 fscanf(f,"%f",&A[i][j]);
//In ra ma tran ban dau
	for (i=1;i<=m;i++)
		{for (j=1;j<=n+1;j++)
		      printf("%.4f   ",A[i][j]);
		      printf("\n");}
		      printf("\n");
		      printf("\n"); 
//Sap xep de cac vi tri tren duong cheo khac 0 
     for (i=1; i<=n+1; ++i){A[m+1][n]=0;}
     j=1;
while(j<=m) 
 {
 	if (A[j][p]==0) {k=0;
 	for(l=p;l<=n;l++){
 		for (i=j;i<=m;i++) if (abs(A[i][p])>0.000001) k=i;
 		if(k) break;
 		if (k==0) p=p+1;}
		if (k) for(i=j;i<=n+1;i++) {
		 	float temp=A[k][i];
		 	A[k][i]=A[j][i];
		 	A[j][i]=temp;
		 }
		 l=j-1;
	if(p==n+2) break;		 
	 }
//Dua ve ma tran bac thang va tra ve gia tri ma tran sau moi lan bien doi
 for(i=j+1; i<=m;++i)
 	{
 	c=A[i][j]/A[j][p];
 	for(k=1; k<=n+1; k++)
 		{
 		A[i][k]=A[i][k]-c*A[j][k];
 		}
	 }
	 j=j+1;
    for (i=1; i<=m; ++i){
        for (l=1; l<=n+1; ++l) printf("%.4f   ",A[i][l]);
        printf("\n");
    }
    printf("\n\n");
 }
 for (i=m;i>=1;i--)
 { j=0;
 	for(k=1;k<=n+1;k++) if(abs(A[i][k])<0.000001) j=j+1;
 	if (j!=(n+1)) {l=i;break;}}
 printf("%d\n",l);
 int pivot[l];j=1;
 for (i=1;i<=l;i++)
 {while(j<=n+1)
 	{if (A[i][j]!=0) {pivot[i]=j;break;}
 	else j=j+1;}
 	}
for (i=1;i<=l;i++)
printf("%d ",pivot[i]);printf("\n");
 if(pivot[l]==n+1) {printf("\nNo Solution!");exit(0);};
 if(pivot[l]!=n+1&&l!=n)
 {
 	 printf("\nThe solution is: \n");
 	for(i=l;i>=1;i--)
 		{
		 for(j=i+1;j<=l;j++)
 		{c=A[i][pivot[j]]/A[j][pivot[j]];
 		for(p=pivot[j];p<=n+1;p++)
 			A[i][p]=A[i][p]-A[j][p]*c;}
 		printf("x_%d=%.4f",pivot[i],A[i][n+1]/A[i][pivot[i]]);
 		for(j=pivot[i]+1;j<=n;j++)
 		{c=0;
		 for(p=pivot[i]+1;p<=pivot[l];p++)
 			{
 				if(j==pivot[p]) c=c+1;
			 }
		if (c==0&&A[i][j]!=0) printf("+%.4f t_%d",-A[i][j]/A[i][pivot[i]],j);
			}
		printf("\n");}
		for(j=1;j<=n;j++)
 		{c=0;
		 for(p=pivot[1];p<=pivot[l];p++)
 			{
 				if(j==pivot[p]) c=c+1;
			 }
		if (c==0) printf("x_%d=t_%d\n",j,j);}
		exit(0);}
 if (A[n][n]!=0) {
 x[n]=A[n][n+1]/A[n][n];
 for(i=n-1; i>=1; i--)
 {
 sum=0;
 for(j=i+1; j<=n; j++)
 {
 sum= sum + A[i][j]*x[j];
 }
 x[i]=(A[i][n+1] - sum)/A[i][i];
 }
 printf("\nThe solution is: \n");
 for(i=1; i<=n; i++)
 {
 printf("\nx%d=%f\t",i,x[i]); 
 }}
 return(0);
}
