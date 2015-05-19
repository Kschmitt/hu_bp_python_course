from random import randint
print 'Welcome to the mini-game guess the number'

y = randint(0, 100)

x = -5

    


count_guesses = 1
while  x != y:
    x = int(raw_input("Please enter a number between 0 and 100:"))   
    count_guesses = count_guesses + 1  
    if x == y:
        print 'You did it you found the number. You needed {} guesses'.format(count_guesses)
    elif x < y:
        print 'Your number is smaller than mine. Would you like to try again?'
    elif x > y:
        print 'Your number is larger than mine. Would you like to try again?'
   

