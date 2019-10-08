import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

points = np.array([0,8])
plt.figure()
plt.subplots_adjust(hspace=.4)
for i in range(1,11):
	file = np.array(pd.read_csv('g'+repr(i)+'.csv', header = None).iloc[:,1:])
	print(file.shape)
	plt.subplot(3,4,i)
	plt.ylim(0,100)
	plt.xlim(-1,15)
	plt.xticks(np.array([3,10]), ('Woman', 'Man'))
	plt.title('Team#'+repr(i))
	for m in range(file.shape[1]):
		plt.bar(points+m,file[:,m], label= 'Alg#'+repr(m+1))
	plt.legend(loc='upper left',
		ncol=3, mode="expand", borderaxespad=0.)
plt.show()
