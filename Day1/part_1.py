import re

filePath = 'Day1\input'
calibrationValues = []

with open(filePath) as f:
    line = f.readline()
    while line:
        lineDigits = re.findall('\d', line)
        print(lineDigits)
        lineValue = str(lineDigits[0]) + str(lineDigits[-1])
        print(lineValue)
        calibrationValues.append(int(lineValue))
        line = f.readline()

print(sum(calibrationValues))