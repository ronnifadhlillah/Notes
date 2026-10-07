from prophet.diagnostics import cross_validation, performance_metrics
import pandas as pd
import Prophet
import openpyxl

df=pd.read_csv("../../DATASET/real_world_sales_dataset_5000.csv", header=0)
df["Order_Date"] = pd.to_datetime(df["Order_Date"], format="%d-%m-%y")
dfA=df.groupby(pd.Grouper(key="Order_Date", freq="MS"))["Profit"].sum().reset_index()
dfA=dfA.rename(columns={"Order_Date": "ds", "Profit": "y"})
m=Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
m.fit(dfA)
df_cv=cross_validation(m, initial='730 days', period='180 days', horizon='365 days')
df_p=performance_metrics(df_cv)
print(df_p[['horizon', 'mae', 'rmse', 'mape']].head())