# enter a word for the program to check
word = input("Enter a word: ")

# while true, loop the program considering that 'c' is the special case!
while(True):
	if 'c' in word: 
		if word.index('i') < word.index('e') and word.index('e') < word.index('c'):
			print(True);
		elif word.index('c') < word.index('e') and word.index('e') < word.index('i'):
			print(True);
		else:
			print(False);
	else:
		print(True);
	another_word = input('Would you like to enter another word? Enter(y/n)').lower()
	if another_word == 'y':
		word = input('Enter a word: ')
	else:
		print('You chose to quit. Goodbye!')
		break