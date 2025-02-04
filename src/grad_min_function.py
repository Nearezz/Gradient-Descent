## Using Gradient Descent to minimize the function (x+5)^2
import matplotlib.pyplot as plt
import numpy as np
import random
import math

## Creating the graph of f(x)
def f(x): 
    return (x+5)**2

def f_prime(x):
    return 2*(x+5)

x = np.linspace(-10,0,100)
y = f(x)

print(type(y))
plt.plot(x,y,label="f(x) = x+5^2",color="blue")
iteration = True

x_old = np.random.uniform(-10,0)
iterations = 0
while (iteration): 
    if abs(f_prime(x_old)) < math.pow(10,-13):
        print(iterations)
        iteration = False

    lr = np.random.normal(loc=0,scale=0.2)
    x_new = x_old - (lr * f_prime(x_old)) ## important fourmula
    y_new = f(x_new)

    plt.plot(x_new,y_new,"ro")
    print("The new x value is: ",x_new)
    x_old = x_new
    iterations += 1


plt.show()
