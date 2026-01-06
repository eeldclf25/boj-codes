import sys
from collections import deque

def func(inputValue):
    n, m, v = map(int, inputValue[0].split())
    dic = {}
    dic[v] = []
    for i in range(1, len(inputValue)):
        start, end = map(int, inputValue[i].split())
        if not dic.get(start):
            dic[start] = []
        if not dic.get(end):
            dic[end] = []
        dic[start].append(end)
        dic[end].append(start)

    dfsVisable = set()
    dfsStr = []
    stack = deque()
    stack.append(v)
    while stack:
        now = stack.pop()
        if not now in dfsVisable:
            dfsVisable.add(now)
            dfsStr.append(now)
            dfsList = dic[now]
            dfsList.sort()
            dfsList.reverse()
            for i in dfsList:
                if not i in dfsVisable:
                    stack.append(i)
    
    print(' '.join(map(str, dfsStr)))
    
    bfsVisable = set()
    bfsStr = []
    queue = deque()
    queue.append(v)
    bfsVisable.add(v)
    while queue:
        now = queue.popleft()
        bfsStr.append(now)
        adjList = dic[now]
        adjList.sort()
        for i in adjList:
            if not i in bfsVisable:
                queue.append(i)
                bfsVisable.add(i)
    
    print(' '.join(map(str, bfsStr)))
    
    
        

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)