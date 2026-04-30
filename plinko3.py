import random
import math
import gamble


def make_board(rows, columns, centre, board, holes, number_of_holes):
    """ Sets up the board """
    # set every second spot to a peg
    for i in range(rows):
        start = centre - i
        for j in range(i + 1): 
            board[i][start + 2 * j] = "."

         
    # set up holes at bottom with values decreasing inwards to -1 at centre
    holes_centre = number_of_holes // 2
    for i in range(number_of_holes):
        distance = abs(i - holes_centre)
        holes[i] = round(-1 + distance * ((rows + 1) / holes_centre), 2)

    
def release_ball(start_index, centre, board, rows):
    """ Moves the ball down the board """
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


def winnings_calculator(wager, x_index, holes):
    """ Calculates the winnings or loss """
    hole_index = x_index // 2
    winnings = wager * holes[hole_index]
    return winnings
 

def show_board(rows, columns, board):
    """ Prints a line of the board one by one"""
    for i in range(rows):
        my_string = ""
        for j in range(columns):
            my_string += board[i][j]
        print(my_string)


def proper_input():
    """ asks for a valid number until it recives one"""
    improper = True
    while improper == True:
        try:
            recieved_input = int(input())
            if recieved_input < 0:
                print("That is not a valid number, try again")
            else:
                improper = False
                return recieved_input
        except ValueError:
            print("That is not a valid number, try again")




def main():
    
    play = True
    while play == True:

        # define variables and lists

        print("How many rows would you like to play (more = harder)? ")
        rows = proper_input()
        columns = rows * 2 - 1
        centre = columns // 2
        number_of_holes = rows + 1


        board = [[" " for _ in range(columns)] for _ in range(rows)]
        holes = [0] * number_of_holes

        # set up the board

        make_board(rows, columns, centre, board, holes, number_of_holes)

        # print game information and get user information

        print("Here are the possible multipliers: ")
        print(holes[0:len(holes)//2])

        print("Remember there is also the -1 multiplier in the middle spot!")
        print("How much would you like to wager? ")
        money = proper_input()
        
        # ask user where they would like to drop from
        start_index = -1
        input_taken = False
        while input_taken == False:
            start_side = input("Would you like to drop from the L or the R? ")
            start_side = start_side.upper()
            if start_side == 'R':
                start_index = 1
                input_taken = True
            elif start_side == 'L':
                input_taken = True
            

        # call function to make ball drop

        x_index = release_ball(start_index, centre, board, rows)

        # show the board
        show_board(rows, columns, board)

        # calculate money won or lost

        winnings = winnings_calculator(money, x_index, holes)

        if winnings > 0:
            print("Congrats you have won ${:.2f}!".format(winnings))
        elif winnings < 0:
            print("Sorry you have lost ${:.2f}...".format(winnings * -1 ))
        else:
            print("You have not lost or made any money!")
        pass

        # ask if player wants to gamble if they made money
        if winnings > 0:
            gamble_choice = input("Would you like to gamble your winnings? (Y/N) ")
            if gamble_choice == "Y":
                # run gamble
                gamble_multiplier = gamble.play()
                print("Your final winnings is ${}.".format(winnings * gamble_multiplier))
                

        # ask if player wants to play again

        play_again = input("Do you want to play again (Y/N)? ")
        if play_again.upper() == "N":
            play = False

if __name__ == "__main__":
    main()

