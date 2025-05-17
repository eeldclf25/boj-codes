import sys

def func(inputValue):
    one = int(inputValue[0])
    
    if ((one % 4 == 0) and (one % 100 != 0)) or one % 400 == 0:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)