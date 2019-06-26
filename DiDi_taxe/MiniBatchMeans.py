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


plt.rcParams['figure.figsize'] = (90.0, 60.0)

order = pd.read_csv("./data/order_20161101", header=None)
Driver_order = pd.read_csv("./data/driver_to_order_11_01.csv")
order.columns = ["order","start_t","end_t","start_lo1","start_lo2","end_lo1","end_lo2"]
order = order.drop_duplicates(subset=["order"], keep="last")
data_lab = pd.merge(Driver_order, order, on=['order'])

running_order = data_lab[["driver","start_t","end_t","end_lo1","end_lo2"]]
need = data_lab[["order","start_t","start_lo1","start_lo2"]]

drivers = list(running_order["driver"])

need = Add_local_time(need,"start_t",['start_h','start_m','start_s'])

need = need.sort_values\
        (["start_t"], axis=0, ascending=True, inplace=False, kind='quicksort',na_position='last')
need = need.reset_index(drop=True)

running_order = running_order.sort_values\
        (["driver","start_t"], axis=0, ascending=True, inplace=False, kind='quicksort',na_position='last')
running_order = running_order.reset_index(drop=True)



empty_car = []
for driver in drivers[1:12]:
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
#pd.concat(temp,empty_car)

#for cc in empty_car:
    #print(cc)


'''
need.sort_values\
        (['start_h','start_m','start_s'], axis=0, ascending=True, inplace=True, kind='quicksort',na_position='last')
need = need.reset_index(drop=True)
'''
#plt.scatter(X["start_lo1"], X["start_lo2"], marker='o',s=1)
#plt.show()
#print(X)
#print(y)

'''
for h in range(0,24):
    need_lo = need.loc[need['end_h'] == h, ["end_lo1","end_lo2"]]
    running_order_lo = running_order.loc[need['start_h'] == h, ["start_lo1","start_lo2"]]
    model = MiniBatchKMeans(n_clusters=20, batch_size=500, random_state=9).fit(need_lo)
    need_lo_pred = model.predict(need_lo)
    running_order_lo_pred = model.predict(need_lo)
    score = metrics.calinski_harabaz_score(need_lo, need_lo_pred)
'''


'''
    plt.subplot(4,6,h+1)
    plt.scatter(need_lo["start_lo1"], need_lo["start_lo2"], c=need_lo_pred)
    plt.text(.99, .01, ('MBKM h=%d k=%d, score: %.2f' % (h,20,score)),
                 transform=plt.gca().transAxes, size=10,
                 horizontalalignment='right')
plt.show()
'''















