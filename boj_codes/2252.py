import sys
from collections import deque

def func(inputValue):
    n, m = map(int, inputValue[0].split())
    
    graph = {}
    for i in range(1, n + 1):
        graph[i] = [0, []]
    
    for i in range(1, len(inputValue)):
        start, end = map(int, inputValue[i].split())
        graph[start][1].append(end)
        graph[end][0] += 1

    result = []
    queue = deque()
    for key, value in graph.items():
        if value[0] == 0:
            queue.append(key)
    while queue:
        nowKey = queue.popleft()
        result.append(nowKey)
        for value in graph[nowKey][1]:
            graph[value][0] -= 1
            if graph[value][0] <= 0:
                queue.append(value)

    print(' '.join(map(str, result)))

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)