import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
from prophet import Prophet

df=pd.read_csv("../../DATASET/real_world_sales_dataset_5000.csv",header=0)

df["Order_Date"]=pd.to_datetime(df["Order_Date"],format="%d-%m-%y").dt.to_period("M").dt.to_timestamp()
dfA=df.groupby(["Order_Date"])["Profit"].sum()
dfA=dfA.reset_index()

dfA = dfA.rename(columns={"Order_Date": "ds", "Profit": "y"})

m=Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False
)
m.fit(dfA)
ftr=m.make_future_dataframe(periods=5)
frcst=m.predict(ftr)

print(frcst[["ds","yhat","yhat_upper","yhat_lower"]].tail())

# fig1 = m.plot(frcst)
# fig2 = m.plot_components(frcst)