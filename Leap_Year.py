# Name: Shammahlon T. Evasco
# ID: 26-4144-869
# Activity: Leap Year Determination Program
# Date: October 3, 2026

# Program to determine if a year is a Leap Year or Not

year = int(input("Enter a year: "))

# Leap Year Logic:
# A year is a Leap Year if:
# 1. It is divisible by 400, OR
# 2. It is divisible by 4 AND NOT divisible by 100

if year % 400 == 0:
    result = "a Leap Year"
elif year % 100 == 0:
    result = "Not a Leap Year"
elif year % 4 == 0:
    result = "a Leap Year"
else:
    result = "Not a Leap Year"

print("Year" + str(year) + " is " str(result)")
