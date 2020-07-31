score = input("Enter Score: ")

try:
    score = float(score)
except:
    print("that wasn't a number")

if score > 1.0:
    print("out of range - score must be between 0.0 and 1.0")
if score < 0.0:
    print("out of range - score must be between 0.0 and 1.0")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("B")
elif score >= 0.6:
    print("D")
else:  # score < 0.6
    print("F")
