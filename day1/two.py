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

def rotate(direction: str , num_to_move, current_position):
    c = current_position
    times_0 = 0
    if direction == 'L':
        for i in range(0, num_to_move):
            c = c - 1
            if c == 0:
                times_0 = times_0 + 1
            if c < 0:
                c = 99
    if direction == 'R':
        for i in range(0, num_to_move):
            c = c + 1
            if c > 99:
                c = 0
            if c == 0:
                times_0 = times_0 + 1

    return c,times_0

def solution(case):
    from utils import parse_input
    clean_input = parse_input(case)
    current_position = 50
    output = 0
    times_run = 0
    for i in clean_input:
        times_run = times_run + 1
        direction = i[0]
        clean = i.removeprefix("L")
        clean = clean.removeprefix("R")
        num_to_move = int(clean)
        c, o =  rotate(direction, num_to_move, current_position)
        current_position = c
        output = output + o

    print(output)

solution(case)