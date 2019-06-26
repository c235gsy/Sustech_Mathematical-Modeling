import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (45.0, 20.0)


def get_data_of_hour(data,hour):
    return data[data['hour'].isin([hour])]


color = {"demand":"blue",
         "distribute": "red",
         "money" : "yellow",
         "response" : "pink",
         "satisfy" : "purple"}


def show_datas(city,day,commends):

    for i in range(0,24):
        plt.subplot(4,6,1+i)
        for c in commends:
            path = city + "/" + c + "_2016.08." + day + "_510100_.csv"
            need = pd.read_csv (path)
            sub = get_data_of_hour(need, i)

            volume = 1*sub["value"]
            plt.scatter(sub["longitude"], sub["latitude"],c=color[c], s=volume, alpha=0.3)

        plt.legend(commends)

        plt.xlabel("longitude", fontsize=15)
        plt.ylabel("latitude", fontsize=15)
        plt.title("hour="+str(i))
        plt.grid (color='black', linestyle='--')
        plt.axis ([103.5, 104.5, 30.5, 31.25])

    plt.tight_layout()
    plt.show()


show_datas("chengdu","09",["demand","money","demand","response","satisfy"])