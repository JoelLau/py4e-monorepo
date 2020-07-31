def computepay(hoursWorked, ratePerHour):
    expectedHours = 40.0
    overtimeMultiplier = 1.5

    totalPay = 0

    if hoursWorked > expectedHours:
        regularPay = expectedHours * ratePerHour

        overtimeHours = hoursWorked - expectedHours
        overtimePay = overtimeHours * (overtimeMultiplier * ratePerHour)

        totalPay = regularPay + overtimePay
    else:
        totalPay = hoursWorked * ratePerHour

    return totalPay


# Hours Worked - input, prompt, validation

inputHoursWorked = input("Enter Hours:")

try:
    hoursWorked = float(inputHoursWorked)
except:
    print("that's not a number")

if hoursWorked < 0.0:
    print("cannot be negative")


# Hours Worked - input, prompt, validation

inputRatePerHour = input("Enter Rate per Hour:")

try:
    ratePerHour = float(inputRatePerHour)
except:
    print("that's not a number")

if ratePerHour < 0.0:
    print("cannot be negative")


# Calculation

pay = computepay(hoursWorked, ratePerHour)


# Output
print("Pay", pay)
