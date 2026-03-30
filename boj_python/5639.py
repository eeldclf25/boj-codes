import sys
sys.setrecursionlimit(10100)

def func(inputValue):
    rootNode = inputValue[0]
    left = None
    right = None
    for i in range(0, len(inputValue)):
        if left == None and rootNode > inputValue[i]:
            left = i
        if right == None and rootNode < inputValue[i]:
            right = i
    
    if left != None:
        if right != None:
            func(inputValue[left:right])
        else:
            func(inputValue[left:len(inputValue)])
    if right != None:
        func(inputValue[right:len(inputValue)])
    
    print(rootNode)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(list(map(int, inputValue)))