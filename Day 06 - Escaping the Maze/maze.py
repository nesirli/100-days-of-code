# The project is based on the website reeborg.ca
# The functions are pre-defined.


def turn_left():
    # This function does not work.
    # The function's purpose is silence errors.
    pass


def move():
    # This function does not work.
    # The function's purpose is silence errors.
    pass


def front_is_clear():
    # This function does not work.
    # The function's purpose is silence errors.
    pass


def right_is_clear():
    # This function does not work.
    # The function's purpose is silence errors.
    pass


def at_goal():
    # This function does not work.
    # The function's purpose is silence errors.
    pass


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
    elif front_is_clear():
        move()
    else:
        turn_left()
