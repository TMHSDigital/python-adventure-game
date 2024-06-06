class Level:
    def __init__(self, level_number, task_description, solution_function):
        self.level_number = level_number
        self.task_description = task_description
        self.solution_function = solution_function

    def check_solution(self, user_function):
        try:
            return self.solution_function() == user_function()
        except Exception as e:
            print(f"Error while evaluating solution: {e}")
            return False

def load_levels():
    return [
        Level(1, "Write a program to calculate the sum of two numbers.", lambda: sum_two_numbers(3, 5)),
        Level(2, "Write a program to find the largest number in a list.", lambda: find_largest_number([1, 2, 3, 4, 5])),
        Level(3, "Write a program to reverse a string.", lambda: reverse_string("hello"))
    ]

def sum_two_numbers(a, b):
    return a + b

def find_largest_number(lst):
    return max(lst)

def reverse_string(s):
    return s[::-1]
