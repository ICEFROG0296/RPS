import random

def f(user,c):
    if((user=='r' and c=='p') or (user=='p' and c=='s') or (user=='s' and c=='r')):
        print("System Won")
    elif user==c:
        print("It's Tie")
    else:
        print("User Won")
while True:     
    user=input()
    if user=='0':
        break
    c=random.choice(['r','s','p'])
    f(user,c)