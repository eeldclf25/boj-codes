import sys
from collections import deque

def func(inputValue):
    r, c = map(int, inputValue[0].split())
    
    root = []
    river = []
    teatree = []
    for i in range(1, len(inputValue)):
        temp = list(inputValue[i])
        for j in range(len(temp)):
            if temp[j] == 'S':
                root.append([i - 1, j])
                temp[j] = '0'
            elif temp[j] == '*':
                river.append([i - 1, j])
        teatree.append(temp)
    

    
    
    
    
    
    
    dirX = [1, 0, -1, 0]
    dirY = [0, 1, 0, -1]
    riverSet = set()
    sonicSet = set()
    queue = deque()
    for i in river:
        queue.append(i)
    queue.append(root[0])
    while queue:
        nowRaw, nowCol = queue.popleft()
        
        if teatree[nowRaw][nowCol] == '*':
            for i in range(4):
                checkCol = nowCol + dirX[i]
                checkRaw = nowRaw + dirY[i]
                if 0 <= checkRaw < r and 0 <= checkCol < c:
                    if teatree[checkRaw][checkCol] != 'D' and teatree[checkRaw][checkCol] == '.':
                        if not tuple([checkRaw, checkCol]) in riverSet:
                            teatree[checkRaw][checkCol] = '*'
                            riverSet.add(tuple([checkRaw, checkCol]))
                            queue.append([checkRaw, checkCol])
        else:
            count = int(teatree[nowRaw][nowCol]) + 1
            
            for i in range(4):
                checkCol = nowCol + dirX[i]
                checkRaw = nowRaw + dirY[i]
                if 0 <= checkRaw < r and 0 <= checkCol < c:
                    if teatree[checkRaw][checkCol] == '.':
                        if not tuple([checkRaw, checkCol]) in sonicSet:
                            teatree[checkRaw][checkCol] = f'{count}'
                            sonicSet.add(tuple([checkRaw, checkCol]))
                            queue.append([checkRaw, checkCol])
                    elif teatree[checkRaw][checkCol] == 'D':
                        print(count)
                        queue = None
                        break
    if queue != None:
        print('KAKTUS')
                    

        
    

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)