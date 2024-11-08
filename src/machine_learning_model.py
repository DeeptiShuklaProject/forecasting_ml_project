# src/machine_learning_model.py
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load preprocessed data
data = pd.read_csv('../data/daily_sales.csv', parse_dates=['transaction_date'])

# Debugging: Print the columns of the dataset
print("Columns in the dataset:", data.columns)

# Feature engineering
data['day_of_week'] = data['transaction_date'].dt.dayofweek
data['week_of_year'] = data['transaction_date'].dt.isocalendar().week
data['month'] = data['transaction_date'].dt.month

# Prepare features and target variable
X = data[['day_of_week', 'week_of_year', 'month']]  # Features based on transaction_date
y = data['total_sales']  # Target variable is total_sales

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate RMSE (Root Mean Squared Error)
rmse = mean_squared_error(y_test, y_pred, squared=False)  # Set squared=False for RMSE directly
print(f'RMSE: {rmse}')

# Feature importance plot
feature_importances = model.feature_importances_
features = X.columns

plt.figure(figsize=(10, 6))
plt.barh(features, feature_importances, color='skyblue')
plt.xlabel('Feature Importance')
plt.title('Feature Importance of Random Forest Model')
plt.savefig('../reports/feature_importance.png')
plt.show()
