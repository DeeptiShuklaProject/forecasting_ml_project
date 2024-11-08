import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

def forecast_sales(daily_sales):
    # Prepare data for Prophet
    daily_sales.rename(columns={'transaction_date': 'ds', 'total_sales': 'y'}, inplace=True)
    
    # Initialize and fit the model
    model = Prophet()
    model.fit(daily_sales)
    
    # Forecast the next 30 days
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    
    # Plot forecast
    model.plot(forecast)
    plt.title('30-Day Sales Forecast')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.savefig('../reports/sales_forecast.png')
    return forecast

if __name__ == "__main__":
    daily_sales = pd.read_csv('../data/daily_sales.csv', parse_dates=['transaction_date'])
    forecast = forecast_sales(daily_sales)
    forecast.to_csv('../data/forecasted_sales.csv', index=False)
    print("Forecasting completed. Forecast saved to 'data/forecasted_sales.csv'.")
