import sys

def func(inputValue):
    comList = []
    for i in range(1, len(inputValue)):
        comList.append(inputValue[i])
        
    stackList = []
    for i in comList:
        com = list(map(str, i.split()))
        if com[0] == 'push':
            stackList.append(int(com[1]))
        elif com[0] == 'pop':
            if len(stackList) == 0:
                print('-1')
            else:
                print(stackList.pop())
        elif com[0] == 'size':
            print(len(stackList))
        elif com[0] == 'empty':
            if len(stackList) == 0:
                print('1')
            else:
                print('0')
        elif com[0] == 'top':
            if len(stackList) == 0:
                print('-1')
            else:
                print(stackList[-1])

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)