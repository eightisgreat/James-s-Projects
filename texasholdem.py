# Python program to shuffle a deck of card

# importing modules
import itertools, random
import re

# make a deck of cards
deck = list(itertools.product(range(1,15),['Spades','Hearts','Diamonds','Clubs']))

# shuffle the cards
random.shuffle(deck)

#remove invalid card (1) from the list
deck.remove((1, 'Spades'))
deck.remove((1, 'Hearts'))
deck.remove((1, 'Diamonds'))
deck.remove((1, 'Clubs'))

# draw two cards 

user_card1 = str(deck[0])
user_card2 = str(deck[1])

# removing commas, quotes and parentheses

remove1_user_card1 = (user_card1.replace(",", ""))
remove1_user_card2 = (user_card2.replace(",", ""))

remove2_user_card1 = (remove1_user_card1.replace("(", ""))
remove2_user_card2 = (remove1_user_card2.replace("(", ""))

remove3_user_card1 = (remove2_user_card1.replace("'", ""))
remove3_user_card2 = (remove2_user_card2.replace("'", ""))

remove4_user_card1 = (remove3_user_card1.replace(")", ""))
remove4_user_card2 = (remove3_user_card2.replace(")", ""))

# replacing numbers over 10 with face card text

jack_user_card1 = (remove4_user_card1.replace("11", "Jack"))
jack_user_card2 = (remove4_user_card2.replace("11", "Jack"))
queen_user_card1 = (jack_user_card1.replace("12", "Queen"))
queen_user_card2 = (jack_user_card2.replace("12", "Queen"))
king_user_card1 = (queen_user_card1.replace("13", "King"))
king_user_card2 = (queen_user_card2.replace("13", "King"))
ace_user_card1 = (king_user_card1.replace("14", "Ace"))
ace_user_card2 = (king_user_card2.replace("14", "Ace"))

dealt_card1 = ace_user_card1
dealt_card2 = ace_user_card2

print ("You have been dealt the following cards: ")
print()
print ("          " + (dealt_card1))
print()
print ("          " + (dealt_card2))
print()

user_bet = input("How much do you want to bet? ")

flop_card1 = str(deck[3])
flop_card2 = str(deck[4])
flop_card3 = str(deck[5])

remove1_flop_card1 = (flop_card1.replace(",", ""))
remove1_flop_card2 = (flop_card2.replace(",", ""))
remove1_flop_card3 = (flop_card3.replace(",", ""))

remove2_flop_card1 = (remove1_flop_card1.replace("(", ""))
remove2_flop_card2 = (remove1_flop_card2.replace("(", ""))
remove2_flop_card3 = (remove1_flop_card3.replace("(", ""))

remove3_flop_card1 = (remove2_flop_card1.replace("'", ""))
remove3_flop_card2 = (remove2_flop_card2.replace("'", ""))
remove3_flop_card3 = (remove2_flop_card3.replace("'", ""))

remove4_flop_card1 = (remove3_flop_card1.replace("(", ""))
remove4_flop_card2 = (remove3_flop_card2.replace("(", ""))
remove4_flop_card3 = (remove3_flop_card3.replace("(", ""))

final_flop_card1 = (remove4_flop_card1.replace(")", ""))
final_flop_card2 = (remove4_flop_card2.replace(")", ""))
final_flop_card3 = (remove4_flop_card3.replace(")", ""))

jack_flop_card1 = (final_flop_card1.replace("11", "Jack"))
jack_flop_card2 = (final_flop_card2.replace("11", "Jack"))
jack_flop_card3 = (final_flop_card3.replace("11", "Jack"))
queen_flop_card1 = (jack_flop_card1.replace("12", "Queen"))
queen_flop_card2 = (jack_flop_card2.replace("12", "Queen"))
queen_flop_card3 = (jack_flop_card3.replace("12", "Queen"))
king_flop_card1 = (queen_flop_card1.replace("13", "King"))
king_flop_card2 = (queen_flop_card2.replace("13", "King"))
king_flop_card3 = (queen_flop_card3.replace("13", "King"))
ace_flop_card1 = (king_flop_card1.replace("14", "Ace"))
ace_flop_card2 = (king_flop_card2.replace("14", "Ace"))
ace_flop_card3 = (king_flop_card3.replace("14", "Ace"))

final_flop_card1 = (ace_flop_card1.replace("14", "Ace"))
final_flop_card2 = (ace_flop_card2.replace("14", "Ace"))
final_flop_card3 = (ace_flop_card3.replace("14", "Ace"))

print("The flop is: ")
print()
print("          " + (final_flop_card1))
print()
print("          " + (final_flop_card2))
print()
print("          " + (final_flop_card3))
print()

input()

turn_card1 = str(deck[6])

remove1_turn_card1 = (turn_card1.replace(",", ""))
remove2_turn_card1 = (remove1_turn_card1.replace("(", ""))
remove3_turn_card1 = (remove2_turn_card1.replace("'", ""))
remove4_turn_card1 = (remove3_turn_card1.replace("(", ""))
remove5_turn_card1 = (remove4_turn_card1.replace(")", ""))

jack_turn_card1 = (remove5_turn_card1.replace("11", "Jack"))
queen_turn_card1 = (jack_turn_card1.replace("12", "Queen"))
king_turn_card1 = (queen_turn_card1.replace("13", "King"))
ace_turn_card1 = (king_turn_card1.replace("14", "Ace"))

final_turn_card1 = (ace_turn_card1.replace("14", "Ace"))

print("The turn card is: ")
print()
print("          " + (final_turn_card1))
print()

input()

river_card1 = str(deck[7])

remove1_river_card1 = (river_card1.replace(",", ""))
remove2_river_card1 = (remove1_river_card1.replace("(", ""))
remove3_river_card1 = (remove2_river_card1.replace("'", ""))
remove4_river_card1 = (remove3_river_card1.replace("(", ""))

jack_river_card1 = (remove4_river_card1.replace("11", "Jack"))
queen_river_card1 = (jack_river_card1.replace("12", "Queen"))
king_river_card1 = (queen_river_card1.replace("13", "King"))
ace_river_card1 = (king_river_card1.replace("14", "Ace"))

final_river_card1 = (ace_river_card1.replace(")", ""))

print("The river card is: ")
print()
print("          " + (final_river_card1))
print()

input()

2, of, Spades

[(4, 'Clubs'), (12, 'Clubs'), (7, 'Clubs'), (9, 'Clubs'), (8, 'Clubs'), (8, 'Spades'), (11, 'Diamonds'), (2, 'Hearts'), (13, 'Clubs'), (12, 'Diamonds'), (11, 'Hearts'), (12, 'Spades'), (6, 'Spades'), (2, 'Clubs'), (3, 'Clubs'), (11, 'Spades'), (10, 'Diamonds'), (10, 'Spades'), (3, 'Diamonds'), (13, 'Spades'), (3, 'Hearts'), (7, 'Diamonds'), (7, 'Hearts'), (4, 'Diamonds'), (4, 'Spades'), (11, 'Clubs'), (12, 'Hearts'), (5, 'Diamonds'), (9, 'Diamonds'), (13, 'Hearts'), (14, 'Hearts'), (7, 'Spades'), (10, 'Hearts'), (4, 'Hearts'), (6, 'Diamonds'), (6, 'Hearts'), (3, 'Spades'), (9, 'Hearts'), (14, 'Spades'), (9, 'Spades'), (6, 'Clubs'), (5, 'Clubs'), (5, 'Spades'), (2, 'Diamonds'), (2, 'Spades'), (10, 'Clubs'), (14, 'Diamonds'), (8, 'Diamonds'), (14, 'Clubs'), (8, 'Hearts'), (13, 'Diamonds'), (5, 'Hearts')]

deck_count = count.deck()