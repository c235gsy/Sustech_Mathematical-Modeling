import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

for d in range(1,31):
    mark = "0"
    if d >= 10:
        mark = str(d)
    else:
        mark = mark+str(d)

    gps = pd.read_csv("./data/gps_201611"+mark, header=None, usecols=[0,1])
    gps.columns = ["driver","order"]
    gps = gps.drop_duplicates(subset=["order"], keep="last")
    gps = gps.reset_index(drop=True)
    print(len(gps))
    gps.to_csv('./data/driver_to_order_11_'+mark+'.csv',index=0)


