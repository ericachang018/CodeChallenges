# input is an int 
# output is a staircase of # 
# Staircase to the left output:
     #
    ## 
   ###
  ####
 #####
######

def staircase_to_right(nums):
	steps = range(0,nums +1)
	print steps
	for x in steps:
		print "#" * x

def staircase_to_left(nums):
	steps = range(1, nums + 1)
	print steps
	for x in steps: 
		spaces = steps[-1] - x
		hashes = steps[x - 1]
		print " " * spaces + "#" * hashes	 


staircase_to_left(6)

# staircase_to_right(6)
# 