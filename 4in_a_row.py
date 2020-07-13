import random

user_1 = "red"
user_2 = "yellow"
game_board = [[0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0]]
user_1_disks1 = 21
user_2_disks2 = 21

def show_game_board (game_board):
    for x in game_board:
        print(x)




#interaction start here

print("hello users welcome to my game :)")
print("user1 is red color")
print("user2 is yellow color")

tmp= input("press enter to choose by luck who will start")


who_is_first=random.randint(1,2)
if who_is_first==1:
    print("user1(red) is starting first")
else:

    print("user2 (yellow) is starting first")

#game start here

print("-===+===- -===+===- -===+===-  START GAME  -===+===- -===+===- -===+===-")

show_game_board(game_board)
