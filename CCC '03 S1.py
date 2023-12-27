snakesLadders = {
    9: 34,
    40: 64,
    67: 86,
    99: 77,
    90: 48,
    54: 19
}

currentPos = 1
while True:
    orginalPos = currentPos

    move = int(input())
    if move == 0:
        print("You Quit!")
        break

    currentPos += move

    if currentPos in snakesLadders.keys():
        currentPos = snakesLadders[currentPos]

    if currentPos > 100:
        currentPos = orginalPos

    print("You are now on square", currentPos)

    if currentPos == 100:
        print("You Win!")
        break
