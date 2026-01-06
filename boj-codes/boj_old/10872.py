import sys

def func(inputValue):
    n = int(inputValue[0])
    print(recursion(n))
    
def recursion(n):
    if n <= 1:
        return 1
    return n * recursion(n - 1)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)