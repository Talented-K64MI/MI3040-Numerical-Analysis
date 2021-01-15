#include "MyMath.h"
using namespace Hieu;
void IoFile(bool ok){
    if (ok) {
        freopen("Equation.inp","r",stdin);
        freopen("Equation.out","w",stdout);
    }
}
int main()
{
    IoFile(true);
    try{
        int n;
        double eps;
        cin>>n;
        cin>>eps;
        Matrix A(n,n),B(n,1),X0(n,1);
        for (int i=1;i<=n;++i)
        for (int j=1;j<=n;++j){
            double tam;
            cin>>tam;
            A.setVal(i,j,tam);
        }
        for (int i=1;i<=n;++i){
            double tam;
            cin>>tam;
            B.setVal(i,1,tam);
        }
        for (int i=1;i<=n;++i){
            double tam;
            cin>>tam;
            X0.setVal(i,1,tam);
        }
        Matrix X(n,1);
        Equation myequation;
        /* X=myequation.singleloop(A,B,X0,eps);
        for (int i=1;i<=X.getRow();++i) cout<<X.getVal(i,1)<<" ";
        cout<<"\n"; */
       /*  X=myequation.singleloop(A,B,X0,eps,2);
        for (int i=1;i<=X.getRow();++i) cout<<X.getVal(i,1)<<" ";
        cout<<"\n"; */
       /*  X=myequation.jacobiloop(A,B,X0,eps);
        for (int i=1;i<=X.getRow();++i) cout<<X.getVal(i,1)<<" ";
        cout<<"\n"; */
        /* X=myequation.jacobiloop(A,B,X0,eps,2);
        for (int i=1;i<=X.getRow();++i) cout<<X.getVal(i,1)<<" ";
        cout<<"\n"; */
        /*  X=myequation.gaussseidelloop(A,B,X0,eps);
        for (int i=1;i<=X.getRow();++i) cout<<X.getVal(i,1)<<" ";
        cout<<"\n"; */
       /*  X=myequation.gaussseidelloop(A,B,X0,eps,2);
        for (int i=1;i<=X.getRow();++i) cout<<X.getVal(i,1)<<" ";
        cout<<"\n"; */
    } catch (MyError e){
     cout<<e.getName();
    }
    return 0;
}
