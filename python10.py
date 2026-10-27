
# Manufacturing Cost and Profitability Analysis

material = 5000
labour = 2000
wastage = 500
machine = 1000

selling_price = 12000
profit_target = 3000

total_cost = material + labour + wastage + machine
profit = selling_price - total_cost

print("Material Cost:", material)
print("Labour Charges:", labour)
print("Wastage Cost:", wastage)
print("Machine Cost:", machine)

print("Total Production Cost:", total_cost)
print("Selling Price:", selling_price)
print("Profit:", profit)

if profit >= profit_target:
    print("Profit Target Achieved!")
else:
    print("Profit Target Not Achieved.")
    print("Additional Profit Needed:", profit_target - profit)
