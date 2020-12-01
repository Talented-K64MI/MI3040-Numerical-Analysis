#include <vector>
#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;
namespace Hieu
{
    class MyError{
        private :
            string name;
            int errorId;
        public :
            MyError(const int &errorId, const string &name){
                this->errorId = errorId;
                switch (errorId) {
                case 101:
                    this->name = name + ": Error not square matrix";
                    break;
                case 102:
                    this->name = name + ": Error matrix did not have the right size";
                    break;
                case 103:
                    this->name = name + ": Error invalid column or row";
                    break;
                case 104:
                    this->name = name + ": Error not vector";
                    break;
                case 105:
                    this->name = name + ": Error negative epsilon";
                    break;
                case 106:
                    this->name = name + ": Error matrix have norm greater than one";
                    break;
                default:
                    this->name = name + ": Error";
                    break;
                }
            }
            int getErrorId(){
                return this->errorId;
            }
            string getName(){
                return this->name;
            }
    };
    class Matrix{
        protected :
            int row,col;
            vector <vector <double > > table;
            void createMatrix(){
                this->table.resize(this->row+2);
                for (int i=0;i<this->table.size();++i){
                    this->table[i].resize(this->col+2);
                }
                for (int i=1;i<=this->row;++i){
                    for (int j=1;j<=this->col;++j){
                        this->table[i][j]=0.0;
                    }
                }
            }
        public :
            Matrix(const int &row,const int &col) throw(MyError){
                if (row>=1 && col>=1){
                    this->row = row;
                    this->col = col;
                    this->createMatrix();
                } else throw MyError(103,"Matrix");
            }
            Matrix(const int &degree) throw(MyError){
                if (degree>=1){
                    this->row = degree;
                    this->col = degree;
                    this->createMatrix();
                    for (int i=1;i<=this->row;++i){
                        this->table[i][i]=1.0;
                    }
                } else throw MyError(103,"Matrix");
            }
            void setVal(const int &row,const int &col,const double &val) throw(MyError){
                if (row>=1 && row<=this->row && col>=1 && col<=this->col){
                    this->table[row][col]=val;
                }
                else throw MyError(103,"setVal");
            }
            int getRow() throw(MyError){
                return this->row;
            }
            int getCol() throw(MyError){
                return this->col;
            }
            double getVal(const int &row,const int &col) throw(MyError){
                if (row>=1 && row<=this->row && col>=1 && col<=this->col){
                    return this->table[row][col];
                } else throw MyError(103,"getVal");
            }
            double getNorm(const int &normType) throw(MyError){
                double norm1;
                double norm2;
                switch (normType){
                case 1:
                    norm1=0.0;
                    norm2=0.0;
                    for (int i=1;i<=this->row;++i){
                        for (int j=1;j<=this->col;++j){
                            norm1=norm1+fabs(this->table[i][j]);
                        }
                        norm2=max(norm2,norm1);
                        norm1=0.0;
                    }
                    return norm2;
                case 2:
                    norm1=0.0;
                    norm2=0.0;
                    for (int i=1;i<=this->col;++i){
                        for (int j=1;j<=this->row;++j){
                            norm1=norm1+fabs(this->table[j][i]);
                        }
                        norm2=max(norm2,norm1);
                        norm1=0.0;
                    }
                    return norm2;
                case 3:
                    norm1=0.0;
                    norm2=0.0;
                    for (int i=1;i<=this->row;++i){
                        for (int j=1;j<=this->col;++j){
                            norm1=norm1+this->table[i][j]*this->table[i][j];
                        }
                    }
                    norm2=sqrt(norm1);
                    return norm2;
                default:
                    return -1.0;
                    break;
                }
            }
            void toRound(double eps) throw(MyError){
                if (eps<0.0) throw MyError(105,"toRound");
                double eps1=-floor(log10(eps));
                eps1=pow(10,eps1);
                for (int i=1;i<=this->row;++i)
                for (int j=1;j<=this->col;++j)
                {
                    double tam=this->table[i][j];
                    tam=tam*eps1;
                    tam=round(tam);
                    tam=tam/eps1;
                    this->table[i][j]=tam;
                }
            }
            int calDig() throw(MyError){
                if (this->row == this->col){
                    double a=0.0;
                    bool ok=false;
                    for (int i=1;i<=this->row;++i)
                    {
                        a=fabs(this->table[i][i]);
                        for (int j=1;j<=this->col;++j){
                            if (i==j) continue;
                            a=a-fabs(this->table[i][j]);
                            if (a<=0.0) {ok=true;break;}
                        }
                        if (a<=0.0) {ok=true;break;}
                    }
                    if (!ok) return 1;
                    ok=false;
                    for (int i=1;i<=this->col;++i)
                    {
                        a=fabs(this->table[i][i]);
                        for (int j=1;j<=this->row;++j){
                            if (i==j) continue;
                            a=a-fabs(table[j][i]);
                            if (a<=0.0) {ok=true;break;}
                        }
                        if (a<=0.0) {ok=true;break;}
                    }
                    if (!ok) return 2;
                    return 0;
                } else throw MyError(101,"calDig");
            }
            Matrix operator+(Matrix& b) throw(MyError) {
                if (this->getCol() == b.getCol() && this->getRow() == b.getRow()){
                    Matrix matrix(this->row,this->col);
                    for (int i=1;i<=this->row;++i){
                        for (int j=1;j<=this->col;++j){
                            matrix.setVal(i,j,this->table[i][j] + b.getVal(i,j));
                        }
                    }
                    return matrix;
                } else throw MyError(101,"+");
            }
            Matrix operator-(Matrix& b) throw(MyError) {
                if (this->getCol() == b.getCol() && this->getRow() == b.getRow()){
                    Matrix matrix(this->row,this->col);
                    for (int i=1;i<=this->row;++i){
                        for (int j=1;j<=this->col;++j){
                            matrix.setVal(i,j,this->table[i][j] - b.getVal(i,j));
                        }
                    }
                    return matrix;
                } else throw MyError(101,"-");
            }
            Matrix operator*(Matrix& b) throw(MyError) {
                if (this->getCol() == b.getRow()){
                    Matrix matrix(this->row,b.getCol());
                    for (int i=1;i<=this->row;++i){
                        for (int j=1;j<=b.getCol();++j){
                            double tam=0.0;
                            for (int k=1;k<=this->col;++k) tam = tam + (this->table[i][k] * b.getVal(k,j));
                            matrix.setVal(i,j,tam);
                        }
                    }
                    return matrix;
                } else throw MyError(101,"*");
            }
            void operator=(Matrix b) throw(MyError) {
                if (this->getCol() == b.getCol() && this->getRow() == b.getRow()){
                    for (int i=1;i<=this->row;++i){
                        for (int j=1;j<=this->col;++j){
                            this->setVal(i,j,b.getVal(i,j));
                        }
                    }
                } else throw MyError(101,"=");
            }
    };
    class Equation{
        public :
            Matrix jacobi(Matrix& A,Matrix& B,Matrix& X0,double& eps,int type = 1) throw (MyError){
                if (A.getCol() != A.getRow()) throw MyError(101,"jacobi");
                if (B.getCol() != 1) throw MyError(104,"jacobi");
                if (X0.getCol() != 1) throw MyError(104,"jacobi");
                if (A.getRow() != B.getRow() || A.getRow() != X0.getRow()) throw MyError(102,"jacobi");
                if (eps < 0.0 ) throw MyError(105,"jacobi");
                int normType = 0;
                for (int i=3;i>=1;--i){
                    if (A.getNorm(i)<1.0) normType = i;
                }
                if (normType == 0) throw MyError(106,"jacobi");
                double q=A.getNorm(normType);
                double eps1=floor(log10(eps));
                eps1=pow(10,eps1)*0.5;
                double eps2=eps-eps1;
                switch (type){
                case 1:
                    {Matrix X(A.getCol(),1);
                    Matrix X1(A.getCol(),1);
                    double w=q/(1-q);
                    X=X0;
                    int loopNumber=0;
                    do {
                        ++loopNumber;
                        X1=X;
                        X=(A*X1)+B;
                    }while (w*(X-X1).getNorm(normType)>eps2);
                    std::cerr<<type<<" "<<normType<<" "<<q<<" "<<loopNumber<<"\n";
                    X.toRound(eps);
                    return X;
                    break;}
                case 2:
                    {
                    Matrix X(A.getCol(),1);
                    Matrix X1(A.getCol(),1);
                    X=X0;
                    X1=(A*X)+B;
                    int loopNumber=ceil((log((eps2*(1-q))/((X-X1).getNorm(normType))))/(log(q)));
                    for (int i=1;i<=loopNumber;++i){
                        X=(A*X)+B;
                    }
                    std::cerr<<type<<" "<<normType<<" "<<q<<" "<<loopNumber<<"\n";
                    X.toRound(eps);
                    return X;
                    break;
                    }
                }
            }
    };

}
