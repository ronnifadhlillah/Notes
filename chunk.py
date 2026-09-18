import pandas as pd
import time
import memory_profiler import memory_usage

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

# ==================================================================

# Comparation with or wirthout chunk.
# Difference in memory consumption between using chunks and not.

def readWithoutChunk():
  df=pd.read_csv("dataset")
  result=df["open"].sum()
  return result

def readWithChunk():
  result=0
  for chunk in pd.read_csv("dataset",chunksize=chunk_size):
    result+=chunk["open"].sum
  return result

if __name__=="__main__":
  startTime1=time.time()
  memComps1=memory_usage(readWithoutChunk) # memory usage without chunk.
  resTime1=time.time()-startTime1
  print(f"Without chunk -> Max RAM consumption: {max(memComps1):.2f} MB | time: {resTime1:.2f} second")
# ==================================================================
  startTime2=time.time()
  memComps2=memory_usage(readWithChunk) # memory usage chunk.
  resTime2=time.time()-startTime2
  print(f"With chunk -> Max RAM consumption: {max(memComps2):.2f} MB | time: {resTime2:.2f} second")
# ==================================================================
  # Comparation in percent
  compare=(max(memComps2)/max(memComps1))*100
  