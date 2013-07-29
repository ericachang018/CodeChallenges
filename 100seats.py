# make an array of seats from 1-100
seats = range(1,101)
# toggle odd on and off when we loop back around 
odd_toggle = 0

while len(seats) > 1:
    if len(seats) % 2 == 0 and odd_toggle == 0:
        del seats[odd_toggle::2]
    elif len(seats) % 2 == 0 and odd_toggle == 1:
        del seats[odd_toggle::2]
    elif len(seats) % 2 == 1 and odd_toggle == 0:
        del seats[odd_toggle::2]
        odd_toggle = 1
    else:
        del seats[odd_toggle::2]
        odd_toggle = 0

print seats