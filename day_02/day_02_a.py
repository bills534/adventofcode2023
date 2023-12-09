

dayNumber = 2
TESTING = False
TEST_AMOUNT = 5

fName = f'day_{str(dayNumber).zfill(2)}_input.txt'
directory = f'c:/Development/python/adventofcode2023/day_{str(dayNumber).zfill(2)}'
inputFile = f'{directory}/{fName}'
# cube input
INPUT_CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}
result = 0
gameNumber = 1

def validCubes(inCubes: dict, testCubes: dict):
    '''Checks one dict of RGB values against another to see if the test values are greater than possible'''
    result = True
    for color in inCubes:
        if testCubes[color] > inCubes[color]:
            result = False
    return result

with open(inputFile) as openFile:
    for line in openFile:
        # removing the game number from the input
        line = line.strip().replace(f'Game {gameNumber}: ', '')
        print(line)
        gamePossible = True

        subGames = line.split(';')

        for game in subGames:
            rgb = {
                'red': 0,
                'green': 0,
                'blue': 0
            }
            # print(f'={game.strip()}')

            draws = game.split(',')
            for draw in draws:
                current_draw_value = draw.strip().split(' ')[0]
                current_draw_color = draw.strip().split(' ')[1]
                # print(f"--{current_draw_color}: {current_draw_value}")
                rgb[current_draw_color] += int(current_draw_value)

            print(rgb)
            if not validCubes(INPUT_CUBES,rgb):
                gamePossible = False


        if gamePossible:
            result += gameNumber

        if TESTING:
            if gameNumber >= TEST_AMOUNT:
                break

        
        print(f'----gnum:{gameNumber} - {result}')
        gameNumber += 1
print(f'final: {result}')