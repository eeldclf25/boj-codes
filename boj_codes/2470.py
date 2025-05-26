import sys

def func(inputValue):
    solList = list(map(int, inputValue[1].split()))
    solList.sort()
    
    currentOne = None
    currentTwo = None
    start = 0
    end = len(solList) - 1
    
    while start < end:
        if (currentOne == None) or (abs(solList[start] + solList[end]) < abs(solList[currentOne] + solList[currentTwo])):
            currentOne = start
            currentTwo = end
            
        if 0 <= (solList[start] + solList[end]):
            end -= 1
        else:
            start += 1
    
    print(solList[currentOne], solList[currentTwo])


if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)