import matplotlib.pyplot as plt

def plot_confusion_matrix(cm, classes, normalize=True,title=None,cmap=plt.cm.BuPu):
	if not title:
		title = 'Confusion Matrix'

	#calculataion normalized confusion matrix
	cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
	cm = cm*100
	logging.info("Normalized confusion matrix")
	logging.info(cm)

	#setting up plots
	fig, ax = plt.subplots()
	im = ax.imshow(cm,cmap=cmap)
    ax.figure.colorbar(im, ax=ax, label ='Accuracy [in %]')
    #show all ticks
    ax.set(xticks=np.arange(cm.shape[1]), yticks=np.arange(cm.shape[0]),
    	xticklabels=classes, yticklabels=classes, title=title,
    	ylabel='True label', xlabel='Predicted label')
    ax.tick_params(labelsize = 6)
    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
    	for j in range(cm.shape[1]):
    		if cm[i,j] > 0.09:
    			ax.text(j, i, format(cm[i, j], fmt),
    				ha="center", va="center", size= 6,
    				color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax

#plt.savefig(name + '.eps', dpi = 200)
#plt.show()