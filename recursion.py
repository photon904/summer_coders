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

print(num_list([100, 20, 18, 12, 5, 5]))
