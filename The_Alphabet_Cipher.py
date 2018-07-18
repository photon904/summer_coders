# take in a message
message = input("Enter message: ").lower()

# take in original keyword
original_keyword = input("Enter keyword: ")

# replace variable to append the original keyword to match the length of msg
keyword = ''

# create variable for encryption
encryption = None

# pad keyword until it's the same length as message
# ASSUME msg is always longer than keyword
# remember to slice incase padding exceeds the length of message.
# if that is the case, slice the end of string -- *while* it's longer!!
while len(keyword) < len(message):
	keyword += original_keyword
	if len(keyword) > len(message):
		while len(keyword) > len(message):
			keyword = keyword[:-1]

print(keyword)
print(message)

for a in range(0, (len(message))):
    char = chr(((ord(message[a]) + ord(keyword[a]) - 194) % 26) + 97)
    print(char, sep='', end='')