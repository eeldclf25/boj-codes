import sys

def func(inputValue):
    a = int(inputValue[0])
    b = int(inputValue[1])
    c = int(inputValue[2])
    
    result = a * b * c
    
    for i in range(10):
        count = 0
        for ii in str(result):
            if str(i) == str(ii):
                count += 1
        print(count)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)