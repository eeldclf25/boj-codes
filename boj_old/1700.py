import sys

def func(inputValue):
    n, k = map(int, inputValue[0].split())
    useList = list(map(int, inputValue[1].split()))
    
    
    
    currentConcent = []
    undoCount = 0
    for _ in range(len(useList)):
        if useList[0] in currentConcent:
            useList.pop(0)
            continue
        if len(currentConcent) < n:
            currentConcent.append(useList.pop(0))
            continue
        
        popList = currentConcent.copy()
        for i in range(len(useList)):
            if len(popList) == 1:
                break
            if useList[i] in popList:
                popList.remove(useList[i])
        
        currentConcent.remove(popList[0])
        currentConcent.append(useList.pop(0))
        undoCount += 1

    print(undoCount)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)