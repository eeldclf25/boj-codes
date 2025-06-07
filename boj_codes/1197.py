import sys
from collections import deque



parent = None
rank   = None

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1
    return True

def func(inputValue):
    maxVertex, _ = map(int, inputValue.pop(0).split())
    sortEdges = sorted(inputValue, key = lambda x : int(x.split()[2]))
    global parent
    global rank
    parent = list(range(maxVertex + 1))
    rank   = [0] * (maxVertex + 1)
    
    totalWeight = 0
    totalVertex = 0
    checkVertex = {}
    for i in range(len(sortEdges)):        
        front, end, weight = map(int, sortEdges[i].split())
        if union(front, end):
            totalWeight += weight
            totalVertex += 1
            if maxVertex - 1 == totalVertex:
                break

    print(totalWeight)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)