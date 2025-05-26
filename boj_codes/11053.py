import sys

count = 0


def func(inputValue):
    a = int(inputValue[0])
    valueList = list(map(int, inputValue[1].split()))
    
    Recursion(valueList, 0, 0, 0)
    print(count)
    
    
    
    
def Recursion(valueList, currentValue, currentCount, currentIndex):
    global count
    
    if currentValue < valueList[currentIndex]:
        currentCount += 1
        currentValue = valueList[currentIndex]
        if count < currentCount:
            count = currentCount
    else:
        return
    
    for i in range(currentIndex, len(valueList) - 1):
        Recursion(valueList, currentValue, currentCount, i + 1)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)