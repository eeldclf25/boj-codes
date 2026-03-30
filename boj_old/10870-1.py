import sys

def func(inputValue):
    n = int(inputValue[0])
    
    sum = 0
    if n == 0:
        sum = 0
    elif n == 1:
        sum = 1
    else:
        leftValue = 0
        rightValue = 1
        for i in range(n - 1):
            sum = rightValue + leftValue
            temp = rightValue
            rightValue = rightValue + leftValue
            leftValue = temp
    
    print(sum)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)