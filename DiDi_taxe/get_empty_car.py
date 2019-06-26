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


def Add_local_time(data_df,index_in,index_out):
    time_local = []
    for t in data_df[index_in]:
        time_local.append(list(map(int,time.strftime('%H:%M:%S',time.localtime(t)).split(":"))))
    time_DF = pd.DataFrame(time_local)
    time_DF.columns = index_out
    data_df_out = pd.concat([data_df, time_DF], axis=1)
    return data_df_out


for d in range(1, 2):
    mark = "0"
    if d >= 10:
        mark = str(d)
    else:
        mark = mark + str(d)
    #plt.rcParams['figure.figsize'] = (90.0, 60.0)

    order = pd.read_csv("./data/order_201611"+mark, header=None)
    Driver_order = pd.read_csv("./data/driver_to_order_11_"+mark+".csv")
    order.columns = ["order","start_t","end_t","start_lo1","start_lo2","end_lo1","end_lo2"]
    print("order:",len(order))
    order = order.drop_duplicates(subset=["order"], keep="last")
    print("order:",len (order))
    print ("Driver_order:", len (Driver_order))
    data_lab = pd.merge(Driver_order, order, on=['order'])
    print("data_lab:",len(data_lab))

    need = data_lab[["order", "start_t", "start_lo1", "start_lo2"]]
    running_order = data_lab[["driver","start_t","end_t","end_lo1","end_lo2"]]
    print(len(running_order))
    drivers = list(set(running_order["driver"]))
    print(len(drivers))

    need = need.sort_values \
        (["start_t"], axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')
    need = need.reset_index (drop=True)

    running_order = running_order.sort_values\
        (["driver","start_t","end_t"], axis=0, ascending=True, inplace=False, kind='quicksort',na_position='last')
    running_order = running_order.reset_index(drop=True)


    empty_car = []
    for driver in drivers:
        dada = running_order.loc[running_order['driver'] == driver, ["start_t","end_t","end_lo1","end_lo2"]]
        e = list(dada["end_t"])
        s = list(dada["start_t"])
        lo1 = list(dada["end_lo1"])
        lo2 = list(dada["end_lo2"])
        n = len(e)
        lili = [[driver,e[i],s[i+1],lo1[i],lo2[i]] for i in range(0, n-1)]
        empty_car.extend (lili)

    empty_car = pd.DataFrame(empty_car)
    empty_car.columns = ["driver","start_t","end_t","lo1","lo2"]
    print(empty_car.head())
    print(need.head())
    #empty_car.to_csv ('./need_and_emptyCar/empty_car_11_' + mark + '.csv', index=0)
    #need.to_csv ('./need_and_emptyCar/need_11_' + mark + '.csv', index=0)
