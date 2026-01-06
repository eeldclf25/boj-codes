import sys

def func(inputValue):
    n = int(inputValue[0])
    
    oneValue = 0
    twoValue = 1
    threeValue = 1
    for _ in range(n - 1):
        oneValue = twoValue % 15746
        twoValue = threeValue % 15746
        threeValue = twoValue + oneValue

    print(threeValue % 15746)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)