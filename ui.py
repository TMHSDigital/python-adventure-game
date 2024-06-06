class GameUI:
    def __init__(self, game):
        self.game = game

    def display_main_screen(self):
        print("===== Code Idle Sim =====")
        print("1. Start Game")
        print("2. View Status")
        print("3. View Current Task")
        print("4. Submit Code")
        print("Type 'quit' to exit the game.")
        print("=========================")

    def display_status(self):
        status = self.game.get_status()
        print("===== Game Status =====")
        print(f"Level: {status['level']}")
        print(f"Resources: {status['resources']}")
        print("=======================")

    def display_current_task(self):
        task = self.game.get_current_task()
        print("===== Current Task =====")
        print(task)
        print("========================")
