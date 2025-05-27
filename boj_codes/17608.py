import sys

def func(inputValue):
    stack = []
    for i in range(1, len(inputValue)):
        stack.append(int(inputValue[i]))
    
    maxHeight = 0
    count = 0
    while 0 < len(stack):
        currentHeight = stack.pop()
        if maxHeight < currentHeight:
            count += 1
            maxHeight = currentHeight
    print(count)
        
        

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)