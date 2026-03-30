import sys

def func(inputValue):
    t = int(inputValue[0])
    
    for i in range(t):
        ran = len(inputValue[i + 1])
        lastScore = 0
        currentScore = 0
        for ii in range(ran):
            if inputValue[i + 1][ii] == 'O':
                lastScore = lastScore + 1
                currentScore += lastScore
            else:
                lastScore = 0
        print(currentScore)
                

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)