import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from sklearn import metrics
import pandas as pd

plt.rcParams['figure.figsize'] = (45.0, 45.0)


order = pd.read_csv("./order_20161101", header=None)
#order = np.loadtxt("./order_20161101")
order.columns = ["order","start_t","end_t","start_lo1","start_lo2","end_lo1","end_lo2"]
print(order)

X = order[["start_lo1","start_lo2"]]
#plt.scatter(X["start_lo1"], X["start_lo2"], marker='o',s=1)
#plt.show()
#print(X)
#print(y)

for index, k in enumerate((12,13,14,15,16,17,18,19,20)):
    plt.subplot (3, 3, index + 1)
    model = MiniBatchKMeans (n_clusters=k, batch_size=200, random_state=9).fit(X)
    y_pred = model.predict (X)
    score = metrics.calinski_harabaz_score (X, y_pred)
    plt.scatter(X["start_lo1"], X["start_lo2"], c=y_pred,s=1)
    plt.text(.99, .01, ('KM k=%d, score: %.2f' % (k,score)),
                 transform=plt.gca().transAxes, size=50,
                 horizontalalignment='right')
plt.show()
