import pandas as pd
import matplotlib.pyplot as plt

def plot_sales(daily_sales):
    # Plot daily sales
    plt.figure(figsize=(14, 6))
    plt.plot(daily_sales['transaction_date'], daily_sales['total_sales'], label='Daily Sales')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.title('Daily Sales Over Time')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.savefig('../reports/daily_sales_plot.png')
    
    # Calculate and plot moving averages
    daily_sales['7_day_MA'] = daily_sales['total_sales'].rolling(window=7).mean()
    daily_sales['30_day_MA'] = daily_sales['total_sales'].rolling(window=30).mean()
    plt.figure(figsize=(14, 6))
    plt.plot(daily_sales['transaction_date'], daily_sales['total_sales'], alpha=0.5, label='Daily Sales')
    plt.plot(daily_sales['transaction_date'], daily_sales['7_day_MA'], label='7-Day MA', color='orange')
    plt.plot(daily_sales['transaction_date'], daily_sales['30_day_MA'], label='30-Day MA', color='red')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.title('Daily Sales with Moving Averages')
    plt.legend()
    plt.grid(True)
    plt.savefig('../reports/moving_averages_plot.png')

if __name__ == "__main__":
    daily_sales = pd.read_csv('../data/daily_sales.csv', parse_dates=['transaction_date'])
    plot_sales(daily_sales)
    print("EDA completed. Plots saved to 'reports' folder.")
