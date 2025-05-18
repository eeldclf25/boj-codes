import sys

def func(inputValue):
    n, x = map(int, inputValue[0].split())
    numbers = list(map(int, inputValue[1].split()))
    
    result = ''
    for num in numbers:
        if num < x:
            result += f'{num} '
    print(result.strip())

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)