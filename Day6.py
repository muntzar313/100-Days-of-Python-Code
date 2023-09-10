# Using For Loop

def move_right():
    turn_left()
    turn_left()
    turn_left()

def first_huddle():
    turn_left()
    turn_left()
    turn_left()
    move()

def for_left():
    move()
    turn_left()
    move()

def passing():
    for_left()
    move_right()
    move()
    first_huddle()
    turn_left()

for step in range(6):
    passing()
  
## Using WHile Loop
def move_right():
    turn_left()
    turn_left()
    turn_left()

def first_huddle():
    turn_left()
    turn_left()
    turn_left()
    move()

def for_left():
    move()
    turn_left()
    move()

def passing():
    for_left()
    move_right()
    move()
    first_huddle()
    turn_left()

while not at_goal():
    passing()




