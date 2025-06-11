import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250605.csv")

fur_color = squirrel_data['Primary Fur Color'].dropna().unique().tolist()
fur_color_count = squirrel_data["Primary Fur Color"].value_counts().to_list()
print(fur_color, fur_color_count)
df = pd.DataFrame({'Primary Fur Color':fur_color, 'Count':fur_color_count})

df.to_csv('output.csv', index= True)
