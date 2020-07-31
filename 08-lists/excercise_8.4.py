# Excercise 8.4
# Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.

filename = 'romeo.txt'

try:
    filehandle = open(filename)
except:
    print('File cannot be opened: ', filename)
    quit()

uniqueWords = list()
for line in filehandle:
    line = line.rstrip()
    for word in line.split(' '):
        word = word.rstrip()
        if (word not in uniqueWords):
            uniqueWords.append(word)

print(sorted(uniqueWords))
