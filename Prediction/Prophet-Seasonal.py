import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error

df=pd.read_csv("../../DATASET/real_world_sales_dataset_5000.csv",header=0)

df["Order_Date"]=pd.to_datetime(df["Order_Date"],format="%d-%m-%y") # .dt.to_period("M").dt.to_timestamp()
# dfA=df.groupby(["Order_Date"])["Profit"].sum()
dfA=df.groupby(pd.Grouper(key="Order_date",freq="MS"))["Profit"].sum()
dfA=dfA.reset_index()

dfA = dfA.rename(columns={"Order_Date": "ds", "Profit": "y"})

m=Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False
)
m.fit(dfA)
ftr=m.make_future_dataframe(periods=12,freq="MS")
frcst=m.predict(ftr)

print(frcst[["ds","yhat","yhat_upper","yhat_lower"]].tail())
fig1 = m.plot(frcst)
plt.title("Year profit prediction")
plt.show()

# Accuration Test
train_df=dfA.iloc[:-12].copy()
test_df=dfA.iloc[-12:].copy()

preds=frcst.tail(12)['yhat'].values
actuals=test_df['y'].values

mae=mean_absolute_error(actuals,preds)
rmse=np.sqrt(mean_squared_error(actuals,preds))
mape=np.mean(np.abs((actuals-preds)/actuals)) * 100

print(f"MAE  (Mean absolute error) : {mae:,.2f}")
print(f"RMSE (Root mean squared error) : {rmse:,.2f}")
print(f"MAPE (Mean absolute percentage error) : {mape:.2f}%")

fig1=m.plot(frcst)
plt.title("Year Profit Prediction & Accuracy Test")
plt.show()

# Result
# MAE  (Mean absolute error) : 189,541.90
# RMSE (Root mean squared error) : 237,543.70
# MAPE (Mean absolute percentage error) : 81.90%