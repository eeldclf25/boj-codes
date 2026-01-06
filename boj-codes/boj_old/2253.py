import sys

def func(inputValue):
    n, m = map(int, inputValue[0].split())
    trapList = []
    for pos in range(1, len(inputValue)):
        trapList.append(int(inputValue[pos]))
    
    dp  = [[float("inf") for _ in range(int((2*n)**0.5) + 2)]  for _ in range(n+1)]
    dp[1][0] = 0
    
    for pos in range(2, n+1):
        if pos in trapList:
            continue
        for speed in range(1, int((2*n)**0.5) + 1):
            if pos - speed == 0:
                break
            
            currentSpeedDown = dp[pos - speed][speed - 1]
            currentSpeedMid = dp[pos - speed][speed]
            currentSpeedUp = dp[pos - speed][speed + 1]
            
            result = min(currentSpeedDown, currentSpeedMid, currentSpeedUp)
            dp[pos][speed] = result + 1
    
    result = min(dp[n])
    if result == float("inf"):
        print(-1)
    else:
        print(result)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)