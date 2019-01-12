from __future__ import division
import random

#CHOOSE_TO_SWITCH = False
#iterations = 10000

#storing the outcomes here, 1 is a win, 0 is a loss
outcomes = []

keep_playing = True

while keep_playing == True:

	print_intro()

	doors[] = pick_and_check()



	#print("win: " + win_door + " chosen: " + chosen_door + " fake: " + fake_door)


	did_we_win = False
	fake_door = 6 - chosen_door - win_door

	print("Alright, you chose door number " + str(chosen_door))

	if(chosen_door == win_door):

		print("Good choice, and I'll show you that nothing is behind door number " + bad_door)

	else:
		print("Good choice, and I'll show you that nothing is behind door number " + bad_door)

	if(CHOOSE_TO_SWITCH):
		print("-----")
		#create an array of doors
		doors = ['bad','bad','bad']

		if(chosen_door == win_door):
			doors[chosen_door - 1] = 'chosen_win'
		else:
			doors[(chosen_door - 1)] = 'chosen_bad'
			doors[(win_door - 1)] = 'win'

		print(doors)

		#if they don't match, just eliminate the non-chosen non-win door
		if(win_door != chosen_door):
			doors.remove('bad')
		#person chose the winning door, removing one of the others
		elif(win_door == chosen_door):
			if(chosen_door == 1):
				doors.remove(str(doors[random.randint(1,2)]))
			elif(chosen_door == 2):
				rand = random.randint(0,1)
				if(rand == 1):
					rand = 2
				doors.remove(str(doors[rand]))
			elif(chosen_door == 3):
				doors.remove(str(doors[random.randint(0,1)]))

		print("After elimination: " + str(doors))

		#set the "new" doors (just make them doors 1 & 2 now)
		new_chosen_door = -1
		new_win_door = -2
		if 'chosen_bad' in doors:
			new_chosen_door = doors.index('chosen_bad')
		elif 'chosen_win' in doors:
			new_chosen_door = doors.index('chosen_win')

		if 'win' in doors:
			new_win_door = doors.index('win')
		elif 'bad' in doors:
			new_win_door = doors.index('chosen_win')

		#switch doors
		if(new_chosen_door == 0):
			new_chosen_door = 1
		elif(new_chosen_door == 1):
			new_chosen_door = 0

		print("Switched doors. Chosen door: " + str(new_chosen_door) + " Win door: " + str(new_win_door))

		if(new_win_door == new_chosen_door):
			outcomes.append(1)
			did_we_win = True
		else:
			outcomes.append(0)
			did_we_win = False

	elif(not(CHOOSE_TO_SWITCH)):
		if(win_door == chosen_door):
			outcomes.append(1)
			did_we_win = True
		else:
			outcomes.append(0)
			did_we_win = False

	print("Result was...Winning door: " + str(win_door) +
	" | Chosen door: " + str(chosen_door) +
	" | Did we win: " + str(did_we_win))


	keep_playing = keep_playing_question()
	if not keep_playing:
		print_statistics()

	print("Thanks for playing! kbai!")


def print_statistics():
	total = 0
	for x in range(0, iterations):
		#print("outcomes value: " + str(int(outcomes[x])))
		total += int(outcomes[x])
		#print("total value: " + str(total))

	average_win = total / iterations * 100
	print("\nTotal wins: " + str(total) + " out of " + str(iterations))
	print ("You won " + str(average_win) + "% of the time.")


def print_intro():
	print("Welcome to the best command line game ever!")
	print("You're about to play for a prize of absolutely nothing.")
	print("You need to choose between door number 1, 2, or 3.")
	print("Only one of the doors contain a prize")

def pick_and_check():
	chosen_door = input("Which door would you like to choose?  ")
	choice_valid = False
	while choice_valid == False:
		if (int(chosen_door) < 1 or int(chosen_door) > 3):
			chosen_door = input("Invalid choice. This isn't rocket surgery. Pick 1, 2, or 3: ")
		else:
			choice_valid = True

	win_door = random.randint(1,3)
	fake_door = win_door
	if win_door == chosen_door:
		while fake_door == win_door:
			fake_door = random.randint(1,3)
	else:
		fake_door = 6 - chosen_door - win_door

	#return doors?

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
	return y
