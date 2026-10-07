import pandas as pd
import openpyxl
import Prophet

df=pd.read_csv('https://raw.githubusercontent.com/facebook/prophet/main/examples/example_yosemite_temps.csv')
m=Prophet(changepoint_prior_scale=0.01).fit(df)
future=m.make_future_dataframe(periods=300, freq='H')
fcst=m.predict(future)
fig=m.plot(fcst)
fig=m.plot_components(fcst)