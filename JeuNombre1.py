# Jeu "Deninez le nombre"
import random

print('Bonjour ! Comment t\'appelles-tu ?')
my_name = input()

number = random.randint(1, 20)
print('Bien, ' + my_name + ', je pense à un nombre entre 1 et 20. Tu as 6 essais.')

guesses_taken = 0
guesses_left = 6
while guesses_left > 0:
    print('Essaie de le deviner.')
    guess = input()

    if not guess.isdigit():
        print('Ceci n\'est pas un nombre positif.')
        continue

    guess = int(guess)

    if guess <= 0 or guess > 20:
        print('Ce nombre n\'est pas entre 1 et 20.')
        continue

    guesses_left -= 1
    guesses_taken += 1

    if guess < number:
        print('Trop petit.')

    if guess > number:
        print('Trop grand.')

    if guess == number:
        break

if guess == number:
    guesses_taken = str(guesses_taken)
    print('Bravo, ' + my_name + ' ! Tu as trouvé mon nombre en ' + guesses_taken +' essai(s) !')

if guess != number:
    number = str(number)    
    print('Raté ! Le nombre auquel je pensais était ' + number + '.')
