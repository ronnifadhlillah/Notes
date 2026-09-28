import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

df = pd.read_csv('https://raw.githubusercontent.com/facebook/prophet/main/examples/example_wp_log_peyton_manning.csv')
# print(df.isnull().sum())
m=Prophet()
m.fit(df)

future=m.make_future_dataframe(periods=365)
forecast=m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
# fig1=m.plot(forecast)
# fig2 = m.plot_components(forecast)

# print(forecast)
# print(forecast[["ds","yhat"]])
forecast['ds'] = pd.to_datetime(forecast['ds'])
is_above_2016 = forecast['ds'].dt.year > 2016
forecast_above = forecast[is_above_2016]
forecast_base = forecast[~is_above_2016]

plt.figure(figsize=(10, 5))
plt.plot(forecast_base['ds'], forecast_base['trend'], color='#0072B2', label='Trend')
plt.plot(forecast_above['ds'], forecast_above['trend'],linewidth=2.5, color='#CC79A7', label='Trend')
plt.fill_between(
    forecast['ds'], 
    forecast['trend_lower'], 
    forecast['trend_upper'], 
    color='#555555', 
    alpha=0.2, 
    label='Uncertainty Interval'
)
plt.xlabel('ds')
plt.ylabel('trend')
plt.grid(False, linestyle='-', alpha=0.3)
plt.xlim(forecast['ds'].min(), forecast['ds'].max())
plt.legend(loc='upper left')
plt.show()

# GAP counting
forecast['trendGap'] = forecast['trend_upper'] - forecast['trend_lower']
# first data (head) VS end data (tail)
print("GAP on start periode (2008):", forecast['trendGap'].head(1).values[0])
print("GAP on last periode (prediction) (2017):", forecast['trendGap'].tail(1).values[0])