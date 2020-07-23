import matplotlib.pyplot as plt
import numpy as np
'''
filename = 'out_x1.dat'
x,y = [],[]
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        x.append(value[0])
        y.append(value[1])
print(x)
print(y)
plt.plot(x,y)
plt.figure(figsize=(12,6))
plt.subplot(311)
plt.subplot(312)
plt.subplot(313)
plt.show()
'''
'''
data = np.loadtxt('out_x1.dat')
plt.figure(figsize=(20,3))
plt.plot(data[:,0],data[:,1],linewidth='0.5')
plt.show()
'''


a = np.array([1,2,3,4,5])
print(a)
b = np.zeros((2,3))
print(b)
c = np.arange(10)
print(c)
d = np.arange(2,10,dtype=np.float)
print(d)
e = np.linspace(1.0,4.0,6)
print(e)
f = np.indices((3,3))
print(f)