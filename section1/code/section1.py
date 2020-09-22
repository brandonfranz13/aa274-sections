#!/usr/bin/env python

#Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import minimize

#Functions

x = np.arange(0., 2*np.pi, 0.01)

def sin_np(x):
    return np.sin(x)

y = sin_np(x)


#Integrate
def integrand(x):
    return sin_np(x)

y_int = quad(integrand, 0, 1)
print("Integral of sin(x) from x=0..1: {}".format(y_int[0]))

#Minimize
x0 = 0
print("Nelder-Mead simplex method:")
res = minimize(sin_np, x0, method='nelder-mead', options={'xtol': 1e-8, 'disp': True})

#Plot
plt.plot(x,y)
plt.title("Plot of Sin(x)")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()