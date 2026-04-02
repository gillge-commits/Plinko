# gambling part of PLINKO

import random

def test():
    print("hello")

def form_deck(cards, suits):
    """ set up the cards to be picked from """
    for i in range (4): #suits
        suit = suits[i]
        for j in range(1,11): # cards to ten
            number = str(j)
            cards.append((suit, number))
        cards.append((suit, "Jack"))
        cards.append((suit, "King"))
        cards.append((suit, "Queen"))


def colour_checker(guess):
    """ return the colour of the card """
    if guess == "Hearts" or guess == "Diamonds":
        return "RED"
    else:
        return "BLACK"

def interaction(prompt, card):
    """ take in the input needed and show user the card """

    user_input = input(prompt)
    print("Card drawn is...")
    print("{} of {}".format(card[1], card[0]))
    return user_input
    

    
        
if __name__ == "__main__":
    # intilise
    
    cards = []
    suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

    # call deck function
    form_deck(cards, suits)
    
    # ask if the user wants to pick a card
    
    user_answer = input("Would you like to draw a card (Y/N)? ")
    if user_answer.upper() == "Y":

        # draw a card and check its colour
        drawn_card = random.choice(cards)
        card_suit = drawn_card[0]
        card_colour = colour_checker(card_suit)
        
        # interact with player (show and ask for colur)
        guess = interaction("What colour do you think the card is? ", drawn_card)

        # tell player if they have won or not
        if(card_colour == guess.upper()):
            print("You have doubled your money!")
            
            # ask user to play the second round
            user_answer = input("Double or nothing?? (Y/N) ")
            if user_answer.upper() == "Y":

                # draw card
                drawn_card = random.choice(cards)
                card_suit = drawn_card[0]

                # show card
                guess = interaction("What suit do you think the card is? ", drawn_card)

                # if player is right show them
                if guess.upper() == card_suit.upper():
                    print("You have quadrubled your money!!!")
                else:
                    print("Oh no, you have lost all your winnings.")
                

        else:
            print("Oh no, you have lost all your winnings.")

        
            


    
    

    
        
