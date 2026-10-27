
budget = 1000

products = {
    "Shirt": [300, 2],
    "Shoes": [500, 1],
    "Bag": [200, 2],
    "Watch": [400, 1]
}

total = 0

print("Shopping Bill")
print("----------------")

for name, details in products.items():
    price = details[0]
    quantity = details[1]
    cost = price * quantity

    if quantity >= 2:
        cost = cost * 0.90  # 10% discount

    products[name].append(cost)
    total += cost

    print(name, "- Rs.", cost)

print("----------------")
print("Total Amount: Rs.", total)
print("Budget: Rs.", budget)

if total <= budget:
    print("Shopping is within budget!")
else:
    print("Budget exceeded by Rs.", total - budget)

    for name, details in products.items():
        if total > budget and details[1] > 0:
            print("Reduce quantity of:", name)
            total -= details[0]
            details[1] -= 1

    print("Final Amount: Rs.", total)
    print("Remaining Budget: Rs.", budget - total)
