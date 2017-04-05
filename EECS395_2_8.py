import matplotlib.pyplot as plt
import numpy as np
import math

x=[];
y=[];
y_prime=[];
for i in range(-49,50):
    x.append(i/25);
    y.append(x[i+49]*math.tanh(x[i+49]));
    y_prime.append(math.tanh(x[i+49]+x[i+49]/(math.cosh(x[i+49])**2)))

plt.figure(1);
plt.plot(x,y);


plt.figure(2);
plt.plot(x,y_prime);

plt.show();
