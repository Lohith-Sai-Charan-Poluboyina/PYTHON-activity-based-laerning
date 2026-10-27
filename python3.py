
students = [
    ["Arun", 85, 80, 90],
    ["Priya", 92, 85, 95],
    ["Rahul", 70, 60, 75],
    ["Sneha", 88, 90, 85]
]

print("Eligible Students:")

eligible = []

for s in students:
    name = s[0]
    maths = s[1]
    science = s[2]
    english = s[3]

    total = maths + science + english
    average = total / 3

    if maths >= 60 and science >= 60 and average >= 75:
        eligible.append([name, average])

# Rank by average marks (highest first)
eligible.sort(key=lambda x: x[1], reverse=True)

print("\nAdmission Ranking:")

rank = 1

for student in eligible:
    print(rank, student[0], "- Average:", student[1])
    rank += 1

if len(eligible) == 0:
    print("No students are eligible for admission.")
