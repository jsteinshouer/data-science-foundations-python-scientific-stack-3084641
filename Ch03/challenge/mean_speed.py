# What is the mean speed (mile/hour) in taxi.parquet?

# - Run download_data.py to download the data

# %%
import pandas as pd
import numpy as np

parquet_file = 'taxi.parquet'
df = pd.read_parquet(parquet_file)

# df = pd.read_parquet(parquet_file, parse_dates=['tpep_pickup_datetime','tpep_dropoff_datetime'])
len(df)
# %%
df.columns
# %%
df.info()
# %%
df.describe()

# %%
df[0:10]

# %%
df["travel_time"] = (df["tpep_dropoff_datetime"] -
                     df["tpep_pickup_datetime"]) / pd.Timedelta(1, 'hour')
travel_time_hours = (df["tpep_dropoff_datetime"] -
                     df["tpep_pickup_datetime"]) / pd.Timedelta(1, 'hour')

# %%
speed = df["trip_distance"] / travel_time_hours

# %%
speed = speed.replace(np.inf, np.nan)
speed.mean()  # 17.093514389056462

# I came up with roughly the same answer but he used
# this to remove lines with bad data

# mask = df['tpep_dropoff_datetime'] > df['tpep_pickup_datetime']
# df = df[mask]
# %%
speed.describe()
# %%
