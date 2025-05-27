import sys

def func(inputValue):
    a, b, c = map(int, inputValue[0].split())

    print(recursion(a, b, c))
    
def recursion(a, b, c):
    if b == 1:
        return a % c
    
    leftB = b // 2
    rightB = b - leftB
    
    if leftB == rightB:
        left = recursion(a, leftB, c)
        right = left
        return (left * right) % c
    else:
        left = recursion(a, leftB, c)
        right = left * a
        return (left * right) % c
    

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue) 