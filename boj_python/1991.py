import sys
from collections import deque

def func(inputValue):
    tree = {}
    for i in range(1, len(inputValue)):
        root, left, right = map(str, inputValue[i].split())
        tree[root] = left, right
    
    frontResult = []
    frontSearch = deque()
    frontSearch.append(['A', 0])
    while len(frontSearch) != 0:
        node, check = frontSearch.pop()
        if check == 1:
            frontResult.append(node)
            continue
        left, right = tree[node]
        if right != '.':
            frontSearch.append([right, 0])
        if left != '.':
            frontSearch.append([left, 0])
        if check == 0:
            frontSearch.append([node, 1])
    print(''.join(frontResult))

    midResult = []
    midSearch = deque()
    midSearch.append(['A', 0])
    while len(midSearch) != 0:
        node, check = midSearch.pop()
        if check == 1:
            midResult.append(node)
            continue
        left, right = tree[node]
        if right != '.':
            midSearch.append([right, 0])
        if check == 0:
            midSearch.append([node, 1])
        if left != '.':
            midSearch.append([left, 0])
    print(''.join(midResult))


    endResult = []
    endSearch = deque()
    endSearch.append(['A', 0])
    while len(endSearch) != 0:
        node, check = endSearch.pop()
        if check == 1:
            endResult.append(node)
            continue
        left, right = tree[node]
        if check == 0:
            endSearch.append([node, 1])
        if right != '.':
            endSearch.append([right, 0])
        if left != '.':
            endSearch.append([left, 0])
    print(''.join(endResult))






if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)