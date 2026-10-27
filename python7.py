
# University Admission Decision Engine

students = [
    ["Arun", 85, 80, 90],
    ["Priya", 92, 85, 95],
    ["Rahul", 70, 60, 75],
    ["Sneha", 88, 90, 85]
]

eligible = []

for s in students:
    name = s[0]
    maths = s[1]
    science = s[2]
    english = s[3]

    average = (maths + science + english) / 3

    if maths >= 60 and science >= 60 and average >= 75:
        eligible.append([name, average, maths])

# Rank by average marks, then Mathematics marks
eligible.sort(key=lambda x: (x[1], x[2]), reverse=True)

print("Eligible Students")
print("-----------------")

if len(eligible) == 0:
    print("No eligible students")
else:
    rank = 1
    for s in eligible:
        print(rank, s[0], "- Average:", round(s[1], 2))
        rank += 1
