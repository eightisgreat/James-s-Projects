import random
import sys
import time

user_wins = 0
computer_wins = 0

def end_score():
	print("You won", user_wins, "times.")
	print("The computer won", computer_wins, "times")
	print("Thank you for playing!")



while True: 
	computer_number = random.randint(1, 3)
	inquiry = "Play the computer in rock, paper, scissors!(or quit) What is your guess? "
	for expression in inquiry:
		sys.stdout.write(expression)
		sys.stdout.flush()
		time.sleep(0.05)
	user_guess = input("> ").lower()


#game loop
	if user_guess not in ["rock", "paper", "scissors", "quit"]:
		print("This is not an acceptable answer.")
		continue
#rock=1 paper=2 scissors=3
#tie conditions
	if user_guess == str("rock") and computer_number == int(1):
		print("This is a tie! The computer's guess was the same!")
		continue
	if user_guess == str("paper") and computer_number == int(2):
		print("This is a tie! The computer's guess was the same!")
		continue
	if user_guess == str("scissors") and computer_number == int(3):
		print("This is a tie! The computer's guess was the same!")
		continue
#win conditions
	if user_guess == str("rock") and computer_number == int(3):
		user_wins += 1
		print("You win! Rock beats scissors!")
		continue
	if user_guess == str("paper") and computer_number == int(1):
		user_wins += 1
		print("You win! Paper beats rock!")
		continue
	if user_guess == str("scissors") and computer_number == int(2):
		user_wins += 1
		print("You win! Scissors beats paper!")
		continue
#lose conditions
	if user_guess == str("scissors") and computer_number == int(1):
		computer_wins += 1
		print("You lose! Rock beats scissors!")
		continue
	if user_guess == str("rock") and computer_number == int(2):
		computer_wins += 1
		print("You lose! Paper beats rock!")
		continue
	if user_guess == str("paper") and computer_number == int(3):
		computer_wins += 1
		print("You lose! Scissors beats paper!")
		continue
	else:
		end_score()
		input()
		computer_wins = 0
		user_wins = 0

