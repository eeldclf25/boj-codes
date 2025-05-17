import sys

def func(inputValue):
    inputValue = inputValue[0].split()
    a = int(inputValue[0])
    b = int(inputValue[1])
    v = int(inputValue[2])
    
    dayUp = a - b
    lastCheck = v - a
    day = lastCheck // dayUp
    
    if lastCheck % dayUp == 0:
        day += 1
    else:
        day += 2

    print(int(day))

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)