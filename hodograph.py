#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt 


#n = int(input("Введите n:"))

n = 4

a = [0]

for i in range(0, n):
    a.append(int(input("Введите a" + str(i+1) + ":")))

def Im(a, w):
    return a[2]*w - a[4]*w*w*w

def Re(a, w):
    return a[1] - a[3]*w*w

w2 = math.sqrt(a[1] / a[3])
w3 = 0

if Im(a, 0) == 0:
    w3 = math.sqrt(a[2] / a[4])

p1 = [0, Re(a, 0), Im(a, 0)]
p2 = [w2, 0, Im(a, w2)]  
p3 = [w3, Re(a, w3), 0]

if w2 > w3:
    points = [p1, p3, p2]
else:
    points = [p1, p2, p3]

x = []; y = []

x.append(1)
y.append(0)

for point in points:
    x.append(point[1])
    y.append(point[2])

x.append(-40)
y.append(-40)

plt.plot(x, y)
plt.xlabel('Re')
plt.ylabel('Im')

plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')


plt.title('My first graph!') 

plt.show() 

