import sys

def func(inputValue):
    m, n, l = map(int, inputValue[0].split())
    

    
    animalList = []
    for i in range(2, len(inputValue)):
        animalList.append(list(map(int, inputValue[i].split())))
    gunList = list(map(int, inputValue[1].split()))
    gunList.sort()
    huntCount = 0
    
    
    
    
    
    for i in range(len(animalList)):
        if animalList[i][1] > l:
            pass
        
        lange = l - animalList[i][1]
        checkLeft = animalList[i][0] - lange
        checkRight = animalList[i][0] + lange
        
        hunt = False
        left = 0
        right = len(gunList)
        while left < right:
            mid = (left + right) // 2
            
            if checkRight < gunList[mid]:
                right = mid - 1
            elif checkLeft > gunList[mid]:
                left = mid + 1
            else:
                hunt = True
                break
        if hunt == True:
            huntCount += 1
    
    
    
    
    print(huntCount)
        
    
    
if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)