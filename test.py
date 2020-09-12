import re
fhand = open('regex_sum_570929.txt')
text = ''
total = 0

for i in fhand:
    line = i.strip()
    text = text + ' ' + line
numbers = re.findall('[0-9]+', text)

for k in range(0, len(numbers)):
    floats = float(numbers[k])
    total = floats + total

print(total)
