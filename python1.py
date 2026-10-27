
# Bus Passenger Occupancy Simulation

capacity = 50
passengers = 0

stops = [
    ("Stop 1", 20, 0),
    ("Stop 2", 15, 5),
    ("Stop 3", 10, 8),
    ("Stop 4", 12, 10),
    ("Stop 5", 5, 7)
]

print("BUS PASSENGER OCCUPANCY SIMULATION")
print("-" * 45)

for stop, boarding, alighting in stops:
    passengers -= alighting
    passengers += boarding

    print(f"\n{stop}")
    print("Passengers boarded:", boarding)
    print("Passengers alighted:", alighting)
    print("Current passengers:", passengers)

    if passengers > capacity:
        print("WARNING: Bus capacity exceeded!")
    else:
        print("Status: Within capacity")

print("\nSimulation completed!")
