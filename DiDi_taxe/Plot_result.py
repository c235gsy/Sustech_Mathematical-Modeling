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


model = get_Kmeans_model.get_Kmeans_model(20)
centers = model.cluster_centers_
for c in centers:
    print(c[1],",",c[0])


def line_plot_for_all(data):

    plt.rcParams['figure.figsize'] = (15.0, 10.0)
    plt.figure ()
    data.plot ()
    plt.legend (loc='best')
    plt.savefig ("./method_4_lines.png")


def point_polts_for_hour(h_range,n1,n2,data,cens):
    plt.rcParams['figure.figsize'] = (90.0, 60.0)
    ind = 1
    for h in h_range:
        x = [c[1] for c in cens]
        y = [c[0] for c in cens]

        Area = list((1000*data["hour%i"%h]**2*10))
        print(Area)
        plt.subplot (n1, n2, ind)

        color = ['#FFEFD5','#FFDAB9','#CD853F','#FFC0CB','#DDA0DD','#B0E0E6','#800080',
                 '#FF0000','#BC8F8F','#4169E1','#8B4513','#FA8072','#FAA460','#2E8B57',
                 '#FFF5EE','#A0522D','#C0C0C0','#87CEEB','#6A5ACD','#708090','#FFFAFA',
                 '#00FF7F','#4682B4','#D2B48C','#008080','#D8BFD8','#FF6347','#40E0D0',
                 '#EE82EE','#F5DEB3','#FFFFFF','#F5F5F5','#FFFF00','#9ACD32']

        for a in range(0,20):
            plt.scatter (x[a], y[a], c=color[a], s=Area[a],label="area%i" % a)
        #plt.axis ([30.5, 30.9, 103.8, 104.2])
        plt.legend (loc='best',frameon = None,fontsize=10,markerscale=0.25)

        plt.text (.99, .01, ('MBKM h=%d ' % (h)), transform=plt.gca ().transAxes, size=30,
                  horizontalalignment='right')
        ind += 1

    plt.savefig("./method_4_points.png")


def line_polts_for_area(area_range,n1,n2,data,cens):
    plt.rcParams['figure.figsize'] = (90.0, 60.0)
    ind = 1
    for a in area_range:
        x = [c[1] for c in cens]
        y = [c[0] for c in cens]

    Area = list ((data["hour%i" % a] ** 2) / 10)
    print (Area)
    plt.subplot (n1, n2, ind)

    color = ['#FFEFD5','#FFDAB9','#CD853F','#FFC0CB','#DDA0DD','#B0E0E6','#800080',
                 '#FF0000','#BC8F8F','#4169E1','#8B4513','#FA8072','#FAA460','#2E8B57',
                 '#FFF5EE','#A0522D','#C0C0C0','#87CEEB','#6A5ACD','#708090','#FFFAFA',
                 '#00FF7F','#4682B4','#D2B48C','#008080','#D8BFD8','#FF6347','#40E0D0',
                 '#EE82EE','#F5DEB3','#FFFFFF','#F5F5F5','#FFFF00','#9ACD32']

    for a in range(0,20):
        plt.scatter (x[a], y[a], c=color[a], s=Area[a],label="area%i" % a)

        plt.legend (loc='best',frameon = None,fontsize=10,markerscale=0.25)

        plt.text (.99, .01, ('MBKM h=%d ' % (a)), transform=plt.gca ().transAxes, size=30,
                  horizontalalignment='right')
        ind += 1

    plt.savefig("./11111111111111.png")



for d in range(8,9):
    mark = "0"
    if d >= 10:
        mark = str(d)
    else:
        mark = mark + str(d)
    res = pd.read_csv("./result4/result_11%s.csv"%mark,index_col=0)
    #res = res.cumsum ()

    #line_plot_for_all(res.T)
    print(res)

    point_polts_for_hour(range(0,24),4,6,res,centers)




    '''
    for h in range (0, 24):
        need_lo = need.loc[need['end_h'] == h, ["end_lo1", "end_lo2"]]
        running_order_lo = running_order.loc[need['start_h'] == h, ["start_lo1", "start_lo2"]]
        model = MiniBatchKMeans (n_clusters=20, batch_size=500, random_state=9).fit (need_lo)
        need_lo_pred = model.predict (need_lo)
        running_order_lo_pred = model.predict (need_lo)
        score = metrics.calinski_harabaz_score (need_lo, need_lo_pred)

        plt.subplot (4, 6, h + 1)
        plt.scatter (need_lo["start_lo1"], need_lo["start_lo2"], c=need_lo_pred)
        plt.text (.99, .01, ('MBKM h=%d k=%d, score: %.2f' % (h, 20, score)), transform=plt.gca ().transAxes, size=10,
              horizontalalignment='right')
    plt.show ()
    '''