import sys

def func(inputValue):
    value = int(inputValue[0])
    if (90 <= value and value <= 100):
        print('A')
    elif (80 <= value and value <= 89):
        print('B')
    elif (70 <= value and value <= 79):
        print('C')
    elif (60 <= value and value <= 69):
        print('D')
    else:
        print('F')

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)