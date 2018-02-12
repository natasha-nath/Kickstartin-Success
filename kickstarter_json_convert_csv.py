import json
import pandas as pd
from pandas.io.json import json_normalize

# =============================================================================
# 
# LOAD JSON FILE
# 
# =============================================================================

path = ''
datapath = path + 'Kickstarter_2018-01.json'
max_records = 1000

output_path = datapath + ".csv"

df = pd.read_json(datapath, lines=True, chunksize=max_records)

# =============================================================================
# 
# CONVERT INTO PANDA DATAFRAME
# 
# =============================================================================

# Kept features
# Name: created_at, dtype: datetime64[ns]
# Name: id, dtype: int64
# Name: data, dtype: object

# Initialize a new dataframe
final_data = pd.DataFrame()
chunkIndex = 0

# Iterate over every chunk in the dataframe
for df_chunk in df:
    print("Starting a new chunk ")
    print(chunkIndex)
    df_chunk = df_chunk['data']
    # For each row in the dataframe, extract the data and write it to a CSV
    for i in range(0, len(df.index)):
        # Necessary data preprocessing
        if(not("slug" in df_chunk.iloc[i]["creator"])):
            df_chunk.iloc[i]["creator"]["slug"] = "N/A"
        # Write the headers for the first row but nothing else
        if(chunkIndex==0 and i==0):
            NewLineOfData = json_normalize(df_chunk.iloc[i]).to_csv(path_or_buf=output_path, mode="a")
            print("Printed headers")
        else:
            NewLineOfData = json_normalize(df_chunk.iloc[i]).to_csv(path_or_buf=output_path, mode="a", header=False)
    chunkIndex += 1


# We can potentially dropped some columns here
# dropped_features = []
# selected_features = []

# final_data is a panda DataFrame with 89 columns
# =============================================================================
# final_data.columns.values
# =============================================================================
