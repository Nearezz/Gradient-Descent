## Using Gradient Descent to minimize the function (x+5)^2
import matplotlib.pyplot as plt
import numpy as np


## Creating the graph of f(x)
def f(x): 
    return (x+5)**2

def f_prime(x):
    return 2*(x+5)

x = np.linspace(-10,0,100)
y = f(x)
plt.plot(x,y,label="f(x) = x+5^2",color="blue")


lr = 0.1 ## The learning rate is how much the function will update.

x_old = -4 ##stating from a random value of x technically can be anything 
for i in range(10):
    x_new = x_old - (lr * f_prime(x_old)) ## important fourmula
    y_new = f(x_new)

    plt.plot(x_new,y_new,"ro")
    x_old = x_new
plt.show
