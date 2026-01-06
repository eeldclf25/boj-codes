import sys

count = 0

def func(inputValue): # 이 함수는 단순히 입력값을 받고 재귀함수에 입력만 하는 함수라서 패스하면 됩니다
    n, s = map(int, inputValue[0].split())
    nList = list(map(int, inputValue[1].split()))
                 
    recursion(n, s, nList, [], 0)
    print(count)

def recursion(n, s, nList, currentList, currentIndex):
    if sum(currentList) == s and len(currentList) > 0:  # 어차피 재귀의 반복 자체가 동일한 원소의 조합은 못하게 되어 있어서 그냥 if문으로 값만 확인하면 됨
        global count
        count += 1
    
    for i in range(currentIndex, n):    # 반복문이 전 재귀의 i값 + 1(currentIndex)로 받았기 때문에 그이후의 인덱스로 다시 반복문(동일한 원소의 조합을 못하게 하는)
        currentList.append(nList[i])
        recursion(n, s, nList, currentList, i + 1)  # 재귀를 하는데 현재 반복된 i값의 + 1 의 인덱스로 재귀 (중복 인덱스를 허용하지 않은)
        currentList.pop()

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)