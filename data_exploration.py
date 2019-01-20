#data
import pandas as pd
raw_wine_data = "wine_raw_data.csv"

raw_wine_data_df = pd.read_csv(raw_wine_data)
raw_wine_data_df.head()