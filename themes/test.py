
import numpy as np
import matplotlib.pyplot as plt

n = 100

np.random.seed(1)
v1 = np.random.normal(0,1,(n,1))
v2 = np.random.normal(0,1,(n,1))

# Comment

r1 = v1/v2


lim = 50
dx = 1

centers = np.arange(-lim, lim+dx, dx)
counts = np.zeros((2*lim+1))

plt.hist(np.round(r1), int(2*lim/dx+1), (-lim+dx/2, lim-dx/2))
plt.show()

mean_test = np.zeros((n,1))
mean_test[0] = r1[0]
for i in range(1,n):
    mean_test[i] = (mean_test[i-1]*i + r1[i])/(i+1)

plt.plot(np.arange(0,len(mean_test)),mean_test)
plt.show()

