filePath = 'Day2\input'
#filePath = 'Day2\\test.txt'

TOTAL_RED_CUBES = 12
TOTAL_GREEN_CUBES = 13
TOTAL_BLUE_CUBES = 14

games= {}
sumPossibleGameIds = 0

with open(filePath) as f:
    line = f.readline()
    while line:
        lineSeperated = line.replace("\n", "").split(': ')
        gameId = lineSeperated[0].replace("Game ", "")
        gamePulls = lineSeperated[1].split("; ")

        gamePossible = True
        games[gameId] = "possible"

        for pull in gamePulls:
            if gamePossible == False:
                break

            pullCubes = pull.split(", ")

            for value in pullCubes:
                valueSplit = value.split(" ")
                cubeColour = valueSplit[1]
                cubeCount = int(valueSplit[0])
                match cubeColour:
                    case "red":
                        if cubeCount > TOTAL_RED_CUBES:
                            print("Game", gameId, "not possible as", value, "greater than total possible:", TOTAL_RED_CUBES)
                            gamePossible = False
                            games[gameId] = "impossible"
                            break
                    case "green":
                        if cubeCount > TOTAL_GREEN_CUBES:
                            print("Game", gameId, "not possible as", value, "greater than total possible:", TOTAL_GREEN_CUBES)
                            games[gameId] = "impossible"
                            gamePossible = False
                            break
                    case "blue":
                        if cubeCount > TOTAL_BLUE_CUBES:
                            print("Game", gameId, "not possible as", value, "greater than total possible:", TOTAL_BLUE_CUBES)
                            games[gameId] = "impossible"
                            gamePossible = False
                            break
        
        if gamePossible:
            sumPossibleGameIds = sumPossibleGameIds + int(gameId)
        
        line = f.readline()
        
print(games)
print(sumPossibleGameIds)