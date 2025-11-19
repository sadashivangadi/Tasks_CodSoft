#password generation with random strings tasks3
import random
import string
print("Simple Password Genaration")

len=int(input("Enter the Lenght of Password"))

letters=string.ascii_letters
digits=string.digits
symbols=string.punctuation


all_char=letters+digits+symbols

password=" ".join(random.choice(all_char)
for _ in range(len))

print("Generate Password",password)
