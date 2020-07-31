filename = input('Enter the file name: ')

try:
    filehandle = open(filename)
except:
    print('File cannot be opened: ', filename)
    quit()

total = 0
count = 0
for line in filehandle:
    line = line.rstrip()

    headerText = "X-DSPAM-Confidence:0.232442"
    if line.startswith(headerText):
        numberSubstring = line[len(headerText):]
        try:
            number = float(numberSubstring)
            total += number
            count += 1
        except:
            print("Warning: ", numberSubstring, "is not a float")
            continue

average = total / count
print("Average spam confidence:", average)
