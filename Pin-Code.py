# Created by VeryNoobCoder on Github.com/VeryNoobCoder

import itertools
from string import digits
import random

pin = f"{random.randint(100000, 999999)}"   # Generate a random 6 digit PIN code
print(f"Target PIN: {pin}") 

print("PIN code cracking...")
for guess_digits in itertools.product(digits, repeat=6):   # Uses itertools to generate all possible combinations of any 6 digit number
    guess = ''.join(guess_digits)   # Converts the tuple of guessed digits into a string
    print(f"Cracking PIN: {guess}")

    if guess == pin:
        print(f"PIN has been cracked: {guess}")
        break
