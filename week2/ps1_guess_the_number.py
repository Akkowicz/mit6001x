min = 0
max = 100
ans = 'answer'
guess = 0
print('Please think of a number between 0 and 100!') 
while True:
    guess = min + (max - min) // 2
    print('Is your secret number ' + str(guess) + '?')
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if ans == 'h':
        max = guess
    elif ans == 'l':
        min = guess
    elif ans == 'c':
        break
    else:
        print('Sorry, I did not understand your input.')
print('Game over. Your secret number was: ' + str(guess))
