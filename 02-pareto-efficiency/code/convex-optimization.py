#!python3

import cvxpy as cp
from cvxpy import log

print("\n\n\nPROBLEM #1")
print("A cake with three regions has to be divided among two people with values:")
print("19 0 81")
print("0 20 80")

# Define x = the fraction of the third region given to the first agent.
x = cp.Variable()

print("\nAttempt 1: find a sum-maximizing division:")
prob = cp.Problem(
    cp.Maximize((81*x + 19) + (80*(1-x)+20)),
    [0 <= x, x <= 1])
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal x", x.value)


print("\nAttempt 2: maximize the sum of roots:")
prob = cp.Problem(
    cp.Maximize((81*x + 19)**0.5 + (80*(1-x)+20)**0.5),
    [0 <= x, x <= 1])
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal x", x.value)


print("\nAttempt 3: maximize the sum of logs:")
prob = cp.Problem(
    cp.Maximize(log(81*x + 19) + log(80*(1-x)+20)),
    [0 <= x, x <= 1])
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal x", x.value)

print("\n\n\nPROBLEM #2")
print("A cake with four regions has to be divided among 3 people with values:")
print("19 0 0 81")
print("0 20 0 80")
print("0 0 40 60")

# Define x,y,z = the fraction of the fourth region given to agents 1,2,3.
x = cp.Variable()
y = cp.Variable()
z = cp.Variable()

print("\nMaximize the sum of logs:")
prob = cp.Problem(
    cp.Maximize(log(81*x + 19) + log(80*y+20) + log(60*z+40)),
    [0 <= x, x <= 1, 0<=y, y<=1, 0<=z, z<=1, x+y+z==1])
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal x", x.value)
print("optimal y", y.value)
print("optimal z", z.value)
