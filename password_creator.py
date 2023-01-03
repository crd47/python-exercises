import random#it creates random outputs from the computer
import string#it is a library for strings
print("welcome to the password creator")
adjectives=['dumb','crazy','brave','cool','complex','handsome','proper','like','syke','dyke']#it is the inputs for the password
noun=['dog','cat','wolf','kangaroo','fox','sniper','militia','panda','snowwhite']
while True:
    adjectives=random.choice(adjectives)
    noun=random.choice(noun)
    characters=random.choice(string.punctuation)
    num=random.randrange(0,99)
    password=adjectives+noun+str(num)
    print('your new password is:' +password)
    response=input("do you want another password? 'y' or 'n' ")
    if response=='n':
     break
if len(password)<5:
    print("the password is weak better try again")
else:
    print("you have it")