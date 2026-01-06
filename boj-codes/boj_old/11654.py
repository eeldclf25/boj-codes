import sys

def func(inputValue):
    chr = inputValue[0]
    asci = ord(chr)
    print(asci)

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)