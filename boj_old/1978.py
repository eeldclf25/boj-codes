import sys

def func(inputValue):
    n = int(inputValue[0])
    numbers = list(map(int, inputValue[1].split()))
    
    count = 0
    for i in range(n):
        if numbers[i] == 1:
            continue
        else:
            check = False
            for ii in range(numbers[i]):
                if ii == 0 or ii == 1:
                    continue
                elif numbers[i] % ii == 0:
                    check = True
            if check == False:
                count += 1
    print(count)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)