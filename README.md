## The Monty Hall Problem simulation

Problem is described here: https://en.wikipedia.org/wiki/Monty_Hall_Problem

The first montyhall_play.py program will let you play a simple version of the classic 3-door game. Choose a door, get told of a bad door, then choose to stay with your current door or switch to the other door that's left. Intuition tells us it's a 50% chance to win, but it's not. This version will keep track of your wins/losses then calculate and print your statistics once you're done. 

The montyhall_run.py program can generate any amount of iterations of random automatic play selecting random doors. There are inputs you can play around with, whether to always switch doors after a bad door is revealed and how many iterations you want to generate. If running at least 100 iterations (can go as high as you'd like, but north of 1,000,000 may take several minutes to run) you should start to reveal a clear statistic into the "problem" and the outcomes being ~33% to win if you stay and ~66% to win if you switch. Run it as many times as you like to show your friends that it's not a 50/50 chance ;).

## To run

Since it contains f-strings you need at least Python 3.6 or later. Just run `python montyhall_run.py` in command line to run.
