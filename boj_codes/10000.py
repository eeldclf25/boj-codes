import sys

def func(inputValue):
    frontList = []
    endList = []
    for i in range(1, len(inputValue)):
        one, ran = map(int, inputValue[i].split())
        front = one - ran
        end = one + ran
        frontList.append([front, end - front, end - front])
        endList.append(end)
    frontList.sort(key=lambda x: (-x[0], x[1]))
    endList.sort()
    endList.reverse()
    
    count = 0
    stackList = []
    while len(frontList) != 0 or len(endList) != 0:
        if len(frontList) != 0 and frontList[-1][0] < endList[-1]:
            stackList.append(frontList.pop())
        else:
            endList.pop()
            temp = stackList.pop()
            if len(stackList) != 0:
                stackList[-1][1] -= temp[2]
            count += 1
            if temp[1] == 0:
                count += 1
    
    print(count + 1)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)