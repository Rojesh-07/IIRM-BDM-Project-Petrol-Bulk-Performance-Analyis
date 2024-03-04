import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error


df= pd.read_excel('Petrol1.xlsx')

df_arima = df[['Date', 'Sales']].set_index('Date')

train_size = int(len(df_arima) * 0.5)
train, test = df_arima.iloc[:train_size], df_arima.iloc[train_size:]
# 9 1 7
order = (8, 2, 8)  # Example order, you may need to tune this
model = ARIMA(train, order=order, exog=None, seasonal_order=(0, 0, 0, 0), trend=None, enforce_stationarity=True, enforce_invertibility=True, concentrate_scale=False, trend_offset=1, dates=None, freq=None, missing='none', validate_specification=True)
model_fit = model.fit()
# class statsmodels.tsa.arima.model.ARIMA(endog, exog=None, seasonal_order=(0, 0, 0, 0), trend=None, enforce_stationarity=True, enforce_invertibility=True, concentrate_scale=False, trend_offset=1, dates=None, freq=None, missing='none', validate_specification=True)
forecast= model_fit.forecast(steps=len(test))

plt.plot(test.index, test, label='Actual')
plt.plot(test.index, forecast, label='Forecast')
plt.legend()
plt.show()


mae = mean_absolute_error(test, forecast)
print(f'Mean Absolute Error: {mae}')

# import itertools

# # Define a range of values for p, d, and q
# p_values = range(0, 10)
# d_values = range(0, 10)
# q_values = range(0, 10)

# # Generate all possible combinations of p, d, and q
# combinations = list(itertools.product(p_values, d_values, q_values))

# # Evaluate each combination using a validation set
# best_mae = float('inf')
# best_order = None

# for order in combinations:
#     try:
#         model = ARIMA(train, order=order)
#         model_fit = model.fit()
#         forecast = model_fit.forecast(steps=len(test))
#         mae = mean_absolute_error(test, forecast)
        
#         if mae < best_mae:
#             best_mae = mae
#             best_order = order
#     except:
#         continue

# print(f'Best Order: {best_order}')
# print(f'Best Mean Absolute Error: {best_mae}')