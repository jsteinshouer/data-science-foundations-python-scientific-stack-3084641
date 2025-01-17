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

df['tip_percent'] = df['tip_amount'] / df['total_amount'] * 100
df['tip_percent']
# %%
# Create a bar chart of average tip % per passenger_count

df_by_count = (
    df
    .groupby(['passenger_count'], as_index=False)
    ['tip_percent']
    .mean()
)

ny_chart = df_by_count.plot.bar(x='passenger_count', y='tip_percent')
ny_chart.set_ylabel('Tip %')
ny_chart.set_xlabel('Passenger Count')
# %%
# Create a bar chart of average tip % per day of week
df['day'] = df['tpep_pickup_datetime'].dt.day_name()
df['dayofweek'] = df['tpep_pickup_datetime'].dt.dayofweek

df_by_day = (
    df
    .groupby(['dayofweek', 'day'], as_index=False)
    ['tip_percent']
    .mean()
)
# df_by_day
df_by_day.plot.bar(x='day', y='tip_percent')
# %%
