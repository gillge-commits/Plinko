import random
import math

# function to make the board
def make_board():
    
    # set every second spot to a peg
    for i in range(rows):
        start = centre - i
        for j in range(i + 1): 
            board[i][start + 2 * j] = "."
            
    # set up holes at bottom with values decreasing inwards to -1 at centre
    for i in range(number_of_holes):
        distance = abs(i - holes_centre)
        holes[i] = round(-1 + distance * ((rows + 1) / holes_centre), 2)
        

# function to make ball drop
def release_ball(start_index):
    ways = ['L', 'R']
    x_index = centre + start_index
    for y_index in range (rows):
        board[y_index][x_index] = "0"
        way = random.choice(ways)
        if way == 'L':
            x_index -= 1
        else:
            x_index += 1
    return x_index


# function to calculate winnings
def winnings_calculator(wager, x_index):
    hole_index = x_index // 2
    winnings = wager * holes[hole_index]
    return winnings

# function to show board
def show_board():
    for i in range(rows):
        myString = ""
        for j in range(columns):
            myString += board[i][j]
        print(myString)    
    


# define variables and lists

rows = int(input("How many rows would you like to play (more = harder)? "))
columns = rows * 2 - 1
centre = columns // 2
number_of_holes = rows + 1

board = [[" " for _ in range(columns)] for _ in range(rows)]
holes = [0] * number_of_holes
holes_centre = number_of_holes // 2

# set up the board

make_board()

# print game information and get user information

print("Here are the possible multipliers: ")
print(holes[0:len(holes)//2])

print("Remember there is also the -1 multiplier in the middle spot!")
money = int(input("How much would you like to wager? "))
start_side = input("Would you like to drop from the L or the R? ")

# call function to make ball drop
start_index = -1
if start_side == 'R':
    start_index = 1
    
x_index = release_ball(start_index)

# show the board
show_board()

# calculate money won or lost

winnings = winnings_calculator(money, x_index)

if winnings > 0:
    print("Congrats you have won ${:.2f}!".format(winnings))
elif winnings < 0:
    print("Sorry you have lost ${:.2f}...".format(winnings * -1 ))
else:
    print("You have not lost or made any money!")






