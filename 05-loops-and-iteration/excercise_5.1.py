largest = None
smallest = None

while True:
    # Input / prompt
    num = input("Enter a number: ")

    # Input Validation (1)
    if num == "done":
        break
s  
    # Input Validation (2)
    try:
        num = int(num)  # type casting
    except:
        print('Invalid input')
        continue

    # Check if largest
    if largest is None:
        largest = num
    elif num > largest:
        largest = num

    # Check if smallest
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
