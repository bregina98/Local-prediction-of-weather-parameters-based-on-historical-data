# LOCAL PREDICTION OF WEATHER PARAMETERS BASED ON HISTORICAL DATA


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dateutil import parser

# Uvoz podatkov in vizualizacija dela podatkov

params = ['AMBIENT_TEMPERATURE', 'AIR_PRESSURE', 'WIND_SPEED', 'SOLAR_RADIATION_INTENSITY']

station_id = 5001
data = pd.read_csv(f'ELES-MAS-{station_id}-2020-2023.csv.gz', compression='gzip')
data = data[data['data_validity'] <= 32]
data.head()

for param in params:
    param_data = data[data['parameter_type'] == param]
    times = [parser.parse(time) for time in param_data['acquisition_timestamp']]
    
    fig, ax = plt.subplots(1,1, figsize=(17, 10))
    ax.scatter(times, param_data['value'], s=1)
    ax.set_ylabel(param)
    ax.set_title(f'station_id = {station_id}')

    


