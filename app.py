import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Step 1: Create DataFrames

# Customers DataFrame
customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5],
    'customer_name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'country': ['USA', 'Canada', 'USA', 'Canada', 'USA']
})

# Orders DataFrame
orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105],
    'customer_id': [1, 2, 3, 1, 4],
    'product_id': [1001, 1002, 1003, 1004, 1001],
    'order_date': [datetime.now() - timedelta(days=i*30) for i in range(5)],
    'quantity': [2, 1, 5, 3, 2]
})

# Products DataFrame
products = pd.DataFrame({
    'product_id': [1001, 1002, 1003, 1004],
    'product_name': ['Laptop', 'Phone', 'Tablet', 'Monitor'],
    'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics'],
    'price': [1000, 800, 600, 300]
})

# Step 2: Transformations and Joins

# Calculate total sales amount for each order
orders['total_amount'] = orders['quantity'] * orders['product_id'].map(products.set_index('product_id')['price'])

# Join orders with customers to get customer details
orders_with_customers = pd.merge(orders, customers, on='customer_id', how='left')

# Display the result
print("Orders with Customer Details and Total Amount:")
print(orders_with_customers)