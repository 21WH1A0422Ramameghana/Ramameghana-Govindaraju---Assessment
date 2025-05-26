inventory = [
    ["Strawberry", "Fruit", 3.50, 40, 10],
    ["Broccoli", "Vegetable", 2.20, 25, 8],
    ["Cheddar", "Dairy", 5.00, 18, 4],
    ["Baguette", "Bakery", 2.80, 35, 2],
    ["Blueberry", "Fruit", 4.00, 22, 6],
    ["Spinach", "Vegetable", 1.80, 30, 12],
    ["Yogurt", "Dairy", 1.20, 50, 15],
    ["Croissant", "Bakery", 3.00, 28, 3],
]

#Q1: Calculate the TotalRevenue
total_revenue = 0
for i in inventory:
    price = i[2]
    sold = i[3]
    total_revenue += price * sold
print(f"Total Revenue: {total_revenue}")

#Q2: List Low stock item if stock is less than 5
low_stock = []
for i in inventory:
    if i[4] < 5:
        low_stock.append(i[0])
print(low_stock)

#Q3: Calculate category wise revenue
category_revenue = {}
for i in inventory:
    category = i[1]
    price = i[2]
    sold = i[3]
    revenue = price * sold
    if category not in category_revenue:
        category_revenue[category] = 0
    category_revenue[category] += revenue
print("Category-wise Revenue:")
for category, revenue in category_revenue.items():
    print(f"{category}: {revenue}")
