from __future__ import division
import random

#GLOBAL VARIABLES
outcomes = []
keep_playing = True

#Sum it all up, print some info on the outcomes
def print_statistics():
	totalwins = 0
	iterations = len(outcomes)
	for x in outcomes:
		totalwins = totalwins + x
	average_win = totalwins / iterations * 100
	print("\nTotal wins: " + str(totalwins) + " out of " + str(iterations))
	print ("You won " + str(average_win) + "% of the time.")

#let the player pick the door and check if choice is valid
def pick_and_check():
	chosen_door = input("Which door would you like to choose?: ")
	choice_valid = False
	while choice_valid == False:
		if (chosen_door == "1" or chosen_door == "2" or chosen_door == "3"):
			chosen_door = int(chosen_door)
			if (int(chosen_door) < 1 or int(chosen_door) > 3):
				chosen_door = input("Invalid choice. Pick 1, 2, or 3: ")
			else:
				choice_valid = True
		else:
			chosen_door = input("Invalid choice. Pick 1, 2, or 3: ")
	chosen_door = int(chosen_door)
	return chosen_door

#let the player pick the door and check if choice is valid
def switch_or_stay_check():
	switch = input("\nNow, since you chose door number " + str(chosen_door) + "...\nand you know door number " \
	+ str(fake_door) + " is bad...\ndo you want to stay with door " + str(chosen_door) \
	+ " or switch to door number " + str(6 - chosen_door - fake_door) + "? (switch / stay): ")
	choice_valid = False
	while choice_valid == False:
		if (switch != "switch" and switch != "stay"):
			switch = input("Invalid choice. Pick switch or stay: ")
		else:
			choice_valid = True
	if switch == "switch":
		return True
	else:
		return False

#end game, see if we should continue and check choice, return boolean yes/no
def keep_playing_question():
	check = False
	kp = True
	while check == False:
		kp = input("Do you want to keep playing? (yes/no): ")
		if(kp == "yes" or kp == "y"):
			kp = True
			check = True
		elif(kp == "no" or kp == "n"):
			kp = False
			check = True
		else:
			print("Not a valid choice.")
	return kp

#get results of choice and if it matches winning door, return if we won or not
def run(chosen_door, fake_door, win_door):
	CHOOSE_TO_SWITCH = switch_or_stay_check()
	if(CHOOSE_TO_SWITCH):
		chosen_door = 6 - int(chosen_door) - int(fake_door)

	did_we_win = False
	if(win_door == chosen_door):
		did_we_win = True
		outcomes.append(1)
	else:
		did_we_win = False
		outcomes.append(0)
	return did_we_win

#Just print out the startup message
def print_intro():
	print("\nWelcome to the Monty Hall problem.\n")
	print("Choose a door: 1, 2, or 3.")
	print("Only one of the doors contain a prize")

#print the choices we chose and fake door
def choice_print(chosen_door, fake_door):
	print("\nDoor number " +str(chosen_door) + ", a fantastic choice, and I'll " \
	+ "show you that nothing is behind door number " + str(fake_door))

#print out the results
def print_results(chosen_door, fake_door, win_door):
	print("\nRESULTS:\n" +
	"\nWinning door: " + str(win_door) +
	"\nChosen door: " + str(chosen_door) +
	"\nDid we win: " + str(did_we_win) + "\n")

##########
#MAIN LOOP
##########
while keep_playing == True:

	print_intro()

	win_door = random.randint(1,3)
	chosen_door = pick_and_check()
	fake_door = 0

	if chosen_door == win_door:
		fake_door = random.randint(1,3)
		while(fake_door == chosen_door):
			fake_door = random.randint(1,3)
	else:
		fake_door = 6 - int(chosen_door) - int(win_door)

	choice_print(chosen_door, fake_door)

	did_we_win = run(chosen_door, fake_door, win_door)

	print_results(chosen_door, fake_door, win_door)	

	keep_playing = keep_playing_question()
	if (not keep_playing):
		print_statistics()
		print("\nThanks for playing! kbai!\n")