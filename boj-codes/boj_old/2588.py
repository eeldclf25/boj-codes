import sys

def func(inputValue):
    one = inputValue[0]
    two = inputValue[1]
    
    three = int(one) * int(two[2])
    four = int(one) * int(two[1])
    five = int(one) * int(two[0])
    six = three + (four * 10) + (five * 100)
    
    print(three)
    print(four)
    print(five)
    print(six)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)