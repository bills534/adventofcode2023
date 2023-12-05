

dayNumber = 1

inputFile = f'day_{str(dayNumber).zfill(2)}/day_{str(dayNumber).zfill(2)}_input.txt'

checksumList = []
result = 0
count = 0
replace_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def findDigit(inputString):
    outputInt = 0
    for char in inputString:
        if char.isdigit():
            outputInt = int(char)
            break
    
    return outputInt

# this needs to be able to convert the line in reverse too somehow
def convertNumbers(inputString, replacements, reversed):
    
    for old, new in replacements.items():
        if reversed:
            inputString = inputString[::-1].replace(old[::-1], new)
            return inputString[::-1]
        else:
            inputString = inputString.replace(old, new)
            return inputString


with open(inputFile) as openFile:
    for dirty_line in openFile:
        line = convertNumbers(dirty_line.strip(), replace_dict, False)
        line_reversed = convertNumbers(dirty_line.strip(), replace_dict, True)
        
        firstNumber = 0
        secondNumber = 0

        firstNumber = str(findDigit(line))
        secondNumber = str(findDigit(line_reversed[::-1]))

        checksumCombined = f'{firstNumber}{secondNumber}'
        checksumList.append(checksumCombined)
        count += 1

        print(f'{dirty_line.strip()}; {line}; {line_reversed} - {checksumCombined}')


for checknum in checksumList:
    result += int(checknum)

print(f'count: {count}')
print(result)