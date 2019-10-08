import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
x = np.array(['A<10','10~19','20~29','30~31','A>40'])
plt.figure()
plt.subplots_adjust(hspace=.4)
for i in range(1,11):
	file = pd.read_csv(repr(i)+'.csv', header = None).iloc[:,1:]
	file = np.array(file)
	print(file.shape)
	plt.subplot(3,4,i)
	plt.ylim(0,50)
	plt.title('Team#'+repr(i))
	for m in range(file.shape[1]):
		plt.plot(x,file[:,m], label= 'Alg#'+repr(m+1))
	plt.legend(loc='upper left',
		ncol=3, mode="expand", borderaxespad=0.)
plt.show()
