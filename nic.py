from datetime import datetime, timedelta

nic = input("Enter NIC: ").strip()

# New NIC (12 digits)
if len(nic) == 12 and nic.isdigit():
    year = int(nic[:4])
    day = int(nic[4:7])

# Old NIC (10 digits ending with V/X)
elif len(nic) >= 5:
    year = 1900 + int(nic[:2])
    day = int(nic[2:5])

else:
    print("Invalid NIC")
    exit()

gender = "Male"
if day > 500:
    gender = "Female"
    day -= 500

# Leap year check
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Your requested adjustment
if is_leap:
    birthday = datetime(year, 1, 1) + timedelta(days=day - 1)
else:
    birthday = datetime(year, 1, 1) + timedelta(days=day - 2)

print("Birthday:", birthday.strftime("%Y-%m-%d"))
print("Gender:", gender)     me code eka linkedin dannada
