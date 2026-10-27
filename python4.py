
# Monthly Calendar Generator

days = int(input("Enter number of days in the month (28-31): "))
start = int(input("Enter starting weekday (1=Mon, 7=Sun): "))

print("\nMon Tue Wed Thu Fri Sat Sun")

day = 1

# Print spaces for starting weekday
for i in range(1, start):
    print("    ", end="")

# Generate calendar using nested loops
while day <= days:
    for i in range(start, 8):
        if day <= days:
            print("%3d " % day, end="")
            day += 1
        else:
            break
    print()
    start = 1
