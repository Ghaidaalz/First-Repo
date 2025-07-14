import pandas as pd
import matplotlib.pyplot as plt
# Read the CSV file
data = pd.read_csv('Sales.csv')
# Display the data
print("Sales Data:")
print(data)
###Viz1
# Visualization: plot quantity sold over time
# Convert SaleDate to datetime
data['SaleDate'] = pd.to_datetime(data['SaleDate'], errors='coerce')
# Group by date and sum the quantities
daily_sales = data.groupby('SaleDate')['Quantity'].sum()
# Plot
plt.figure(figsize=(10, 5))
daily_sales.plot(kind='line', marker='o')
plt.title('Quantity of Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Quantity Sold')
plt.grid(True)
plt.tight_layout()

# Show plot
plt.show()

####Viz2
# Get top 5 products by total quantity sold
top_products = data.groupby('ProductID')['Quantity'].sum().nlargest(5).index
# Filter data to include only top 5 products
filtered_data = data[data['ProductID'].isin(top_products)]

# Group by ProductID for total sales (for bar chart)
product_totals = filtered_data.groupby('ProductID')['Quantity'].sum()

# Group by date and product for time trend (for line chart)
trend_data = filtered_data.groupby(['SaleDate', 'ProductID'])['Quantity'].sum().unstack().fillna(0)

# Plot
plt.figure(figsize=(14, 6))

# Bar chart - total sales per product
plt.subplot(1, 2, 1)
product_totals.plot(kind='bar', color='skyblue')
plt.title('Top 5 Most Sold Products')
plt.xlabel('Product ID')
plt.ylabel('Total Quantity Sold')
plt.grid(axis='y')

# Line chart - sales trend over time
plt.subplot(1, 2, 2)
trend_data.plot(marker='o')
plt.title('Sales Trend Over Time (Top 5 Products)')
plt.xlabel('Date')
plt.ylabel('Quantity Sold')
plt.grid(True)
plt.tight_layout()

# Show all plots
plt.show()

###Viz3
# Group by ProductID and sum the Quantity
product_sales = data.groupby('ProductID')['Quantity'].sum()

# Create a pie chart
plt.figure(figsize=(8, 8))
colors = plt.cm.viridis_r(range(len(product_sales)))  # Creative color map
plt.pie(product_sales, labels=product_sales.index, autopct='%1.1f%%', startangle=140, colors=colors)

# Add a title and make it look nice
plt.title('Sales Quantity Distribution by Product', fontsize=14)
plt.axis('equal')  # Make the pie chart a perfect circle
plt.tight_layout()

# Show the plot
plt.show()

###Viz4
plt.figure(figsize=(10,6))

# Scatter plot: ProductID vs CustomerID, bubble size = Quantity sold
plt.scatter(data['ProductID'], data['CustomerID'],
            s=data['Quantity'] * 100,  # bubble size scaled by quantity
            alpha=0.6,
            c='#6a0dad',  # purple color
            edgecolors='black')

plt.xlabel('Product ID')
plt.ylabel('Customer ID')
plt.title('Sales Quantity Bubble Chart', fontsize=16, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()



