def getNextPosition(position, action):
    x = position[0]
    y = position[1]

    dx = action.value[0]
    dy = action.value[1]

    newX = x + dx
    newY = y + dy

    newPosition = (newX, newY)

    return newPosition