

dayNumber = 3
TESTING = True
TEST_AMOUNT = 5

fName = f'day_{str(dayNumber).zfill(2)}_input.txt'
directory = f'c:/Development/python/adventofcode2023/day_{str(dayNumber).zfill(2)}'
inputFile = f'{directory}/{fName}'

puzzle_array = []
with open(inputFile) as openFile:
    for line in openFile:
        # removing the game number from the input
        current_list = []
        line = line.strip()
        for item in line:
            current_list.append(item)
        
        puzzle_array.append(current_list)


if TESTING:
    LAST_ROW = TEST_AMOUNT
else:
    LAST_ROW = len(puzzle_array)


for row in range(LAST_ROW):
    puzzle_array[row]


       