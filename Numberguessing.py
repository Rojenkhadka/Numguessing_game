import random
import math

lowest = int(input("Enter the lower number : "))
highest = int(input("Enter the highest number : "))

random_num = random.randint(lowest, highest)
# print(f"\nThe number generated was {r}.")

count = 0
max_guesses = math.ceil(math.log(highest - lowest + 1, 2))
print(f"You have only {max_guesses} chances to guesses.")

while count < max_guesses:
    # count += 1

    guess = int(input("Guess a number : "))
  
    if random_num == guess:
        print(f"Congratulations! You have guessed the number in {count} try.")
        break
    elif random_num > guess:
        print("You have guess a low number.") 
    elif random_num < guess:
        print("You have guessed a high number.")
    count += 1

if  count == max_guesses and guess != random_num:
    print(f'game over! The number was {random_num}')
    print('Better luck next time')