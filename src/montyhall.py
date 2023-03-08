import random


class MontyGame:
    """Class instance for Monty Hall game setup and game actions"""

    def __init__(self) -> None:
        self.games_won = 0
        self.games_played = 0
        self.win_door = 0
        self.chosen_door = 0
        self.bad_door = 0

    def setup_new_game(self) -> None:
        self.win_door = random.randint(1, 3)
        self.chosen_door = 0
        self.bad_door = 0
        
    def evaluate_win(self) -> bool:
        self.games_played += 1
        if self.chosen_door == self.win_door:
            self.games_won += 1
            return True
        return False
            

    def get_game_statistics(self) -> dict:
        win_pct = 0.0
        if self.games_won > 0:
            win_pct = round((self.games_won / self.games_played) * 100, 2)

        return {
            "wins": self.games_won,
            "played": self.games_played,
            "win_pct": win_pct,
        }

    def pick_door(self, auto: bool) -> None:
        """Ask user for the door. If auto is True is set, pick a random door"""
        
        if auto:
            self.chosen_door = random.randint(1, 3)
        else:
            while True:
                choice = input("Monty: Which door would you like to choose? (1, 2, or 3): ")
                if choice.isdigit() and int(choice) in [1, 2, 3]:
                    self.chosen_door = int(choice)
                    break
                print("Not a valid door choice, try again.")

    def ask_for_switch(self, auto: bool):
        """Ask for input if we should switch, return True if so, else False"""
        
        if not auto:
            other_door = 6 - self.chosen_door - self.bad_door
            print(f"Monty: You picked door number {self.chosen_door}.")
            print(f"Monty: I'm going to reveal that door number {self.bad_door} has a goat behind it...")
            print(f"Now, you can either stay with door number {self.chosen_door} or go with door number {other_door}.")
        
        while True:
            switch = input("Monty: Would you like to switch or stay?: ")
            if switch == "switch":
                return True
            elif switch == "stay":
                return False
            print("Not a valid entry, type 'switch' or 'stay' to continue.")

    def expose_random_bad_door(self) -> None:
        """Set the door we're exposing as the decoy"""

        doors = [1, 2, 3]
        doors.remove(self.chosen_door)
        if self.win_door != self.chosen_door:
            doors.remove(self.win_door)
        self.bad_door = random.choice(doors)
        
    def switch_chosen_door(self) -> None:
        doors = [1, 2, 3]
        doors.remove(self.chosen_door)
        doors.remove(self.bad_door)
        self.chosen_door = doors[0]
