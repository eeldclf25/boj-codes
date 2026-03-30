import sys
from collections import deque

def func(inputValue):
    nodeSet = set()
    graph = {}
    n, _ = map(int, inputValue[0].split())
    for i in range(1, n + 1):
        graph[i] = []
        nodeSet.add(i)
    
    for i in range(1, len(inputValue)):
        start, end = map(int, inputValue[i].split())
        graph[start].append(end)
        graph[end].append(start)
    
    count = 0
    while nodeSet:
        start = nodeSet.pop()
        queue = deque()
        queue.append(start)
        while queue:
            now = queue.popleft()
            for i in graph[now]:
                if i in nodeSet:
                    nodeSet.remove(i)
                    queue.append(i)
        count += 1
    
    print(count)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)