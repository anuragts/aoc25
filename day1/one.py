"""
Dial starts at 50
L means to go to left
R means to go to right
Dial has number from 0 to 99
and if we got left of 0 then we will start from 99 as its circle, same for opposite 99 -> 0
We need to find password that is times dial is left pointing at 0. aka [0,0,0] -> 3 is password
"""


case = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82

"""

def parse_input(case):
    stripped = case.splitlines()
    b = []
    for i in stripped:
        i.strip()
        if i == '':
            continue
        else:
            b.append(i)
    return b


def rotate(direction: str , num_to_move, current_position):
    c = current_position
    times_loop_moved = 0
    if direction == 'L':
        for i in range(0, num_to_move):
            times_loop_moved += 1
            c = c - 1
            if c < 0:
                c = 99
    if direction == 'R':
        for i in range(0, num_to_move):
            c = c + 1
            if c > 99:
                c = 0

    return c

def solution(case):
    clean_input = parse_input(case)
    current_position = 50
    no_of_times_reached = 0
    times_run = 0
    for i in clean_input:
        times_run = times_run + 1
        direction = i[0]
        clean = i.removeprefix("L")
        clean = clean.removeprefix("R")
        num_to_move = int(clean)
        output = rotate(direction, num_to_move, current_position)
        current_position = output
        if output == 0:
            no_of_times_reached += 1

    print(no_of_times_reached)




solution(case)