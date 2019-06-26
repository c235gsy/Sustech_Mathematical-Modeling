import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from sklearn import metrics
import pandas as pd
import time


def get_Kmeans_model(K):
    need = pd.DataFrame()
    for d in range(7,14):
        mark = "0"
        if d >= 10:
            mark = str(d)
        else:
            mark = mark + str(d)
        #empty_car = pd.read_csv("./need_and_emptyCar/empty_car_11_"+mark+".csv")
        need = pd.concat([pd.read_csv("./need_and_emptyCar/need_11_"+mark+".csv"),need])

    need_lo = need[["start_lo1","start_lo2"]]

    model = MiniBatchKMeans(n_clusters=K, batch_size=500, random_state=9).fit(need_lo)
    return model


plt.rcParams['figure.figsize'] = (80.0, 60.0)

K =20

need = pd.DataFrame()
for d in range(7,14):
    mark = "0"
    if d >= 10:
        mark = str(d)
    else:
        mark = mark + str(d)
    #empty_car = pd.read_csv("./need_and_emptyCar/empty_car_11_"+mark+".csv")
    need = pd.concat([pd.read_csv("./need_and_emptyCar/need_11_"+mark+".csv"),need])

need_lo = need[["start_lo1","start_lo2"]]

model = MiniBatchKMeans(n_clusters=K, batch_size=500, random_state=9).fit(need_lo)

c = model.predict(need_lo)

plt.scatter(need_lo["start_lo1"], need_lo["start_lo2"], c=c, s=5, alpha=0.3)
plt.axis ([103.7, 104.5, 30.4, 31,])
plt.savefig("./all_areas.png")
