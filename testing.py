import random

chosen_door = 2
win_door = 3

doors = [1, 2, 3]
doors.remove(chosen_door)
if win_door != chosen_door:
    doors.remove(win_door)
bad_door = random.choice(doors)

print(bad_door)