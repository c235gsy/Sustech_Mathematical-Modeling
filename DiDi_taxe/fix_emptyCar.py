import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from sklearn import metrics
import pandas as pd
import time
pd.set_option('display.max_colwidth',100)
pd.set_option('display.max_column',12)

for d in range(2, 31):
    mark = "0"
    if d >= 10:
        mark = str(d)
    else:
        mark = mark + str(d)
    #plt.rcParams['figure.figsize'] = (90.0, 60.0)
    empty_car = pd.read_csv("./need_and_emptyCar/empty_car_11_"+mark+".csv")
    print(empty_car.head())
    empty_car = empty_car.drop_duplicates (keep="first")
    empty_car.to_csv ("./need_and_emptyCar/empty_car_11_"+mark+".csv", index=0)