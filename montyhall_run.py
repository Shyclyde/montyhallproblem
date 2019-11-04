from __future__ import division
import random

print("\nLet's generate some Monty Hall games!")

#ask for switch/stay, error check
def ask_for_switch():
	while True:
		chose_to_switch = input("Do we always want to switch or stay: ")
		if chose_to_switch == "switch":
			chose_to_switch = True
			return chose_to_switch
		elif chose_to_switch == "stay":
			chose_to_switch = False
			return chose_to_switch
		print("Not a valid entry, type 'switch' or 'stay' to continue.")

#ask for how many iterations, error check
def ask_for_iterations():	
	while True:
		iterations = input("How many random games should we generate: ")
		try:
			iterations = int(iterations)
			return int(iterations)
		except:
			print("Not a valid number, try again")

#start the game
def play_game(chose_to_switch):
		print("-")

		#set and print the random chosen door and set the random win door
		win_door = random.randint(1,3)
		chosen_door = random.randint(1,3)
		print(f"Chose door number {chosen_door}")

		#set and print the door we're exposing as the "decoy"
		if win_door == chosen_door:
			exposed_door = random.randint(1,3)
			while exposed_door == chosen_door:
				exposed_door = random.randint(1,3)
		elif win_door != chosen_door:
			exposed_door = 6 - win_door - chosen_door
		print(f"Door number {exposed_door} revealed as bad")

		#check for switch, then print action and door
		if chose_to_switch:
			chosen_door = 6 - chosen_door - exposed_door
			print(f"Switched to door number {chosen_door}")
		elif not chose_to_switch:
			print(f"Stayed with door number {chosen_door}")

		print(f"Door number {win_door} was the right door, win: {chosen_door == win_door}")

		return chosen_door == win_door

#calulate and print the results
def print_statistics(win_count, run_count):
	print(f"\nTotal wins: {win_count} out of {run_count}")
	print (f"We won {round(win_count / run_count * 100, 2)}% of the time.")

run_count = ask_for_iterations()
switch = ask_for_switch()
win_count = 0
for i in range(run_count):
	win_count += int(play_game(switch))
print_statistics(win_count, run_count)