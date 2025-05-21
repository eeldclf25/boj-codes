import sys

def func(inputValue):
    x = int(inputValue[0])
    
    print(exp(x))
    print(tail_exp(1, x))
    print(fast_exp(1, x))
    
def exp(x):
    if x == 1:
        return 1
    return x * exp(x - 1)


def tail_exp(x, y):
    if y == 1:
        return x * y
    return tail_exp(x * y, y - 1)

def fast_exp(x, y):
    if y == 1:
        return x * y
    
    if x // 2 == 0:
        return Square(fast_exp(x * y, y - 1))
    else:
        return fast_exp(x * y, y - 1)



if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)