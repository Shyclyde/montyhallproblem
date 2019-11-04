from __future__ import division
import random


#let the player pick the door and check if choice is valid
def pick_door():
	chosen_door = input("Choose a door: 1, 2, or 3?: ")
	while True:
		if (chosen_door == "1" or chosen_door == "2" or chosen_door == "3"):
			return int(chosen_door)
		else:
			chosen_door = input("Invalid choice. Pick 1, 2, or 3: ")

#let the player pick the door and check if choice is valid
def choose_to_switch():
	print(f"Now, since you chose door number {chosen_door}, and you know door number {exposed_door} is bad...")
	switch = input(f"Do you want to stay with door {chosen_door} or switch to door number {6 - chosen_door - exposed_door}? (switch / stay): ")

	while True:
		if (switch != "switch" and switch != "stay"):
			switch = input("Invalid choice. Pick switch or stay: ")
		else:
			if switch == "switch":
				return True
			else:
				return False

#print out the results
def print_results(chosen_door, win_door):
	print("\nRESULTS:\n")
	print(f"Winning door: {win_door}")
	print(f"Chosen door: {chosen_door}")
	if chosen_door == win_door:
		print("Awesome, you won!\n")
	else:
		print("Too bad, maybe next time.\n")

#end game, see if we should continue and check choice, return boolean
def keep_playing_question():
	while True:
		play = input("Do you want to keep playing? (yes/no): ")
		if(play == "yes" or play == "y"):
			return True
		elif(play == "no" or play == "n"):
			return False
		else:
			print("Not a valid choice.")

#Sum it all up, print some info on the outcomes
def print_statistics(win_count, run_count):
	print(f"\nTotal wins: {win_count} out of {run_count}")
	print (f"We won {round(win_count / run_count * 100, 2)}% of the time.")

#MAIN LOOP
win_count = 0
run_count = 0
while True:

	print("\nWelcome to the Monty Hall game! Out of 3 doors only 1 has a prize.")
	#set up the doors
	win_door = random.randint(1,3)
	chosen_door = pick_door()
	if win_door == chosen_door:
		exposed_door = random.randint(1,3)
		while exposed_door == chosen_door:
			exposed_door = random.randint(1,3)
	elif win_door != chosen_door:
		exposed_door = 6 - win_door - chosen_door
	print(f"\nDoor number {chosen_door}, a fantastic choice! Now I'll show you nothing is behind door {exposed_door}.")

	if choose_to_switch():
		chosen_door =  6 - int(chosen_door) - int(exposed_door)

	if chosen_door == win_door:
		win_count += 1
	run_count += 1
	print_results(chosen_door, win_door)	

	if (not keep_playing_question()):
		print_statistics(win_count, run_count)
		print("\nThanks for playing!\n")
		break