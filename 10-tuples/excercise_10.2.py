# 10.2
# Write a program to read through the mbox-short.txt and
# figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and
# then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.

# Sub-procedures

def getFilename() -> str:
    return 'mbox-short.txt'


def getSendersFromFile(filename):
    return open(filename)


def getEmailAddressFromLine(line):
    tokens = line.split(' ')
    emailAddress = tokens[1]
    return emailAddress


# Main procedure


def main():
    filename: str = getFilename()
    filehandle = open(filename)

    senderEmailAddresses = [getEmailAddressFromLine(
        line.rstrip()) for line in filehandle if line.startswith('From: ')]

    print(senderEmailAddresses)

    return 0


# Run Main
main()
