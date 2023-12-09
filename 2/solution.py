import re

def check_game(game):
    quantities = re.findall(r"\d+ \w+", game)

    mezzanine = []
    for item in quantities:
        mezzanine.append(item[2::].strip())
        mezzanine.append(int(item[0:2]))   

    tuples = []
    for i in range(0, len(mezzanine)-1, 2):
        tuples.append((mezzanine[i], mezzanine[i+1]))

    red = []
    blue = []
    green = []

    for item in tuples:
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
                game_id = re.search(r"\d+", line)
                GAMES.append(line[game_id.span()[0]:game_id.span()[1]])
            else:
                continue
UGUEM = 0
for game in GAMES:
    UGUEM += int(game)
    
print("UGUEM: ", UGUEM)