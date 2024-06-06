import sys
from game import Game
from ui import GameUI
from levels import load_levels

def main():
    levels = load_levels()
    game = Game(levels)
    ui = GameUI(game)

    while True:
        ui.display_main_screen()
        command = input("Enter command: ").strip().lower()
        if command == 'quit':
            print("Thank you for playing!")
            sys.exit()
        elif command == '1':
            game.start_game()
        elif command == '2':
            ui.display_status()
        elif command == '3':
            ui.display_current_task()
        elif command == '4':
            code = input("Enter your code:\n")
            game.submit_code(code)
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
