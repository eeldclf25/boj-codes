import sys
from collections import deque

def func(inputValue):
    rootNode = None
    binaryTree = {}
    for i in inputValue:
        if rootNode == None:
            binaryTree[i] = [None, None]
            rootNode = i
            continue
        currentNode = rootNode
        while True:
            if i < currentNode and binaryTree[currentNode][0] != None:
                currentNode = binaryTree[currentNode][0]
            elif i > currentNode and binaryTree[currentNode][1] != None:
                currentNode = binaryTree[currentNode][1]
            elif i < currentNode and binaryTree[currentNode][0] == None:
                binaryTree[i] = [None, None]
                binaryTree[currentNode][0] = i
                break
            elif i > currentNode and binaryTree[currentNode][1] == None:
                binaryTree[i] = [None, None]
                binaryTree[currentNode][1] = i
                break
    
    strList = []
    dfsStack = deque()
    dfsStack.append([rootNode, 0])
    while dfsStack:
        currentNode, seen = dfsStack.pop()
        if seen == 1:
            strList.append(currentNode)
            continue
        left, right = binaryTree[currentNode]
        dfsStack.append([currentNode, 1])
        if right != None:
            dfsStack.append([right, 0])
        if left != None:
            dfsStack.append([left, 0])
    
    for i in strList:
        print(i)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    inputValue = [int(i) for i in inputValue]
    func(inputValue)