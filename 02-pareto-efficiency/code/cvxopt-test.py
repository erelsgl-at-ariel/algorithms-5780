#!python3

import numpy
from cvxopt import matrix, solvers

# Solve the linear program: "maximize 2x + 3y subject to 4x + 5y <= 6, x >= 0, y >= 0"
A = matrix([[4.0, 1.0, 0.0], [5.0, 0.0, 1.0]])
b = matrix([6.0, 0.0, 0.0])
c = matrix([2.0, 3.0])
sol=solvers.lp(c,A,b)
print(sol['x'])

# Solve the quadratic program: "maximize 2x^2 + y^2   subject to   x>=0, y>=0, x+y=1"
Q = 2*matrix([ [2, .5], [.5, 1] ])
p = matrix([1.0, 1.0])
G = matrix([[-1.0,0.0],[0.0,-1.0]])
h = matrix([0.0,0.0])
A = matrix([1.0, 1.0], (1,2))
b = matrix(1.0)
sol=solvers.qp(Q, p, G, h, A, b)
print(sol['x'])
