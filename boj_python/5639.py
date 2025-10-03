import sys
from collections import deque

def func(inputValue):
    rootNode = int(inputValue[0])
    frontTree = {}
    frontTree[rootNode] = [None, None]
    for i in range(1, len(inputValue)):
        value = int(inputValue[i])
        currentNode = rootNode
        while True:
            if frontTree[currentNode][0] != None and currentNode > value:
                currentNode = frontTree[currentNode][0]
            if frontTree[currentNode][1] != None and currentNode < value:
                currentNode = frontTree[currentNode][1]
            if frontTree[currentNode][0] == None and currentNode > value:
                frontTree[currentNode][0] = value
                frontTree[value] = [None, None]
                break
            if frontTree[currentNode][1] == None and currentNode < value:
                frontTree[currentNode][1] = value
                frontTree[value] = [None, None]
                break

    endResult = []
    endSearch = deque()
    endSearch.append([int(inputValue[0]), 0])
    while len(endSearch) != 0:
        node, check = endSearch.pop()
        if check == 1:
            endResult.append(node)
            continue
        left, right = frontTree[node]
        if check == 0:
            endSearch.append([node, 1])
        if right != None:
            endSearch.append([right, 0])
        if left != None:
            endSearch.append([left, 0])
    print('\n'.join(map(str, endResult)))

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)