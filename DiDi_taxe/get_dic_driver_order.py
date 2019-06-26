import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from sklearn import metrics
import pandas as pd
import time
#def get_dic_driver_order(gps):

gps = pd.read_csv("./gps_20161101", header=None, nrows =10000)
gps.columns = ["driver","order","time","lo1","lo2"]
#gps = gps.sample(frac=0.01, replace=False, weights=None, random_state=None, axis=0)
print("read finish")

time_local = []
for t in gps["time"]:
    time_local.append(time.strftime('%H:%M:%S',time.localtime(t)).split(":"))
timeDF = pd.DataFrame(time_local)

timeDF.columns = ['h','m','s']
gps = pd.concat([gps.drop(columns=["time","order"]), timeDF], axis=1)


driver = list (gps["driver"])

dic_driver_time = {dd: None for dd in driver}

for dr in driver:
    dic_driver_time[dr] = gps.loc[gps['driver'] == dr, ["h", "m", "s","lo1", "lo2"]]
    dic_driver_time[dr].sort_values\
        (["h", "m", "s"], axis=0, ascending=True, inplace=True, kind='quicksort',na_position='last')
    dic_driver_time[dr] = dic_driver_time[dr].reset_index(drop=True)

print(dic_driver_time[driver[0]])

