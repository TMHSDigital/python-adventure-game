class Game:
    def __init__(self, levels):
        self.level = 0
        self.resources = 0
        self.levels = levels
        self.current_task = None

    def start_game(self):
        self.level = 1
        self.resources = 0
        self.current_task = self.levels[self.level - 1].task_description
        print("Game started. Good luck!")

    def submit_code(self, code):
        if self.level == 0:
            print("Please start the game first.")
            return
        
        user_function = self._generate_user_function(code)
        if self.levels[self.level - 1].check_solution(user_function):
            print("Correct! Moving to the next level.")
            self.level += 1
            if self.level <= len(self.levels):
                self.current_task = self.levels[self.level - 1].task_description
            else:
                print("Congratulations! You've completed all tasks.")
        else:
            print("Incorrect. Please try again.")

    def _generate_user_function(self, code):
        exec(code)
        function_name = code.split('(')[0].split()[-1]
        return locals()[function_name]

    def get_current_task(self):
        if self.current_task:
            return self.current_task
        return "No current task. Please start the game."

    def get_status(self):
        return {
            "level": self.level,
            "resources": self.resources,
            "current_task": self.current_task if self.current_task else "No current task."
        }
