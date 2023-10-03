# recursive number list
def rec_increment(p):
    if len(p) == 0:
        return ""                    
    else:      
        print(p[0], end=" ")                 
        return rec_increment(p[1:])  

print(rec_increment([100, 20, 18, 12, 5, 5]))

# iterating through a list and printing the elements 
def num_list(numbers):
	for index in range(0,len(numbers)):
		return numbers[index:]

print(num_list([100, 20, 18, 12, 5, 5])) en the file
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

	my_coins_string = ' '.join(x for x in coinsen the file
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

	my_coins_string = ' '.join(x for x in coins
