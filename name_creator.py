import random, string

input1 = input("What letter would you like? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
input2 = input("What letter would you like? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
input3 = input("What letter would you like? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'

def generator():
    if input1=='v':
        letter1 = random.choice(vowels)
    elif input1 == 'c':
        letter1 = random.choice(consonants)
    elif input1 == 'l':
        letter1 = random.choice(string.ascii_lowercase)
    else:
        letter1 = input1

    if input2=='v':
        letter2 = random.choice(vowels)
    elif input2 == 'c':
        letter2 = random.choice(consonants)
    elif input2 == 'l':
        letter2 = random.choice(string.ascii_lowercase)
    else:
        letter2 = input2

    if input3=='v':
        letter3 = random.choice(vowels)
    elif input3 == 'c':
        letter3 = random.choice(consonants)
    elif input3 == 'l':
        letter3 = random.choice(string.ascii_lowercase)
    else:
        letter3 = input3

    name = letter1 + letter2 + letter3
    return(name)

for i in range(20):
    print(generator())
