import sys

def func(inputValue):
    t = int(inputValue[0])
    
    count = 1
    while count <= t:
        a, b = map(int, inputValue[count].split())
        print(a + b)
        count += 1

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)