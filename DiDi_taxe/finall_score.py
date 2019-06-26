import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from sklearn import metrics
import pandas as pd
import time
pd.set_option('display.max_colwidth',10000)
pd.set_option('display.max_column',30)
import get_Kmeans_model

def find_the_offer(data,t1,t2):
    #bool_infor =
    return data.loc[((data["end_t"] > t1) & (t1 > data["start_t"])) |
                    ((data["start_t"] < t2) & (t2 < data["end_t"])) |
                    ((data["start_t"] >= t1) & (data["end_t"] <= t2))]


model = get_Kmeans_model.get_Kmeans_model(K=20)

centers = model.cluster_centers_
for c in centers:
    print(c[1],",",c[0])

for d in range(7,14):
    mark = "0"
    if d >= 10:
        mark = str(d)
    else:
        mark = mark + str(d)
    plt.rcParams['figure.figsize'] = (90.0, 60.0)
    start_time = "2016-11-%s 00:00:00" % (mark)
    start_timestamp = time.mktime(time.strptime(start_time, "%Y-%m-%d %H:%M:%S"))
    empty_car = pd.read_csv("./need_and_emptyCar/empty_car_11_"+mark+".csv")
    need = pd.read_csv("./need_and_emptyCar/need_11_"+mark+".csv")

    need["cluster"] = model.predict(need[["start_lo1", "start_lo2"]])
    #print(need["cluster"].value_counts())
    empty_car["cluster"] = model.predict(empty_car[["lo1", "lo2"]])

    need = need.drop(columns=["start_lo1", "start_lo2"])
    empty_car = empty_car.drop(columns=["lo1", "lo2"])

    S_for_day = pd.DataFrame(index=["area%i"%c for c in range(0,20)],
                             columns=["hour%i"%c for c in range(0,24)])
    #O = pd.DataFrame (columns=["area%i" % c for c in range (0, 20)], index=["hour%i" % c for c in range (0, 24)])
    #N = pd.DataFrame (columns=["area%i" % c for c in range (0, 20)], index=["hour%i" % c for c in range (0, 24)])
    #print(S,O,N,"\n")
    #print(S_for_day)

    for H in range(0,24):
        base_time_H = start_timestamp + 3600*H
        S_for_hour = pd.DataFrame(index=["area%i" % c for c in range (0, 20)],
                                 columns=["min%i" % c for c in range (0, 60)])
        #print(S_for_hour)
        for M in range(0,60):
            base_time_M = base_time_H + 60*M
            flagA, flagB = base_time_M, base_time_M + 60
            offer_in_range = find_the_offer(empty_car,flagA, flagB)
            need_in_range = need.loc[(need["start_t"] >= flagA) & (need["start_t"] < flagB)]
            for A in range(0,20):
                o = len(offer_in_range.loc[offer_in_range["cluster"] == A])
                n = len(need_in_range.loc[need_in_range["cluster"] == A])
                if n*o != 0:
                    S_for_hour.iat[A,M] = abs(o-n)/min(n,o)
        S_for_day['hour%i'%H] = S_for_hour.mean(axis=1)

    S_for_day.to_csv("./result2/result_11%s.csv"%mark)




