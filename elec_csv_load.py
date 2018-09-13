import pandas as pd
import numpy as np

data = pd.read_csv('electric_rates.csv')
states = data.iloc[3:53, 0:2].values

d = dict((x[0], (x[1])) for x in states[1:])

state = "Vermont"

for x in range(len(d)):
    if state in d:
        print(d[state])
        break

print(states)
