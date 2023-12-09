

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


def findDigit(inputString: str):
    '''Finds and returns the first digit in a string'''
    outputInt = 0
    for char in inputString:
        if char.isdigit():
            outputInt = int(char)
            break
    
    return outputInt

def newConvert(inputString: str, replacements: dict, reversed: bool):
    '''Takes an input string scans from one side to the other checking to see if any written out numbers are found
        then replaces them with digits'''
    test_string = ''
    raw_string = ''
    output = ''

    if not reversed:
        # add each character of the string 1 by 1 and test each time for replacements
        for char in inputString:
            test_string += char
            raw_string += char  # saving this new string twice to test if it gets changed
            for old, new in replacements.items():
                test_string = test_string.replace(old, new)
                if test_string != raw_string:
                    output = findDigit(test_string)
                    break
    else:
        # add each character of the string 1 by 1 and test each time for replacements
        inputString = inputString[::-1]
        for char in inputString:
            test_string += char
            raw_string += char  # saving this new string twice to test if it gets changed
            for old, new in replacements.items():
                test_string = test_string.replace(old[::-1], new)
                if test_string != raw_string:
                    output = findDigit(test_string)
                    break

    return output


with open(inputFile) as openFile:
    for dirty_line in openFile:

        firstNumber = str(newConvert(dirty_line.strip(), replace_dict, False))
        secondNumber = str(newConvert(dirty_line.strip(), replace_dict, True))

        if firstNumber == '':
            firstNumber = findDigit(dirty_line.strip())
            secondNumber = findDigit(dirty_line.strip()[::-1])

        checksumCombined = f'{firstNumber}{secondNumber}'
        checksumList.append(checksumCombined)
        count += 1

        print(f'{dirty_line.strip()}; {checksumCombined}')


for checknum in checksumList:
    result += int(checknum)

print(f'count: {count}')
print(result)