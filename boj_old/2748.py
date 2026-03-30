import sys

def func(inputValue):
    n = int(inputValue[0])
    
    fiboList = [0 for i in range(n + 1)]
    fiboList[0] = 0
    fiboList[1] = 1
    
    for i in range(2, n + 1):
        fiboList[i] = fiboList[i - 1] + fiboList[i - 2]
        
    print(fiboList[n])

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)