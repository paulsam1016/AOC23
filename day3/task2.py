import re
from os import path

location = path.dirname(path.realpath(__file__))

f = open(file=f"{location}/input.txt")
lines = f.readlines()

# ex = '''467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..'''
#
# lines = ex.split('\n')


gearRatio = 0

for rowIndex, line in enumerate(lines):
    string = line.rstrip()
    matches = list(re.finditer(r'\*', string))
    for match in matches:
        lineLength = len(string)
        index = match.start()
        numbers = []

        # print(f'match:          {match}')
        # print(f'lineLength:     {lineLength}')
        # print(f'match index:    {index}')

        for r in [rowIndex - 1, rowIndex, rowIndex + 1]:
            if -1 < r < len(lines):
                searchLine = lines[r].rstrip()
                # print(searchLine)
                for c in range(index - 1, index + 2):
                    if -1 < c < len(searchLine) and not searchLine[c] == '.' and not searchLine[c] == '*':
                        # print('||||||||FOUND||||||||')
                        # print(f'Found at:       {c}')
                        l = c
                        r = c
                        while l > 0 and searchLine[l - 1].isdigit():
                            l -= 1
                        while r < len(searchLine) and searchLine[r].isdigit():
                            r += 1
                        # print(f'Start at:       {l}')
                        # print(f'Got:            {searchLine[l:r]}')
                        if not [r, l, searchLine[l:r]] in numbers:      # Or use dict [defaultdict(list)]
                            numbers.append([r, l, searchLine[l:r]])

        if len(numbers) != 2:
            # print('------------------------')
            continue

        gearRatio += int(numbers[0][2]) * int(numbers[1][2])
        # print('------------------------')

print(f'sum : {gearRatio}')