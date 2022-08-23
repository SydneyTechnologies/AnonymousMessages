import random
import string

def generate_pass():
    # this function is responsible for generating the users password
    alphabets = string.ascii_lowercase
    password = ''
    for i in range(4):
        rand = random.randint(0, 9)
        password += str(rand)
    for j in range(2):
        password += random.choice(alphabets)
    print(password)
    return password

def generate_username():
    # this function generates the username
    # this will generate a 6 letter username 
    alphabets = string.ascii_lowercase
    username = ''
    for i in range(6):
        username += random.choice(alphabets)
    return username