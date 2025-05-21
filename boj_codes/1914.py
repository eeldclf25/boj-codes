import sys


strArray = []

def func(inputValue):
    n = int(inputValue[0])
    
    if n <= 20:
        recurison(n, 1, 3, 2)
        print(len(strArray))
        for i in strArray:
            print(i)
    else:
        print(2**n - 1)
    
def recurison(n, x, y, z):
    if n == 1:
        strArray.append(f'{x} {y}')
        return
    
    recurison(n - 1, x, z, y)
    strArray.append(f'{x} {y}')
    recurison(n - 1, z, y, x)
    

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)