# read any input file.
file = input('Enter the filename: ').strip()

# open the file
with open(file, 'r')as f:
	# read it line by line so you can parse the file. 
	f_content1 = f.readline()
	# parse the data
	list1 = f_content1.split(" ")

	# this will automatically choose the seocnd line
	f_content2 = f.readline()
	# parse
	list2 = f_content2.split(" ")

	# get rid of the garbage data in list
	list1.pop(0)
	list1.pop(-1)

	list2.pop(0)

	# slice the index that reps the change amount out of list1 
	# and store the total value in a var, and make it an int
	change_amount = int(list1[0]) 

	# store the rest of the indexs into a var that reps the change I own
	coins = list1[1:]

	my_coins_string = ' '.join(x for x in coins)

	# total value
	print(change_amount)

	# space seperated list of coins 
	print(my_coins_string)

	# third line is the bound --
	sign = list2[1]
	number = int(list2[2])
	num_less = number - 1
	num_more = int(number) + 1 
	if sign == '<':
		print(f'Program can only accept {num_less} or less coins')
	elif sign == '>' and sign == '=':
		print(f'Program can accept {number} or more coins')
	elif sign == '<' and sign == '=':
		print(f'Program can accept {number} or less coins')
	else:
		print(f'Program can accept {num_more} or more coins')
