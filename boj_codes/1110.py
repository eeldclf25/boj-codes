import sys

def func(inputValue):
    n = int(inputValue[0]) # n이 26이라고 가정하에 시작
    
    whileCount = 0
    sum = None # while문을 처음 입장하기 위해 None 사용
    while sum != n:
        if sum == None: # while문을 최초로 진입했을때 26부터 시작
            sum = n
        
        whileCount += 1 # 사이클 + 1
        
        if sum >= 10:   # 10 이상일 경우
            one = sum % 10  # 첫번째 자리수 저장 (6)
            two = sum // 10 # 두번째 자리수 저장 (2)
            temp = one + two    # 각각 더하고 temp에 저장 (8)
            sum = (one * 10) + (temp % 10) # 오른쪽 값인 one을 10자리로 옮기고, temp의 첫번째 자리수를 붙이기 (6) -> (60), (8) -> (8) / (60) + (8) = (68)
        else:   # 10이 미만인 경우
            sum = (sum * 10) + (sum) # 그냥 한자리 수를 10으로 곱하고 그 후에 한자리 수를 더하면 완료
    print(whileCount)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)