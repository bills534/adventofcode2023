

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
power_list = []
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

        # for each game we reset the min color count dict
        min_rgb = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        # since we have to times the min color amount together for each game we start at 1
        game_color_total = 1

        # creating the sublist of games
        subGames = line.split(';')
        for game in subGames:
            rgb = {
                'red': 0,
                'green': 0,
                'blue': 0
            }

            # for each individual draw from the bag of cubes
            draws = game.split(',')
            for draw in draws:
                current_draw_value = int(draw.strip().split(' ')[0])
                current_draw_color = draw.strip().split(' ')[1]
                rgb[current_draw_color] += int(current_draw_value)

                # placing the value into the dict when appropriate
                if current_draw_value > min_rgb[current_draw_color]:
                    min_rgb[current_draw_color] = current_draw_value

        for color in min_rgb:
            game_color_total *= min_rgb[color]

        print(min_rgb, game_color_total)
        power_list.append(game_color_total)

        if TESTING:
            if gameNumber >= TEST_AMOUNT:
                break

        print(f'----gnum:{gameNumber} - {game_color_total}')
        gameNumber += 1

for power in power_list:
    result += power

print(f'final: {result}')