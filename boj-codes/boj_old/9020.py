import sys

def func(inputValue):
    n = int(inputValue[0])
    
    for i in range(n + 1)[1:]:
        value = int(inputValue[i])
        
        leftValue = value // 2
        RightValue = value // 2
        for ii in range(leftValue):
            if primeCheck(leftValue) and primeCheck(RightValue):
                break
            else:
                leftValue -= 1
                RightValue += 1
        print(f'{leftValue} {RightValue}')
            
def primeCheck(value):
    check = True
    for iii in range(value)[2:]:
        if value % iii == 0:
            check = False
            break
    return check
            
if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)