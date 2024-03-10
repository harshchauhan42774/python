# import random
# d={1:'rock',2:'paper',3:'Scissor'}
# ch= int(input("Enter the choice"))
# print("You have chosen",ch,"=",d[ch])
# com=random.randint(1,3)
# print("computer have chosen",com,'='d([com]))

# if (ch==1 and com =3)or(ch==2 and com ==1)or(ch==3 and com==2):
#     print('you won')

# elif(ch==1 and com==1)or(ch==2 and com==2 )or(ch==3 and com==2):
#      print("draw")

# else:
#     print("you lose")


import random

d = {1: 'rock', 2: 'paper', 3: 'scissors'}

ch = int(input("Enter the choice: "))
print("You have chosen", ch, "=", d[ch])

com = random.randint(1, 3)
print("Computer has chosen", com, '=', d[com])

if (ch == 1 and com == 3) or (ch == 2 and com == 1) or (ch == 3 and com == 2):
    print('You won')

elif ch == com:
    print("It's a draw")

else:
    print("You lose")

# output:
# Enter the choice: 1
# You have chosen 1 = rock
# Computer has chosen 3 = scissors
# You won
