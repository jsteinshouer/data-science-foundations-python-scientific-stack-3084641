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
# Create a bar chart of average tip % per passenger_count


