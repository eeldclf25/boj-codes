import sys

def func(inputValue):
    x, y = map(int, inputValue[0].split())
    cutX = [0]
    cutY = [0]
    for i in range(int(inputValue[1])):
        sideCheck, value = map(int, inputValue[i + 2].split())
        if sideCheck == 1:
            cutX.append(value)
        else:
            cutY.append(value)
    cutX.append(x)
    cutY.append(y)
    cutX.sort()
    cutY.sort()
    
    maxArea = 0
    for i in range(len(cutX) - 1):
        leftX = cutX[i]
        RightX = cutX[i + 1]
        for ii in range(len(cutY) - 1):
            leftY = cutY[ii]
            RightY = cutY[ii + 1]
            area = (RightX - leftX) * (RightY - leftY)
            if maxArea < area:
                maxArea = area
    print(maxArea)
    
    

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)