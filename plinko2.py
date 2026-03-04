import random
import math

# set up board

n = int(input("How many rows would you like to play (more = harder)? "))
m = n * 2 - 1
board = [[" " for _ in range(m)] for _ in range(n)]

centre = m // 2

# add pegs to every second positon


for i in range(n):                 
    start = centre - i            
    for j in range(i + 1):
        board[i][start + 2*j] = "."


# set up holes for ball to fall into

h = n + 1
hole_centre = h // 2
holes = [0] * h

for i in range(h):
    distance = abs(i - hole_centre)
    holes[i] = round(-1 + distance * ((n + 1) / hole_centre), 2)

# decide to go left or right and from there move ball

ways = ['L', 'R']
x_index = centre
for y_index in range (n):
    board[y_index][x_index] = "0"
    way = random.choice(ways)
    if way == 'L':
        x_index -= 1
    else:
        x_index += 1


# show the possible multipliers and ask for money

print("Here are the possible multipliers: ")
print(holes[0:len(holes)//2])
print("Remember there is also the -1 multiplier in the middle spot!")
money = int(input("How much would you like to wager? "))

# show the board

for i in range(n):
    myString = ""
    for j in range(m):
        myString += board[i][j]
    print(myString)

# calculate the amount of money won

hole_index = x_index // 2
winnings = holes[hole_index] * money

if winnings > 0:
    print("Congrats you have won ${:.2f}!".format(winnings))
elif winnings < 0:
    print("Sorry you have lost ${:.2f}...".format(winnings * -1 ))
else:
    print("You have not lost or made any money!")




        
    

    


        


    

    
    



