# import random

# class Card:
#     def __init__(self, rank, suit):
#         # Each card has a rank (like '3', 'King', 'Ace') and a suit ('Hearts', 'Spades', etc.)
#         self.rank = rank
#         self.suit = suit
    
#     def __repr__(self):
#         # This special method is used to represent a Card object as a string.
#         return f"{self.rank} of {self.suit}"

# class Deck:
#     # Class variables that define the ranks and suits available in a deck of cards
#     ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
#     suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    
#     def __init__(self):
#         # Initialize a new deck of cards. This creates a list of Card objects for each combination of suit and rank.
#         self.deck = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
#     def shuffle(self):
#         # Shuffle the deck using Python's random module.
#         random.shuffle(self.deck)
    
#     def deal(self, number):
#         # Deal 'number' cards from the deck. If not enough cards are left, return a message instead.
#         return [self.deck.pop() for _ in range(number)] if number <= len(self.deck) else 'Not enough cards'
    
#     def count(self):
#         # Return the number of cards left in the deck.
#         return len(self.deck)

# # Example usage
# deck = Deck()  # Create a new deck of cards
# deck.shuffle()  # Shuffle the deck

# # Print a welcome message
# print(f"Card Dealer")
# print(f"I have shuffled a deck of 52 cards.")

# # Ask the user how many cards they would like to be dealt
# number_of_cards = int(input("How many cards would you like? "))  # User inputs the number of cards

# # Check if the requested number of cards is within a valid range
# if 0 < number_of_cards <= 52:  
#     hand = deck.deal(number_of_cards)  # Deal the cards from the deck
#     print("Here are your cards:")
#     for card in hand:
#         # Print each card in the hand
#         print(card)
# else:
#     # If the user asks for an invalid number of cards, prompt them again
#     print("Please enter a number between 1 and 52.")

# # Print how many cards are left in the deck after dealing
# print(f"There are {deck.count()} cards left in the deck.")
# print(f"Good Luck!")

# # Prompt the user to press any key to continue and wait for user input
# print("Press any key to continue...")
# input()  # This will wait for the user to press Enter


import random

class Card:
    def __init__(self, rank, suit):
        # Initialize card with rank and suit
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        # Return the card's details in human-readable form
        return f"{self.rank} of {self.suit}"

class Deck:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    
    def __init__(self):
        # Initialize the deck with 52 cards
        self.deck = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def shuffle(self):
        # Shuffle the deck
        random.shuffle(self.deck)
    
    def deal(self, number):
        # Deal 'number' of cards and return them
        return [self.deck.pop() for _ in range(number)] if number <= len(self.deck) else 'Not enough cards'
    
    def count(self):
        # Count the number of cards left in the deck
        return len(self.deck)

# Function to start the card dealing program
def start_program():
    deck = Deck()
    deck.shuffle()

    print(f"Card Dealer")
    print(f"I have shuffled a deck of 52 cards.")

    number_of_cards = int(input("How many cards would you like? "))
    if 0 < number_of_cards <= 52:
        hand = deck.deal(number_of_cards)
        print("Here are your cards:")
        for card in hand:
            print(card)
    else:
        print("Please enter a number between 1 and 52.")

    print(f"There are {deck.count()} cards left in the deck.")
    print(f"Good Luck!")

# Main program loop
while True:
    start_program()
    
    # Ask the user if they want to continue or quit
    print("Press Enter to deal again or type 'quit' to exit.")
    action = input()
    if action.lower() == 'quit':
        break  # Exit the loop and end the program



