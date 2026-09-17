import pandas as pd

# Process a large CSV file in segments of 50,000 rows
chunk_size = 50000
processed_chunks = []

for chunk in pd.read_csv("../dataset/btcusd_1-min_data.csv", chunksize=chunk_size):
    # Perform filtering or aggregation per chunk
    # filtered_chunk = chunk[chunk["status"] == "active"]
    processed_chunks.append(chunk)

# Combine the processed chunks back into a manageable DataFrame
final_df = pd.concat(processed_chunks, ignore_index=True)
final_df