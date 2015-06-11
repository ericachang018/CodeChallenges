# if n is divisible by 15

def fizz_buzz(num):
    for n in range(1,(num+1)):
        if n % 5 == 0:
            print "fizz buzz"
        elif n % 15 == 0:
            print "buzz"
        elif n % 3 == 0:
            print "fizz"
        else:
            print n

fizz_buzz(40)