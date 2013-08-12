# Added a bunch of print statements to debug. A value was being dropped
# problem has been fixed!! Wooh its working!

# list comprehension again! 
# numbers = [random.randint(1,1000) for i in range(1001)]

import random

numbers = [random.randint(1,10) for i in range(10)]
print numbers

def mergeSort(numbers):
	# Breaking apart the list starts here
    if len(numbers) ==1:
        return numbers
    # else half the length of your list of numbers into a left and right list 
    # This is recursive so it will continue to split into left and right lists till
    # there is only one number left.  
    else:
        half = len(numbers)/2
        left = mergeSort (numbers[:half])
        right = mergeSort(numbers[half:])     
    l = []

	#Merging the list begins here 
    print "begin merge phase> ", left, right 
    # while there is a left and right list are true do the following: 
    while len(left) and len(right):
        print "comparing> ", left[0], right[0]
        # if left index 0 is less than append the left value. 
        if left[0] < right[0]:
            print "appending left value> ", left[0]
            l.append(left.pop(0))
            print "this is l after a append.left.pop", l 
        # else: if the right side is greater append the right value.  
        else:
            print "appending right value> ", right[0]
            l.append(right.pop(0))
	
	#ternary a switch if the left side is true append othe wise append the right 
    l.extend(left if len (left)> 0 else right) 
    print "appended results> ", l
    return l


s = mergeSort(numbers)
print "sorted> ", s