import sys

count = 0

def func(inputValue): # 이 함수는 단순히 입력값을 받고 재귀함수에 입력만 하는 함수라서 패스하면 됩니다
    t = int(inputValue[0])
    numlist = [1, 2, 3]
    global count
    
    for i in range(1, t + 1):
        num = int(inputValue[i])
        count = 0
        recursion(num, numlist, 0)
        print(count)

# checkSum = 맞춰야 하는 수(고정), numlist = 1, 2, 3이 있는 단순 배열(고정), currentNum = 재귀를 통해 지금까지 더해진 값(계속 변함)
def recursion(checkSum, numlist, currentNum):
    global count
    
    # 그냥 재귀를 통해 값이 이상이면 리턴(base case)
    if currentNum == checkSum:  # 값이 같은 값이면 + 후 리턴
        count += 1
        return
    elif currentNum > checkSum: # 값이 이상이면 그냥 리턴
        return
    
    for i in range(len(numlist)):   # 리스트의 0부터 시작하는건데, 재귀마다 이 행위를 반복
        recursion(checkSum, numlist, currentNum + numlist[i])   # 재귀 함수

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)