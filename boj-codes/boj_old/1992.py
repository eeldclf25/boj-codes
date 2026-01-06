import sys

def func(inputValue):
    print('Hello World!')

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)