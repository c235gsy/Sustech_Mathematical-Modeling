import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from sklearn import metrics
import pandas as pd
import time


def Add_local_time(data_df,index_in,index_out):
    time_local = []
    for t in data_df[index_in]:
        time_local.append(list(map(int,time.strftime('%H:%M:%S',time.localtime(t)).split(":"))))
    time_DF = pd.DataFrame(time_local)
    time_DF.columns = index_out
    data_df_out = pd.concat([data_df.drop(columns=[index_in]), time_DF], axis=1)
    return data_df_out



pd.set_option('display.max_colwidth',10000)

plt.rcParams['figure.figsize'] = (45.0, 45.0)
order = pd.read_csv("./order_20161101", header=None)
#order = np.loadtxt("./order_20161101")
order.columns = ["order","start_t","end_t","start_lo1","start_lo2","end_lo1","end_lo2"]
offer = order[["order","end_t","end_lo1","end_lo2"]]
need = order[["start_t","start_lo1","start_lo2"]]

need = Add_local_time(need,"start_t",['start_h','start_m','start_s'])
offer = Add_local_time(offer,"end_t",['end_h','end_m','end_s'])


need.sort_values\
        (["start_h", "start_m", "start_s"], axis=0, ascending=True, inplace=True, kind='quicksort',na_position='last')
need = need.reset_index(drop=True)
need_lo12 = need[["start_lo1","start_lo2"]]
model = MiniBatchKMeans (n_clusters=20, batch_size=200, random_state=9).fit(need_lo12)
need_lo = model.predict(need_lo12)
need["start_lo"] = need_lo
need = need.drop(columns=["start_lo1","start_lo2"])

need.to_csv('11_01.csv',index=0)
print(need)


