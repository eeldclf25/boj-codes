import sys
from collections import deque

def func(inputValue):
    binaryTree = {}
    for i in range(1, len(inputValue)):
        parentNode, leftNode, RightNode = map(str, inputValue[i].split())
        binaryTree[parentNode] = [leftNode, RightNode]
    
    # 스택으로 dfs 전위 순회
    frontStrList = []
    frontDfsStack = deque()
    frontDfsStack.append([inputValue[1][0], 0])
    while frontDfsStack:
        currentNode, seen = frontDfsStack.pop()
        if seen == 1:
            frontStrList.append(currentNode)
            continue
        left, right = binaryTree[currentNode]
        if right != '.':
            frontDfsStack.append([right, 0])
        if left != '.':
            frontDfsStack.append([left, 0])
        frontDfsStack.append([currentNode, 1])
    print(''.join(frontStrList))
    
    # 스택으로 dfs 중위 순회
    midStrList = []
    midDfsStack = deque()
    midDfsStack.append([inputValue[1][0], 0])
    while midDfsStack:
        currentNode, seen = midDfsStack.pop()
        if seen == 1:
            midStrList.append(currentNode)
            continue
        left, right = binaryTree[currentNode]
        if right != '.':
            midDfsStack.append([right, 0])
        midDfsStack.append([currentNode, 1])
        if left != '.':
            midDfsStack.append([left, 0])
    print(''.join(midStrList))
    
    # 스택으로 dfs 후위 순회
    endStrList = []
    endDfsStack = deque()
    endDfsStack.append([inputValue[1][0], 0])
    while endDfsStack:
        currentNode, seen = endDfsStack.pop()
        if seen == 1:
            endStrList.append(currentNode)
            continue
        left, right = binaryTree[currentNode]
        endDfsStack.append([currentNode, 1])
        if right != '.':
            endDfsStack.append([right, 0])
        if left != '.':
            endDfsStack.append([left, 0])
    print(''.join(endStrList))
    
    # (추가) 스택을큐로 바꾸는 것 만으로 bfs
    bfsStrList = []
    bfsStack = deque()
    bfsStack.append([inputValue[1][0], 0])
    while bfsStack:
        currentNode, seen = bfsStack.popleft()
        if seen == 1:
            bfsStrList.append(currentNode)
            continue
        left, right = binaryTree[currentNode]
        bfsStack.append([currentNode, 1])
        if right != '.':
            bfsStack.append([right, 0])
        if left != '.':
            bfsStack.append([left, 0])
    print(''.join(bfsStrList))

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)