import sys

def func(inputValue):
    n, c = map(int, inputValue[0].split())
    homeList = []
    for i in range(1, n + 1):
        homeList.append(int(inputValue[i]))
    homeList.sort()
    
    start = 0
    end = homeList[len(homeList) - 1]
    setHome = []
    
    while start <= end:
        mid = (start + end) // 2
        
        setHome = []
        setHome = [homeList[0]]
        lastX = homeList[0]
        
        for i in homeList:
            if lastX + mid <= i:
                setHome.append(i)
                lastX = i
        
        if len(setHome) >= c:
            start = mid + 1
        else:
            end = mid - 1
    print(end)
            
    

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)