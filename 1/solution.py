import re

def make_number(string):

    dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    dict_rev = {'eno': '1', 'owt': '2', 'eerht': '3', 'ruof': '4', 'evif': '5', 'xis': '6', 'neves': '7', 'thgie': '8', 'enin': '9'}
    indices = []

    if any(re.search(key, string) for key in dict.keys()):

        for pattern, number in dict.items():
            indices.append(string.find(pattern))
                
        min = None
        min_ind = None

        for index, number in enumerate(indices):
            if number >= 0 and (min is None or number < min):
                min = number
                min_ind = index
                
        if min_ind is not None:
            s_left = re.sub(list(dict.keys())[min_ind], list(dict.values())[min_ind], string)
            left_nums = re.sub("[^0-9]", "", s_left)
            left = left_nums[0]

        indices = []
        for pattern, number in dict_rev.items():       
            indices.append(string[::-1].find(pattern))
            

        min = None
        min_ind = None

        for index, number in enumerate(indices):
            if number >= 0 and (min is None or number < min):
                min = number
                min_ind = index
                
            
        if min_ind is not None:
            s_right = re.sub(list(dict.keys())[min_ind], list(dict.values())[min_ind], string)
            right_nums = re.sub("[^0-9]", "", s_right)
            right = right_nums[-1]
            
        number = left+right
        
        return number
    
    string_numbers = re.sub("[^0-9]", "", string)
    number = string_numbers[0] + string_numbers[-1]
    return number


if __name__ == '__main__':

    with open("1/input.txt") as puzzle:
        sol = []
        for line in puzzle.readlines():
            sol.append(make_number(line))
        
    print(sol)
    count = 0

    for num in sol:
        count += int(num)

    print("UGUEM: ", count)
