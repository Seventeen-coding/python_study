
number = 23
running = True

while running :
    guess = int (input('Enter an inteager　：'))

    if guess == number:
        print('guess {guess} == number {number}'.format(guess=guess,number=number))
        running = False
    elif guess < number:
        print('guess {} < number {}'.format(guess, number))
    else:
        print('guess',guess,'>', 'number',number)
else:
    print('game over')

print('done')