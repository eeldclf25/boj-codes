import sys

def func(inputValue):
    t = int(inputValue[0])
    
    for i in range(t):
        array = list(map(int, inputValue[i + 1].split()))
        count = array[0]
        total = 0
        total -= array[0]
        for ii in array:
            total += ii
        mid = total / count
        sucessCount = 0
        for iii in array[1:]:
            if mid < iii:
                sucessCount += 1
        print(f'{((sucessCount / count * 100)):.3f}%')

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)