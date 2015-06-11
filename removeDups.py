# Write a program to remove consecutive duplicate characters from a string 
# removeDupeChars("google") should return "gogle"

def removeDupChars(word): 
	results=[]
	seen = set() 
	for char in word:
		if char not in seen:
			seen.add(char)   
			results.append(char)
	print ''.join(results)

removeDupChars("google")

# returns gole so not the right solution... This solution strip all duplicate letters 

# try number 2 

def removeDupCharacters2(word): 
	results = []
	seen = []
	index = 0
	for char in word: 
		if char not in seen: 
			seen.append(char)
			results.append(char)
			if len(seen) > 1: 
				seen.pop(0)
	print ''.join(results)

removeDupCharacters2("googgggleee")
removeDupCharacters2("google")