'''
ref: 
1. https://towardsdatascience.com/finding-seasonal-trends-in-time-series-data-with-python-ce10c37aa861
2. https://machinelearningmastery.com/time-series-seasonality-with-python/


Y[t]: Our time-series function
T[t]: Trend (general tendency to move up or down)
S[t]: Seasonality (repeating patterns / cyclic pattern occurring at regular intervals)
e[t]: Residual (random noise in the data that isn’t accounted for in the trend or seasonality

1. two types of seasonality - Additive vs Multiplicative Seasonality
    - Additive Seasonality: the amplitude of our seasonality tends to remain the same 
        - Y[t] = T[t] + S[t] + e[t]
    - Multiplicative Seasonality: the amplitude of our seasonality becomes larger or smaller based on the trend.
        - Y[t] = T[t] *S[t] *e[t]

2. Benefits to Machine Learning for understanding seasonality
    - Clearer Signal @ Data processing: Identifying and removing the seasonal component from the time series can result in a clearer relationship between input and output variables. 
        - Modeling seasonality and removing it from the time series may occur during data cleaning and preparation.
    - More Information @ Feature Engineering: Additional information about the seasonal component of the time series can provide new information to improve model performance.
        - Extracting seasonal information and providing it as input features, either directly or in summary form, may occur during feature extraction and feature engineering activities.


3. Removing Seasonality: 
    - The model of seasonality can be removed from the time series. This process is called Seasonal Adjustment, or Deseasonalizing.
    - A time series where the seasonal component has been removed is called seasonal stationary. A time series with a clear seasonal component is referred to as non-stationary.

'''
