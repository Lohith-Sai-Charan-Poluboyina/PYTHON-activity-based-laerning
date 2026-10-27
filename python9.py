
# Retail Billing System

products = [
    ["Shirt", 500, 2, 5],
    ["Shoes", 1000, 1, 12],
    ["Bag", 800, 2, 8]
]

total = 0

print("------ RETAIL INVOICE ------")

for item in products:
    name = item[0]
    price = item[1]
    quantity = item[2]
    tax = item[3]

    amount = price * quantity

    # Apply discount
    if amount >= 1500:
        discount = amount * 0.10
    else:
        discount = amount * 0.05

    # Maximum discount limit
    if discount > 200:
        discount = 200

    amount = amount - discount

    # Calculate category tax
    tax_amount = amount * tax / 100
    final_amount = amount + tax_amount

    total += final_amount

    print("\nProduct:", name)
    print("Quantity:", quantity)
    print("Price:", price)
    print("Discount:", discount)
    print("Tax:", tax_amount)
    print("Total:", final_amount)

print("\n----------------------------")
print("Final Bill: Rs.", round(total, 2))
