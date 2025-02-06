import numpy as np 
import matplotlib.pyplot as plot 


def f(x): 
    return np.sin(x)

def f_prime(x):
    return np.cos(x)


def f_doubleprime(x):
    return -np.sin(x)

x = np.linspace(0,4*np.pi,100)
y = f(x)

plot.plot(x,y,label="Graph of sin(x)")

xNot = np.random.uniform(0,4*np.pi)



