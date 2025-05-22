import sys

totalCount = 0
check = []

def func(inputValue):
    n = int(inputValue[0])
    
    queenPossible(0, 0, n, n, n)
    print(totalCount)

def queenPossible(currentX, currentY, MaxX, MaxY, deep):
    global totalCount
    
    if deep == 0:
        totalCount += 1
        return
    if currentY == MaxY:
        return
    # if currentX == MaxX:
    #     print('is action!!')
    #     return
    
    for moveingX in range(MaxX):
        if moveingX not in check:
            if diagCheck(currentY, moveingX):
                check.append(moveingX)
                queenPossible(0, currentY + 1, MaxX, MaxY, deep - 1)
                check.pop()
    
        
        # if not len(check):
        #     check.append(currentY)
        #     queenPossible(0, currentY + 1, MaxX, MaxY, deep - 1)
        # else:
        #     isPossible = True
        #     for queenX, queenY in queenArray:
        #         if not spaceCheck(queenX, queenY, i, currentY):
        #             isPossible = False
        #             break
        #     if isPossible == True:
        #         queenPossible(0, currentY + 1, MaxX, MaxY, deep - 1)
          
def diagCheck(checkX, checkY):
    for j in range(len(check)):
        if abs(j - checkX) == abs(check[j] - checkY):
            return False
    return True

def spaceCheck(queenX, queenY, spaceX, spaceY):
    if spaceY == queenY:
        return False
    elif spaceX == queenX:
        return False
    else:
        movequeenX = 0
        movequeenY = 0
        if queenX >= spaceX:
            movequeenX = queenX - spaceX
        else:
            movequeenX = spaceX - queenX
        if queenY >= spaceY:
            movequeenY = queenY - spaceY
        else:
            movequeenY = spaceY - queenY
        if movequeenY == movequeenX:
            return False
        else:
            return True

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)