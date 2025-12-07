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
