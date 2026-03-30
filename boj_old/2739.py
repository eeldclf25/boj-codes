import sys

def func(inputValue):
    n = int(inputValue[0])
    
    count = 1
    while count <= 9:
        print(f'{n} * {count} = {n * count}')
        count += 1

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)