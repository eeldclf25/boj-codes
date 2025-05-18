import sys

def func(inputValue):
    check = 0
    max = 0
    for i in range(len(inputValue)):
        if max < int(inputValue[i]):
            max = int(inputValue[i])
            check = i
    print(max)
    print(check + 1)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)