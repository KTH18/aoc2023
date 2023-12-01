import re

filePath = 'Day1\input'
#filePath = 'Day1\\test'

calibrationValues = []
numberLookup = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
    "1": '1',
    "2": '2',
    "3": '3',
    "4": '4',
    "5": '5',
    "6": '6',
    "7": '7',
    "8": '8',
    "9": '9'
}
pattern = '(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)'

with open(filePath) as f:
    line = f.readline()
    while line:
        bestFirstScore = 100
        firstValue = ''
        bestLastScore = -100
        lastValue = ''

        for key, value in numberLookup.items():
            firstScore = line.find(key)
            lastScore = line.rfind(key)

            if firstScore != -1 and firstScore < bestFirstScore:
                bestFirstScore = firstScore
                firstValue = value

            if lastScore != -1 and lastScore > bestLastScore:
                bestLastScore = lastScore
                lastValue = value
    
        calibrationValues.append(int(firstValue + lastValue))
            
        line = f.readline()

print(calibrationValues)
print(sum(calibrationValues))