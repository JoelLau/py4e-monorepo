# 8.5
# Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line
# (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
# You can download the sample data at https://www.py4e.com/code3/mbox-short.txt

# Sub-procedures

def promptGetFilename():
    return input('Enter file name: ')


def getFileContents(filename):
    fileContents = list()

    try:
        filehandle = open(filename)
    except:
        print('ERROR! There was a problem opening the file at:', filename)
        quit()

    for line in filehandle:
        line = line.rstrip()
        fileContents.append(line)

    return fileContents


def getLinesThatStartsWithFrom(lines):
    linesThatStartWithFrom = list()

    for line in lines:
        if line.startswith('From '):
            linesThatStartWithFrom.append(line)

    return linesThatStartWithFrom


def mapFromLinesToEmailAddresses(linesThatStartWithFrom):
    emailAddresses = list()

    for line in linesThatStartWithFrom:
        emailAddress = getEmailAddressFromLine(line)
        emailAddresses.append(emailAddress)

    return emailAddresses


def getEmailAddressFromLine(line):
    tokens = line.split(' ')
    emailAddress = tokens[1]
    return emailAddress


def printStringList(stringList):
    for element in stringList:
        print(element)


def printFromLinesSummary(linesThatStartWithFrom):
    count = len(linesThatStartWithFrom)
    print('There were', count, 'lines in the file with From as the first word')


# Main procedure


def main():
    filename = promptGetFilename()
    fileContents = getFileContents(filename)
    linesThatStartWithFrom = getLinesThatStartsWithFrom(fileContents)
    senderEmailAddresses = mapFromLinesToEmailAddresses(linesThatStartWithFrom)

    printStringList(senderEmailAddresses)
    printFromLinesSummary(linesThatStartWithFrom)

    return 0


# Run Main


main()
