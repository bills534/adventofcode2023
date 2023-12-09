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
    out_string = ''
    for old, new in replacements.items():
        if reversed:
            inputString = inputString[::-1].replace(old[::-1], new)
            inputString = inputString[::-1]
        else:
            inputString = inputString.replace(old, new)

    
    return inputString


def newConvert(inputString, replacements, reversed):
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




print(newConvert('kkeightwo6975six', replace_dict, False))
print(newConvert('kkeightwo6975six', replace_dict, True))


print(newConvert('jjpngnpzglkbltbrv2tjmqrpb', replace_dict, False))
print(newConvert('jjpngnpzglkbltbrv2tjmqrpb', replace_dict, True))