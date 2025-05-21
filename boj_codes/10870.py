import sys

def func(inputValue):
    n = int(inputValue[0])
    
    v = recursion(n)
    
    print(v)
    
def recursion(value):
    if value == 0:
        return 0
    elif value == 1:
        return 1
    
    return recursion(value - 1) + recursion(value - 2)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)