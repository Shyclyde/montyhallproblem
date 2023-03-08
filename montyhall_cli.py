from src.montyhall import MontyGame

GAME = MontyGame()


def ask_play_again() -> bool:
    while True:
        response = input("Play again? (Y or N): ").upper()
        if response in ["Y", "N"]:
            return True if response == "Y" else False
        print("Not a valid game type, try again.")


def play(automate: bool, iterations: int) -> None:
    """Main game loop, will automate through if selected."""

    switch = False
    if automate:
        switch = GAME.ask_for_switch(automate)
    
    while iterations > 0:
        if automate:
            print(f"Playing game {GAME.games_played + 1}...", end="\r")
            
        GAME.setup_new_game()
        GAME.pick_door(automate)
        GAME.expose_random_bad_door()
        
        if not automate:
            switch = GAME.ask_for_switch(automate)
            
        if switch:
            GAME.switch_chosen_door()

        if GAME.evaluate_win():
            if not automate:
                print("You picked the correct door!")
        else:
            if not automate:
                print(f"Wrong door, the winner was door number {GAME.win_door}, sorry!")
        
        if automate:
            iterations -= 1
        else:
            if not ask_play_again():
                break


def ask_if_automating() -> bool:
    while True:
        response = input("Would you like to [A]utomate or [P]lay? (A or P): ").upper()
        if response in ["A", "P"]:
            return True if response == "A" else False
        print("Not a valid game type, try again.")


def ask_iterations() -> int:
    while True:
        iter_input = input("How many random games should we generate?: ")
        if iter_input.isdigit() and int(iter_input) > 0:
            return int(iter_input)
        print("Not a valid integer, try again.")


def main() -> None:
    print("Let's play some Monty Hall games!")

    automate: bool = ask_if_automating()
    iterations = 1
    if automate:
        iterations = ask_iterations()
    play(automate, iterations)

    stats = GAME.get_game_statistics()
    print(
        f"\nTotal wins: {stats['wins']} out of {stats['played']}. Win rate: {stats['win_pct']}%"
    )


if __name__ == "__main__":
    main()
