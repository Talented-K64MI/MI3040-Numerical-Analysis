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
                case 102:
                    this->name = name + ": Error matrix did not have the right size";
                    break;
                case 103:
                    this->name = name + ": Error invalid column or row";
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
                    for (int i=1;i<=col;++i){
                        for (int j=1;j<=row;++j){
                            norm1=norm1+fabs(table[j][i]);
                        }
                        norm2=max(norm2,norm1);
                        norm1=0.0;
                    }
                    return norm2;
                case 3:
                    norm1=0.0;
                    norm2=0.0;
                    for (int i=1;i<=row;++i){
                        for (int j=1;j<=col;++j){
                            norm1=norm1+table[i][j]*table[i][j];
                        }
                    }
                    norm2=sqrt(norm1);
                    return norm2;
                default:
                    return -1.0;
                    break;
                }
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
}
