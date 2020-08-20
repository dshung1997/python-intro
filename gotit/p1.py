import re

NUMBERS = {1: "one",
           "one": 1,
           2: "two",
           "two": 2,
           3: "three",
           "three": 3,
           4: "four",
           "four": 4,
           5: "five",
           "five": 5,
           6: "six",
           "six": 6,
           7: "seven",
           "seven": 7,
           8: "eight",
           "eight": 8,
           9: "nine",
           "nine": 9}


# def convert(origin):
#     z = re.match(
#         r"I completed (\w+) sessions and I rated my expert (\w+) stars", origin)

#     number_of_sessions = NUMBERS[int(z.group(1))]
#     number_of_stars = NUMBERS.index(z.group(2))

#     return f"I completed {number_of_sessions} sessions and I rated my expert {number_of_stars} stars"

class InvalidValueException(Exception):
    def __init__(self, message="Invalid number"):
        self.__message = message
        super().__init__(self.__message)


class Step:
    def __init__(self, number_of_sessions, number_of_stars):
        self.__number_of_sessions = number_of_sessions
        self.__number_of_stars = number_of_stars

    def make_step(self):
        try:
            if self.__number_of_sessions not in NUMBERS:
                raise InvalidValueException("Invalid number of sessions")

            if self.__number_of_stars not in NUMBERS:
                raise InvalidValueException("Invalid number of stars")

            print(
                f"I completed {NUMBERS[self.__number_of_sessions]} sessions and I rated my expert {NUMBERS[self.__number_of_stars]} stars")
        except InvalidValueException as inst:
            print(inst.args[0])


Step(1, "two").make_step()
Step(100, "two").make_step()
