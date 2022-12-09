import copy
liste = open('notcal.txt', 'r')

headPosition = [0,0]
tailPosition = [0,0]
oldPositionOfHead = headPosition
alreadyVisited = [[0,0]]
headTrail = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
oldTrailPosition = headTrail.copy()
alreadyVisitedTrail = [[0,0]]

def is_touching(headPos, tailPos):
    if abs(headPos[0] - tailPos[0]) <=1 and abs(headPos[1] - tailPos[1]) <= 1:
        return True
    else:
        return False

def is_diagonal(pos1, pos2):
    return (pos1[0] != pos2[0]) and (pos1[1] != pos2[1])

def get_diagonal_direction(oldPos, newPos):
    xPosition = 0
    yPosition = 0
    if newPos[0] - oldPos[0] > 0 :
        xPosition = 1
    else:
        xPosition = -1
    if newPos[1] - oldPos[1] > 0:
        yPosition = 1
    else:
        yPosition = -1
    return [xPosition, yPosition]



def move_trail():
    global headTrail
    global headPosition
    global oldTrailPosition
    global alreadyVisitedTrail
    for index, element in enumerate(headTrail):
        if index == 0:
            if not is_touching(headPosition, element):
                oldTrailPosition[index] = element.copy()
                headTrail[index] = oldPositionOfHead.copy()
        else:
            if not is_touching(headTrail[index-1], element):
                if is_diagonal(headTrail[index-1], oldTrailPosition[index-1]):
                    oldTrailPosition[index] = element.copy()
                    diagonalVector = get_diagonal_direction(oldTrailPosition[index-1], headTrail[index-1])
                    if headTrail[index-1][0] != element[0]:
                        headTrail[index][0] = element[0] + diagonalVector[0]
                    if headTrail[index-1][1] != element[1]:
                        headTrail[index][1] = element[1] + diagonalVector[1]
                    if index == 8 and (headTrail[index] not in alreadyVisitedTrail):
                        alreadyVisitedTrail += [headTrail[index].copy()]
                else:
                    oldTrailPosition[index] = element.copy()
                    headTrail[index] = oldTrailPosition[index-1].copy()
                    if index == 8 and (headTrail[index] not in alreadyVisitedTrail):
                        alreadyVisitedTrail += [headTrail[index].copy()]



def move_up():
    global headPosition
    global tailPosition
    global oldPositionOfHead
    global alreadyVisited
    oldPositionOfHead = headPosition.copy()
    headPosition[1] = headPosition[1] + 1
    if not is_touching(headPosition, tailPosition):
        tailPosition = oldPositionOfHead.copy()
        if tailPosition not in alreadyVisited:
            alreadyVisited.append(tailPosition)

def move_down():
    global headPosition
    global tailPosition
    global oldPositionOfHead
    global alreadyVisited
    oldPositionOfHead = headPosition.copy()
    headPosition[1] = headPosition[1] - 1
    if not is_touching(headPosition, tailPosition):
        tailPosition = oldPositionOfHead.copy()
        if tailPosition not in alreadyVisited:
            alreadyVisited.append(tailPosition)

def move_left():
    global headPosition
    global tailPosition
    global oldPositionOfHead
    global alreadyVisited
    oldPositionOfHead = headPosition.copy()
    headPosition[0] = headPosition[0] - 1
    if not is_touching(headPosition, tailPosition):
        tailPosition = oldPositionOfHead.copy()
        if tailPosition not in alreadyVisited:
            alreadyVisited.append(tailPosition)

def move_right():
    global headPosition
    global tailPosition
    global oldPositionOfHead
    global alreadyVisited
    oldPositionOfHead = headPosition.copy()
    headPosition[0] = headPosition[0] + 1
    if not is_touching(headPosition, tailPosition):
        tailPosition = oldPositionOfHead.copy()
        if tailPosition not in alreadyVisited:
            alreadyVisited.append(tailPosition)



for item in liste.readlines():
    currentInput = item.replace('\n', '').split(' ')
    if currentInput[0] == 'R':
        for moveCount in range(int(currentInput[1])):
            move_right()
            move_trail()
    elif currentInput[0] == 'L':
        for moveCount in range(int(currentInput[1])):
            move_left()
            move_trail()
    elif currentInput[0] == 'U':
        for moveCount in range(int(currentInput[1])):
            move_up()
            move_trail()
    elif currentInput[0] == 'D':
        for moveCount in range(int(currentInput[1])):
            move_down()
            move_trail()



print(len(alreadyVisited))
count = 0
for i in alreadyVisitedTrail:
    count += 1
print(count)