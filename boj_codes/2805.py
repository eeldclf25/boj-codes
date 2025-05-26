import sys

def func(inputValue):
    n, m = map(int, inputValue[0].split())
    treeList = list(map(int, inputValue[1].split()))
    
    start = 0
    end = max(treeList)
    cutHeight = 0
    
    while start <= end:
        cutHeight = (start + end) // 2
        
        sumTree = 0
        for i in treeList:
            if i > cutHeight:
                sumTree += i - cutHeight
        
        if sumTree >= m:
            start = cutHeight + 1
        else:
            end = cutHeight - 1
            
    print(end)
            

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)