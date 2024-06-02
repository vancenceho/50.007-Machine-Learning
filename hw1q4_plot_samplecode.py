import numpy as np
import matplotlib.pyplot as	plt

tn = tX.shape[0]
vn = vX.shape[0]

tloss = []
vloss = []
index = np.arange(0, 5, 0.1)

for	i in index:
    w =  ridgeregression(tX, tY, 10**-i)
    tloss = tloss + [np.sum((np.dot(tX, w) − tY)**2)/tn/2]
    vloss = vloss + [np.sum((np.dot(vX, w) − vY)**2)/vn/2]
plt.plot(index, np.log(tloss), 'r')
plt.plot(index, np.log(vloss), 'b')
