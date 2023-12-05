

dayNumber = 1

inputFile = f'day_{str(dayNumber).zfill(2)}_input.txt'

checksumList = []
result = 0

def findDigit(inputString):
    outputInt = 0
    for char in inputString:
        if char.isdigit():
            outputInt = int(char)
            break
    
    return outputInt


with open(inputFile) as openFile:
    for line in openFile:
        print(line.strip())
        firstNumber = 0
        secondNumber = 0

        firstNumber = str(findDigit(line))
        secondNumber = str(findDigit(line[::-1]))

        checksumCombined = f'{firstNumber}{secondNumber}'
        checksumList.append(checksumCombined)


for checknum in checksumList:
    result += int(checknum)

print(result)