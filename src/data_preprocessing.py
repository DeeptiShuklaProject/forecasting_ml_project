import pandas as pd

def load_and_clean_data(file_path):
    # Load the CSV file
    data = pd.read_csv(file_path)
    
    # Convert date columns to datetime
    data['transactionstarttime'] = pd.to_datetime(data['transactionstarttime'], errors='coerce')
    
    # Filter out rows where itemquantity is <= 0
    data = data[data['itemquantity'] > 0]
    
    # Aggregate daily sales
    data['transaction_date'] = data['transactionstarttime'].dt.date
    daily_sales = data.groupby('transaction_date').agg(total_sales=('itemquantity', 'sum')).reset_index()
    
    return daily_sales

if __name__ == "__main__":
    file_path = '../data/restaurant-data.csv'
    daily_sales = load_and_clean_data(file_path)
    daily_sales.to_csv('../data/daily_sales.csv', index=False)
    print("Data preprocessing completed. Cleaned data saved to 'data/daily_sales.csv'.")
