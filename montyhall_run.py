from __future__ import division
import random

CHOOSE_TO_SWITCH = True
iterations = 10000

#storing the outcomes here, 1 is a win, 0 is a loss
outcomes = []

for i in range(0, iterations):

	#set the random chosen door and the random win door
	win_door = random.randint(1,3)
	chosen_door = random.randint(1,3)

	did_we_win = False

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

	print("Results: Winning door: " + str(win_door) +
	" | Chosen door: " + str(chosen_door) +
	" | Win: " + str(did_we_win))

#print(str(outcomes[0]))

total = 0
for x in range(0, iterations):
	#print("outcomes value: " + str(int(outcomes[x])))
	total += int(outcomes[x])
	#print("total value: " + str(total))

average_win = total / iterations * 100
print("\nTotal wins: " + str(total) + " out of " + str(iterations))
print ("We won " + str(average_win) + "% of the time.")
