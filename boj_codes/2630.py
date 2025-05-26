import sys

white = 0
blue = 0

def func(inputValue):
    n = int(inputValue[0])
    paperList = [list(map(int, inputValue[row].split())) for row in range(1, n + 1)]
    
    recursion(paperList, 0, 0, n, n)
    
    print(white)
    print(blue)

def recursion(paperList, leftX, leftY, RightX, RightY):
    global blue
    global white
    
    if leftX + 1 == RightX:
        paper = paperList[leftY][leftX]
        if paper == 1:
            blue += 1
            return
        else:
            white += 1
            return
    
    isCheck = True
    checkPaper = paperList[leftY][leftX]
    for i in range(leftY, RightY):
        if isCheck == False: break
        for ii in range(leftX, RightX):
            if checkPaper != paperList[i][ii]:
                isCheck = False
                break
        
    if isCheck == True:
        if checkPaper == 1:
            blue += 1
            return
        else:
            white += 1
            return
    
    recursion(paperList, leftX, leftY, (leftX + RightX) //2, (leftY + RightY) //2)
    recursion(paperList, leftX, (leftY + RightY) //2, (leftX + RightX) //2, RightY)
    recursion(paperList, (leftX + RightX) //2, leftY, RightX, (leftY + RightY) //2)
    recursion(paperList, (leftX + RightX) //2, (leftY + RightY) //2, RightX, RightY)
    
    
    
    
    
    
if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)