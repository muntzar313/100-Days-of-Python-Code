# Using For Loop Hurdle 1
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
  
## Using While Loop Hurdle 2
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


## Hurdle 3
def move_right():
    turn_left()
    turn_left()
    turn_left()


def passing():
    turn_left()
    move()
    move_right()
    move()
    move_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        passing()
        
    else:
        move()
            
    passing()

#### Huddle 4

def move_right():
    turn_left()
    turn_left()
    turn_left()

    

def passing():
    turn_left()
    while wall_on_right():
        move()
    move_right()
    move()
    move_right()
    
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        passing()
    else:
        move()
            
    

            






