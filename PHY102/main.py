__author__ = 'He Bai'
import numpy as np

def gauss3(n, a, b, c, d):
    i = 1
    while i <= n - 1:
        b[i] = b[i-1]*b[i]/a[i]-c[i-1]
        c[i] = b[i-1]*c[i]/a[i]
        d[i] = b[i-1]*d[i]/a[i]-d[i-1]
        a[i] = 0
        i = i + 1

    i = n - 2
    while i >= 0:
        b[i] = b[i]*b[i+1]/c[i]
        d[i] = d[i]*b[i+1]/c[i]-d[i+1]
        c[i] = 0
        i = i - 1

    i = 0
    while i <= n - 1:
        d[i] = d[i] / b[i]
        i = i + 1
    return np.transpose(d)

def chol3(n,a,b,c,d):
    L1 = np.zeros((n,1))
    L2 = np.zeros((n,1))
    LT2 = np.zeros((n,1))
    LT3 = np.zeros((n,1))
    Y = np.zeros((n,1))

    i = 0
    while i <= n-2:
        L2[i] = np.sqrt(b[i]-L1[i]*L1[i])
        L1[i+1] = a[i+1]/L2[i]
        i = i + 1

    L2[n-1] = np.sqrt(b[n-1]-L1[n-1]*L1[n-1])

    i = 0
    while i <= n - 1:
        LT2[i] = L2[i]
        i = i + 1

    i = 0
    while i <= n - 2:
        LT3[i] = L1[i+1]
        i = i + 1

    Y[0] = d[0]/L2[0]

    i = 1
    while i <= n - 1:
        Y[i] = (d[i]-L1[i]*Y[i-1])/L2[i]
        i = i + 1

    x[n-1] = Y[n-1]/LT2[n-1]

    i = n - 2
    while i >= 0:
        x[i] = (Y[i]-LT3[i]*x[i+1])/LT2[i]
        i = i - 1
    return np.transpose(x)

def thomas3(n,a,b,c,d):
    i = 1
    while i <= n - 1:
        b[i] = b[i-1]*b[i]/a[i]-c[i-1]
        c[i] = b[i-1]*c[i]/a[i]
        d[i] = b[i-1]*d[i]/a[i]-d[i-1]
        i = i + 1
    x[n-1] = d[n-1]/b[n-1]
    i = n - 2
    while i >= 0:
        x[i] = (d[i] - c[i]*x[i+1])/b[i]
        i = i - 1
    return np.transpose(x)

'''
Example code for n = 3
'''
n = 3
a = np.zeros((n, 1))
b = np.zeros((n, 1))
c = np.zeros((n, 1))
d = np.zeros((n, 1))
x = np.zeros((n, 1))
d[0] = 1
d[n - 1] = 1

i = 1
while i <= n - 1:
    a[i] = -1
    i = i + 1
i = 0
while i <= n - 1:
    b[i] = 2
    i = i + 1
i = 0
while i <= n - 2:
    c[i] = -1
    i = i + 1

x = gauss3(n, a,b,c,d)
print x

n = 3
a = np.zeros((n, 1))
b = np.zeros((n, 1))
c = np.zeros((n, 1))
d = np.zeros((n, 1))
x = np.zeros((n, 1))
d[0] = 1
d[n - 1] = 1

i = 1
while i <= n - 1:
    a[i] = -1
    i = i + 1
i = 0
while i <= n - 1:
    b[i] = 2
    i = i + 1
i = 0
while i <= n - 2:
    c[i] = -1
    i = i + 1

x = chol3(n, a,b,c,d)
print x

n = 3
a = np.zeros((n, 1))
b = np.zeros((n, 1))
c = np.zeros((n, 1))
d = np.zeros((n, 1))
x = np.zeros((n, 1))
d[0] = 1
d[n - 1] = 1

i = 1
while i <= n - 1:
    a[i] = -1
    i = i + 1
i = 0
while i <= n - 1:
    b[i] = 2
    i = i + 1
i = 0
while i <= n - 2:
    c[i] = -1
    i = i + 1

x = thomas3(n, a,b,c,d)
print x