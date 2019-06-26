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

gps = pd.read_csv("./gps_20161101", header=None)
gps.columns = ["driver","order","time","lo1","lo2"]

drivers = set(gps["driver"])
O_order = set(order["order"])
G_order = set(gps["order"])

print("drivers: ", len(drivers))
print("order: ",len(O_order))
print("gps  : ",len(G_order))
print("jiao ji = ",len(O_order&G_order))