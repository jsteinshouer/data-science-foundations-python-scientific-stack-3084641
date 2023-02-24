"""
- Load the taxi data.
- Remove all rows with either total_amount <= 0 or
  passenger_count == 0
- Create a bar chart of average tip % per passenger_count
- Create a bar chart of average tip % per day of week
"""


# %%
# Load the taxi data.
import pandas as pd

time_cols = [
    'tpep_pickup_datetime',
    'tpep_dropoff_datetime',
]
df = pd.read_csv(
    'taxi.csv',
    parse_dates=time_cols,
)
df

# %%
# Remove all rows with either total_amount <= 0 or passenger_count == 0
# df = df.drop(df[df.total_amount <= 0].index)
# df = df.drop(df[df.passenger_count == 0].index)
df = df[df.total_amount > 0]
df = df[df.passenger_count != 0]
df

# %%
# Add tip percent

df['tip_percent'] = df['tip_amount'] / df['fare_amount'] * 100
df['tip_percent']
# %%
# Create a bar chart of average tip % per passenger_count

tip_df = (
    df
    .groupby(['passenger_count'], as_index=False)
    ['tip_percent']
    .median()
)
tip_df

# tip_df['tip_index'] = 0;
# tip_df.pivot(
#     columns='passenger_count',
#     index='tip_index',
#     values='tip_percent'
# ).plot.bar(rot=0)

tip_df.plot.bar(x='passenger_count', y='tip_percent')
# %%
# Create a bar chart of average tip % per day of week
df['day'] = df['tpep_pickup_datetime'].dt.day_name()
df_by_day = (
    df
    .groupby(['day'], as_index=False)
    ['tip_percent']
    .median()
)
# df_by_day
df_by_day.plot.bar(x='day', y='tip_percent')
# %%
