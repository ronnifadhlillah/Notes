import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from statsmodels.tsa.holtwinters import ExponentialSmoothing

geoLocator=Nominatim(user_agent="user_app")
location=geoLocator.geocode("Cilegon")

params = {
    "latitude": location.latitude,
    "longitude": location.longitude,
    "start_date": "2026-08-01",
    "end_date": "2026-08-31",
    "daily": "temperature_2m_mean"
}
getHistorical=requests.get("https://archive-api.open-meteo.com/v1/archive",params=params)
get5DJson=getHistorical.json()
# print(get5DJson)

data={
    "timestamp":get5DJson["daily"]["time"],
    "temp":get5DJson["daily"]["temperature_2m_mean"]
}
df=pd.DataFrame(data)
df["timestamp"] = pd.to_datetime(df["timestamp"])
# mod=ExponentialSmoothing(
#     df["temp"],
#     trend="add",
#     seasonal=None,
#     initialization_method="estimated"
#     )

mod=ExponentialSmoothing(
    df["temp"],
    trend="add",
    seasonal="mul",
    damped_trend=True,
    seasonal_periods=7,
    initialization_method="estimated"
    )

modFit=mod.fit()
predict=modFit.forecast(steps=30)
# for i, pred in enumerate(predict,start=1):
#     print(i,pred)
    
future_dates = pd.date_range(
start=df["timestamp"].iloc[-1] + pd.Timedelta(days=1), 
periods=30
)

forecast=[]
for date, pred in zip(future_dates, predict):
    forecast.append({
        "timestamp":pd.to_datetime(date.strftime("%Y-%m-%d")),
        "temp":pred
    })
dfB=pd.DataFrame(forecast)

dfMerge=pd.concat([df,dfB],ignore_index=True)
print(dfMerge)

# Validasi
plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["temp"], label="Data Historis Aktual")
plt.plot(
    dfB["timestamp"], dfB["temp"], label="Prediksi 5 Hari Kedepan", linestyle="--"
)
plt.xlabel("Tanggal")
plt.ylabel("Suhu Rata-rata (°C)")
plt.legend()
plt.grid(True)
plt.show()