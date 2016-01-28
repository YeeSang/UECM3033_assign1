# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( x**2*sy.exp(-x**2), (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array( [[3,1,6,3,1,2,4,6,8,9], [1,1,2,5,7,3,8,4,2,2],[9,7,5,3,1,2,4,5,7,8],[2,4,3,6,8,9,6,4,8,0],[1,2,3,4,5,6,7,8,9,0],[7,8,9,3,1,6,3,5,8,1],[6,7,8,2,4,5,6,7,1,2],[8,5,3,1,3,5,6,8,9,2],[1,2,4,2,5,3,5,8,5,2],[7,8,9,3,2,1,5,6,8,9]] )
    b = np.array([119,38,57,106,45,124,83,102,41,79])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1305785
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
