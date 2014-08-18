#Make a tuple pair and identify which pair has the highest frequency Tumblr

import operator

example = "I want to be a part of it, New York, New York."
punctuation =",!\."

def remove_punctuation(text):
    clean_words = ""
    for letter in text:
        if letter not in punctuation:
            clean_words += letter
    return clean_words



clean_words = remove_punctuation(example)
mylist = clean_words.split()
mydict = {}

for i in range(len(mylist)-1):
    key=(mylist[i],mylist[i+1])
    if key in mydict:
        mydict[key] += 1
    else:
        mydict[key] =1

print mydict

keyanswer = max(mydict.iteritems(), key=operator.itemgetter(1))[0]
valueanswer = mydict[keyanswer]

print "The most frequent word pair is %s %s" %keyanswer,valueanswer



