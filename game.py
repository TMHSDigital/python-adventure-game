class Game:
    def __init__(self):
        self.level = 1
        self.resources = 0
        self.current_task = ""
        self.tasks = self.load_tasks()

    def load_tasks(self):
        return {
            1: "Write a program to calculate the sum of two numbers.",
            2: "Write a program to find the largest number in a list.",
            3: "Write a program to reverse a string."
        }

    def start_game(self):
        self.level = 1
        self.resources = 0
        self.current_task = self.tasks[self.level]
        print("Game started. Good luck!")

    def submit_code(self, code):
        if self.evaluate_code(code):
            print("Correct! Moving to the next level.")
            self.level += 1
            if self.level in self.tasks:
                self.current_task = self.tasks[self.level]
            else:
                print("Congratulations! You've completed all tasks.")
        else:
            print("Incorrect. Please try again.")

    def evaluate_code(self, code):
        # Placeholder for code evaluation logic
        # This function should actually run the code and check if the output is correct
        return True

    def get_current_task(self):
        return self.current_task

    def get_status(self):
        return {
            "level": self.level,
            "resources": self.resources,
            "current_task": self.current_task
        }
