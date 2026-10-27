
# Student Email and ID Validation

email = input("Enter student email: ")
reg_id = input("Enter registration ID: ")

# Email validation
if "@" in email and "." in email and email.index("@") < email.rindex("."):
    print("Valid email")
else:
    print("Invalid email")

# Registration ID validation
if reg_id.startswith("STU") and reg_id[3:].isdigit() and len(reg_id) == 7:
    print("Valid registration ID")
else:
    print("Invalid registration ID")
