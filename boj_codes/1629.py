import sys

def func(inputValue):
    a, b, c = map(int, inputValue[0].split())
    print((a ** b) % c)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue) 