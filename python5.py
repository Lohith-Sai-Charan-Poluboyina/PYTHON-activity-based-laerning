
# Classroom Occupancy Analysis

classrooms = [
    ["Alice", None, "Reserved", None],
    [None, "Bob", None, "Reserved"],
    ["Charlie", None, None, None]
]

students = ["David", "Eva"]
assigned = []

for room in classrooms:
    for i in range(len(room)):
        if room[i] is None and students:
            room[i] = students.pop(0)

print("Classroom Seating:")

for i, room in enumerate(classrooms):
    print("Classroom", i + 1, ":", room)

# Count occupied and vacant seats
occupied = 0
vacant = 0

for room in classrooms:
    for seat in room:
        if seat is None:
            vacant += 1
        else:
            occupied += 1

print("Occupied Seats:", occupied)
print("Vacant Seats:", vacant)
