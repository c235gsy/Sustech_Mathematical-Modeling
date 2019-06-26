import pandas as pd
t1 = 5
t2 = 10
data = pd.DataFrame({"end_t": [0,1,6,0,7,11],
                     "start_t": [3,7,12,15,8,13]})

out = data.loc[((data["end_t"] > t1) & (t1 > data["start_t"])) |
                    ((data["start_t"] < t2) & (t2 < data["end_t"])) |
                    ((data["start_t"] >= t1) & (data["end_t"] <= t2))]

print(out)