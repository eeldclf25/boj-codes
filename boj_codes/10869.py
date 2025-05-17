import sys

def func(inputValue):
    inputValue = inputValue[0].split()
    a = int(inputValue[0])
    b = int(inputValue[1])
    
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)