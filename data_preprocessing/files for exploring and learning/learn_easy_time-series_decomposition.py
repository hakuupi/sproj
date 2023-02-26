'''Following the 'Time Series Decomposition In Python' tutorial at:
https://towardsdatascience.com/time-series-decomposition-in-python-8acac385a5b2'''

#----


'''Time series decomposition is a technique that splits a time series into several components, each representing an underlying pattern category, trend, seasonality, and noise. In this tutorial, we will show you how to automatically decompose a time series with Python.

To begin with, let's talk a bit about the components of a time series:

Seasonality: describes the periodic signal in your time series.
Trend: describes whether the time series is decreasing, constant, or increasing over time.
Noise: describes what remains behind the separation of seasonality and trend from the time series. In other words, it’s the variability in the data that cannot be explained by the model.

For this example, we will use the Air Passengers Data from Kaggle.'''

import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
 
#https://www.kaggle.com/rakannimer/air-passengers
df=pd.read_csv('/Users/HAQbook/Documents/GitHub/sproj/data_files/AirPassengers.csv')
 
print(df.head())