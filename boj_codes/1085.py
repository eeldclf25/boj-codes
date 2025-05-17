import sys

def func(inputValue):
    inputValue = inputValue[0].split()
    x, y, w, h = map(int, inputValue)
    
    xd = x - 0
    xu = w - x
    yd = y - 0
    yu = h - y
    
    li = [xd, xu, yd, yu]
    li.sort()
    
    print(li[0])

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)