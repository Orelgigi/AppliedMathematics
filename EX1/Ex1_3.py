import numpy as np
import matplotlib.pyplot as plt

# Question 3 Section 1
Ts=1/44100
x=np.arange(0,1-Ts,Ts)
y1=np.cos(2*np.pi*x)
plt.plot(x,y1)
y2=np.sin(2*np.pi*x)
plt.plot(x,y1,'b',x,y2,'r')
plt.show()

# Question 3 Section 2
print( np.sum(y1 * y2) )
print( np.dot(y1 , y2) )