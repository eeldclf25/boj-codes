import sys

def func(inputValue):
    n = int(inputValue[0])
    
    print(coin(n))
    
def coin(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibo(n - 1) + fibo(n - 2)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)