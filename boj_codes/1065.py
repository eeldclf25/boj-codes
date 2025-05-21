import sys
import math

def func(inputValue):
    n = int(inputValue[0])
    
    count = 0
    if n <= 99:
        count = n
    else:
        count += 99
        
        for i in range(n + 1)[100:]:
            hansuIsTrue = True
            num_digits = int(math.log10(i)) # int는 소수값 버림

            first_hansu = digits(i, 0) - digits(i, 1)
            while_count = 2
            while while_count <= num_digits:
                check_hansu = digits(i, while_count - 1) - digits(i, while_count)
                if first_hansu != check_hansu:
                    hansuIsTrue = False
                    break
                while_count += 1
            if hansuIsTrue == True:
                count += 1
    print(count)

def digits(n, select):
    index = n // (10**select)
    index = index % 10
    return index

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)