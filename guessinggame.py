secret_number = 6
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess_count +=1
    guess =int(input('guess: '))
    if guess == secret_number:
        print('YOU WON!')
        break
else:
    print('SORRY YOU FAILED!')
