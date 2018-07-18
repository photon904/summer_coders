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

	f_content3 = f.readline()
	list3 = f_content3.split(" ")


	# get rid of the garbage data in list
	list1.pop(0)
	list1.pop(-1)

	list2.pop(0)

	list3.pop(0)


	# slice the index that reps the change amount out of list1 
	# and store the total value in a var, and make it an int
	change_amount = int(list1[0]) 

	# store the rest of the indexs into a var that reps the change I own
	coins = list1[1:]

	my_coins_string = ' '.join(x for x in coins)

	eng_output = " ".join(x for x in list3)

	# total value
	print(change_amount)

	# space seperated list of coins 
	print(my_coins_string)

	# third line is the bound -- eng des of the bound.
	print(eng_output)

