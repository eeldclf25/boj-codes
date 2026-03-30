import sys
from collections import deque

def func(inputValue):
    n, m = map(int, inputValue[0].split())
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    
    roundMap = []
    for i in range(1, len(inputValue)):
        miro = inputValue[i]
        miro = miro.replace('1', '*')
        miro = miro.replace('0', '@')
        roundMap.append(list(miro))
    roundMap[0][0] = 1
    roundMap[n - 1][m - 1] = 'E'

    nodeSet = set()
    queue = deque()
    nodeSet.add(tuple([0, 0]))
    queue.append([0, 0])
    while queue:
        now = queue.popleft()
        count = roundMap[now[0]][now[1]]
        
        for i in range(4):
            checkRow = now[0] + dy[i]
            checkCol = now[1] + dx[i]
            if 0 <= checkRow < n and 0 <= checkCol < m:
                if roundMap[checkRow][checkCol] == '*':
                    nodeSet.add(tuple([checkRow, checkCol]))
                    queue.append([checkRow, checkCol])
                    roundMap[checkRow][checkCol] = count + 1
                elif roundMap[checkRow][checkCol] == 'E':
                    nodeSet.add(tuple([checkRow, checkCol]))
                    print(count + 1)
                    return


if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)