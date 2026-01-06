import sys
from collections import deque

minCount = None

def func(inputValue):
    n, k = map(int, inputValue[0].split())
    coinList = []
    for i in range(1, len(inputValue)):
        coinList.append(int(inputValue[i]))
    coinList.sort(reverse=True)
    
    
    dp ={}
    minCount = None
    queue = deque()
    queue.append([set(), 0])
    while queue:
        now = queue.pop()
        for i in coinList:
            if now[0] in dp:
                break
            
            
            
            newList = []
            newList.append(now[0] + i)
            newList.append(now[1] + 1)
            
            if newList[0] < k:
                queue.append(newList)
            elif minCount == None or newList[0] == k and minCount > newList[1]:
                minCount = newList[1]
        
    print(minCount)
        

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)