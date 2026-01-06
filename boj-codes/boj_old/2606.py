import sys
from collections import deque

def func(inputValue):
    n, m, k, x = map(int, inputValue[0].split())
    
    nodeSet = set()
    graph = {}
    for i in range(1, n + 1):
        graph[i] = [None, []]
        nodeSet.add(i)
    
    for i in range(1, len(inputValue)):
        start, end = map(int, inputValue[i].split())
        graph[start][1].append(end)
    
    queue = deque()
    queue.append(x)
    nodeSet.remove(x)
    graph[x][0] = 0
    while queue:
        now = queue.popleft()
        currentCount = graph[now][0]
        for i in graph[now][1]:
            if i in nodeSet:
                nodeSet.remove(i)
                queue.append(i)
                graph[i][0] = currentCount + 1
    
    result = []
    for i in graph:
        if graph[i][0] == k:
            result.append(i)
    
    if len(result) == 0:
        print(-1)
    else:
        for i in result:
            print(i)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)