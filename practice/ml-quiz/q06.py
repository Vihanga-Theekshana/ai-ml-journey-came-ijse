import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Load the dataset
df = pd.read_csv("house_prices.csv")

# Define features (X) and target (y)
X = df[['size_sqft', 'rooms', 'age_years', 'distance_km']]
y = df['price_lkr_mn']

# Train-test split (exactly as instructed)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# a) Fit LinearRegression & Report Intercept + Coefficients
# ==========================================
model = LinearRegression()
model.fit(X_train, y_train)

# Print intercept and the four coefficients (not as an array)
print(f"{model.intercept_:.4f}", 
      f"{model.coef_[0]:.4f}", 
      f"{model.coef_[1]:.4f}", 
      f"{model.coef_[2]:.4f}", 
      f"{model.coef_[3]:.4f}")

# ==========================================
# b) Report MAE, RMSE, and R2 on the test set
# ==========================================
y_test_pred = model.predict(X_test)

mae = metrics.mean_absolute_error(y_test, y_test_pred)
rmse = metrics.root_mean_squared_error(y_test, y_test_pred)
r2 = metrics.r2_score(y_test, y_test_pred)

print(f"{mae:.4f}", f"{rmse:.4f}", f"{r2:.4f}")

# ==========================================
# c) Predict price for the new house
# ==========================================
new_house = pd.DataFrame({
    'size_sqft': [1800], 
    'rooms': [3], 
    'age_years': [12], 
    'distance_km': [8]
})

pred_price = model.predict(new_house)[0]

print(f"{pred_price:.4f}")