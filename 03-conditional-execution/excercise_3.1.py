# This first line is provided for you

# "CONSTANTS"
EXPECTED_HOURS_WORKED = 40.0
OVERTIME_MULTIPLIER = 1.5

# Input
totalHoursWorked = input("Enter Hours:")
ratePerHour = input("Enter Rate per hour:")

# Type conversion
totalHoursWorked = float(totalHoursWorked)
ratePerHour = float(ratePerHour)

# Calculation
pay = 0.0

if (totalHoursWorked > EXPECTED_HOURS_WORKED):
    # normal hours
    pay = pay + (EXPECTED_HOURS_WORKED * ratePerHour)

    # overtime details
    overtimeHours = totalHoursWorked - EXPECTED_HOURS_WORKED
    overtimeRatePerHour = ratePerHour * OVERTIME_MULTIPLIER

    # overtime hours
    pay = pay + (overtimeHours * overtimeRatePerHour)

else:
    pay = pay + (totalHoursWorked * ratePerHour)

print('Pay: ' + str(pay))
