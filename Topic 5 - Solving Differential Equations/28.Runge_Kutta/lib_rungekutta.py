from sympy import *
from math import *
import sys


class rungekutta_oop:
#{
    def __init__(self, expr, x_0, y_0, h, n, s):
    #{
        x          = symbols("x")
        y          = symbols("y")
        func       = sympify(expr)


        self.y_0   = y_0           # Giá trị ban đầu của x
        self.x_0   = x_0           # Giá trị ban đầu của y
        self.h     = h             # Giá trị h - khoảng cách giữa 2 điểm
        self.n     = n             # Số mốc cần đưa ra
        self.s     = s             # Số nấc s của phương pháp


        self.f     = lambdify((x,y), func, "math");
        self.sym_f = func;


        self.alpha = [0];
        self.beta  = [0];
        self.r     = [0];
    #}

    def __computeNext(self, prev):
    #{
        s     = 3 if(self.s == "heun" or self.s == "Heun") else self.s; 
        f     = self.f;
        h     = self.h;
        r     = self.r;
        alpha = self.alpha;
        beta  = self.beta;

        x   = prev[0]; 
        y   = prev[1]; 
        k   = [0];
        ret = y;

        for i in range(1, s+1):
        #{
            temp_x = x + alpha[i] * h;
            temp_y = y;

            for j in range(1, i):
            #{
                temp_y += beta[i-1][j] * k[j];
            #}
            
            k.append(h * f(temp_x, temp_y));
            ret  += r[i] * k[i];
        #}

        return ret;
    #}
    def __loadCoeff(self, s):
    #{
        if(s == 1):
        #{
            self.r     = [0, 1];
            self.alpha = [0, 0];
            self.beta  = [
                [0],
                [0, 0]
            ];
        #}
        elif(s == 2):
        #{
            self.r     = [0, 1/3, 2/3];
            self.alpha = [0, 0, 3/4];
            self.beta  = [
                [0],
                [0, 3/4]
            ];
        #}
        elif(s == 3):
        #{
            self.r     = [0, 1/6, 2/3, 1/6];
            self.alpha = [0, 0, 1/2, 1];
            self.beta  = [
                [0],
                [0, 1/2],
                [0, -1, 2]
            ];
        #}
        elif(self.s == "heun" or self.s == "Heun"):
        #{
            self.r     = [0, 1/4, 0, 3/4];
            self.alpha = [0, 0, 1/3, 2/3];
            self.beta  = [
                [0],
                [0, 1/3],
                [0, 0, 2/3]
            ];
        #}
        elif(s == 4):
        #{
            self.r     = [0, 1/6, 1/3, 1/3, 1/6];
            self.alpha = [0, 0, 1/2, 1/2, 1];
            self.beta  = [
                [0],
                [0, 1/2],
                [0, 0, 1/2],
                [0, 0, 0, 1]
            ];
        #}
    #}


    def Solve(self):
    #{
        self.__loadCoeff(self.s);
        grid = [[self.x_0, self.y_0]];

        for i in range(self.n):
        #{
            new_x = grid[-1][0] + self.h;
            new_y = self.__computeNext(grid[-1]);

            grid.append([new_x, new_y]);
        #}

        return grid;
    #}
#}

