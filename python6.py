
# Campus Event Financial Planning

venue = 5000
equipment = 3000
catering = 10000
transport = 2000
certificates = 1000

sponsorship = 5000
fee = 200
cost_per_student = 100

total_cost = venue + equipment + catering + transport + certificates
remaining_cost = total_cost - sponsorship

print("Total Event Cost: Rs.", total_cost)
print("Sponsorship: Rs.", sponsorship)
print("Remaining Cost: Rs.", remaining_cost)

participants = int(input("Enter number of participants: "))

contributions = participants * fee
total_expense = total_cost + participants * cost_per_student

print("Participant Contributions: Rs.", contributions)

if contributions + sponsorship >= total_expense:
    print("Event is within budget!")
else:
    print("Additional Sponsorship Needed: Rs.",
          total_expense - contributions - sponsorship)

# Calculate minimum registrations to break even
if fee > cost_per_student:
    minimum = (total_cost - sponsorship) // (fee - cost_per_student) + 1
    print("Minimum Registrations Needed:", minimum)
else:
    print("Registration fee must exceed cost per student.")
