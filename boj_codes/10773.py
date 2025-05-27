import sys

def func(inputValue):
    stackList = []
    
    for i in range(1, len(inputValue)):
        if int(inputValue[i]) == 0:
            if len(stackList) == 0:
                stackList.append(int(inputValue[i]))
            else:
                stackList.pop()
        else:
            stackList.append(int(inputValue[i]))
            
    sum = 0
    for i in stackList:
        sum += i
    print(sum)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)