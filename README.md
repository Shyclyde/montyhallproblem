# The Monty Hall Problem

[Monty Hall Problem Reference](https://en.wikipedia.org/wiki/Monty_Hall_Problem)

Running montyhall_cli.py will let you play a simple version of the Monty Hall 3-door game. Choose a door, have a bad door revealed, then choose to stay with your current door or switch to the other door.

Intuition tells us it's a 50% chance to win, but it's not. This will keep track of your wins/losses, then calculate and print your statistics once you're done.

You can choose to play along, or to automate through a set amount of iterations (choosing to either always stay or always switch). When running at least 100 iterations (you can go as high as you'd like), you should start to see the answer ;).

## Todo

- write out web app
- asyncio on automated runs
- rate limit on abusing the web server requests
- play with bootstrap
- get graphics for game
- figure out WSGI + NGINX
- unittests
