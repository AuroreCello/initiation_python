# Jeu "Deninez le nombre"
import random

guesses_taken = 0

print('Bonjour ! Comment t appelles-tu ?')
my_name = input()

number = random.randint(1, 20)
print('Bien, ' + my_name + ', je pense à un nombre entre 1 et 20.')

for guesses_taken in range(6):
    print('Essaie de le deviner.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Trop petit.')

    if guess > number:
        print('Trop grand.')

    if guess == number:
        break

if guess == number:
    guesses_taken = str(guesses_taken + 1)
    print('Bravo, ' + my_name + '! Tu as trouvé mon nombre en ' + guesses_taken +' essai(s) !')

if guess != number:
    number = str(number)    
    print('Raté ! Le nombre auquel je pensais était' + number + '.')
