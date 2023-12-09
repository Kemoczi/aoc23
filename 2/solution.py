import re

def check_game(game):

    quantities = re.findall(r"\d+ \w+", game)

    meta_list = []
    for item in quantities:
        meta_list.append(item[2::].strip())
        meta_list.append(int(item[0:2]))   

    tuples_list = []
    for i in range(0, len(meta_list)-1, 2):
        tuples_list.append((meta_list[i], meta_list[i+1]))

    red = []
    blue = []
    green = []

    for item in tuples_list:
        if item[0] == 'red':
            red.append(item[1])
        elif item[0] == 'blue':
            blue.append(item[1])
        elif item[0] == 'green':
            green.append(item[1])

    if any(i > 12 for i in red) or any(i > 14 for i in blue) or any(i > 13 for i in green):
        return False
    else:
        return True


if __name__ == '__main__':
    
    GAMES = []

    with open("2/input.txt") as puzzle:

        for line in puzzle.readlines():
            if check_game(line):
                dupa = re.search(r"\d+", line)
                GAMES.append(line[dupa.span()[0]:dupa.span()[1]])
            else:
                continue

uguem = 0

for game in GAMES:
    uguem += int(game)

print("UGUEM: ", uguem)