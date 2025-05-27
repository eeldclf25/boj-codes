import sys

def func(inputValue):
    towerList = list(map(int, inputValue[1].split()))
    stackList = []
    
    for i in range(len(towerList) - 1, -1, -1):
        while len(stackList) != 0 and towerList[i] > stackList[-1][1]:
            towerList[stackList[-1][0]] = i + 1
            stackList.pop()
        stackList.append([i, towerList[i]])
    
    for i in stackList:
        towerList[i[0]] = 0
    
    
    string = ' '.join(map(str, towerList))
    print(string)
        

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)