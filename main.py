import sys
from game import Game
from ui import GameUI

def main():
    game = Game()
    ui = GameUI(game)

    while True:
        ui.display_main_screen()
        command = input("Enter command: ").strip().lower()
        if command == 'quit':
            print("Thank you for playing!")
            sys.exit()
        elif command == 'start':
            game.start_game()
        elif command == 'status':
            ui.display_status()
        elif command == 'task':
            ui.display_current_task()
        elif command == 'submit':
            code = input("Enter your code:\n")
            game.submit_code(code)
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
