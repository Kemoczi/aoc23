import re

# dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
dict = {'eno': '1', 'owt': '2', 'eerht': '3', 'ruof': '4', 'evif': '5', 'xis': '6', 'neves': '7', 'thgie': '8', 'enin': '9'}


with open("input.txt") as puzzle:
    sol = []
    for line in puzzle.readlines():
        line = line[::-1]
        for key, value in dict.items():
            line = line.replace(key, value)
        line = line[::-1]
        line1 = re.sub("[^0-9]", "", line)
        sol.append(line1[0]+line1[-1])

    
    print(sol)
    # count = 0
    # for num in sol:
    #     count += int(num)

    # print("sum is: ", count)
