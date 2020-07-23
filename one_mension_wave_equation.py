import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
L = 6
T = 0.003
h = 0.03
tao = 0.0000001
num_t = []
num_t1 = []
num_t2 = []

for i in range(0, 30000, 1):
    #t = t.append('i')
    num_t.append(i)
print(num_t)

for i in range(0, 30000-1, 1):
    #t = t.append('i')
    num_t1.append(i)
print(num_t1)

for i in range(0, 30000-1, 1):
    #t = t.append('i')
    num_t2.append(i)
print(num_t2)

J = int(L/h)
N = int(T/tao)
vp =4600
r = vp*tao/h
print('N',N)  #30000
print('J',J)  #200
#print(r)
#双循环定义二维列表
u = [[0 for i in range(N)] for i in range(J)]
print(type(u))
#雷克子波
#fricker = np.zeros([1,N])
fricker = []
fm = 50

for i in range(0, N, 1):
    if(i < 100):
        fricker.append(10000*(1 - 2 * (math.pi * fm * (i-50) * 0.001) ** 2) * math.exp(-(math.pi * fm * (i-50) * 0.001) ** 2))
    else:
        fricker.append(0)
fricker = [fricker]
print(fricker)
print(type(fricker))

#u = np.array(u)
#fricker = np.array(fricker)


u[:][0] = 0
u[:][1] = 0
'''
for n in range(1, N-1, 1):# J = 200
    for j in range(1, J-1, 1):
        u[j, n+1] = r**2*(u[j-1, n]+u[j+1, n]) + 2*(1-r**2)*u[j,n]-u[j,n-1]
       # print(u[j,i+1])
        u[J-1,n+1] = u[J-2,n+1]
    u[0,n+1] = u[1,n+1] + 0.03*fricker[0,n+1]
    print(u[0,n+1])
    #u[0, n + 1] = u[1, n + 1] + 1000
    print((fricker[0,n+1]))
fricker[0,500] = 20
print(fricker[0,500])
print(type(h))
'''
for n in range(1, N-1, 1):
    for j in range(1, J-1, 1):
        u[j][n+1] = r**2*(u[j-1][n] + u[j+1][n]) + 2*(1-r**2)*u[j][n] - u[j][n-1]
        u[J-1][n+1] = u[J-2][n+1]
        u[0][n+1] = u[1][n+1] + h*fricker[0][n+1]
'''
plt.figure(figsize=(20,3))
plt.plot(u[:,0],u[:,1],linewidth='0.5')
plt.show()
'''
'''
print('我要打印脉冲响应了！')
print(fricker)
print('我要打印位移了！')
print(u)

for i in range(1, N-1, 1):
    print(fricker[0,i+1])
'''

print('N',N)  #30000
print('J',J)  #200
print('我要打印位移了！')
print(u)

#plt.figure(figsize=(20,3))
fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(u[2][:],linewidth='0.5')
ax.set_xlabel('time(s)')
ax.set_ylabel('Amp')
plt.show()



