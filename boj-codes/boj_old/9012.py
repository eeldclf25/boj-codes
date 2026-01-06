import sys

def func(inputValue):
    for i in range(1, len(inputValue)):
        string = list(map(str, inputValue[i]))
        
        count = 0
        check = True
        for par in string:
            if par == '(':
                count += 1
            else:
                if count != 0:
                    count -= 1
                else:
                    check = False
                    break
                
        if check == True and count == 0:
            print('YES')
        else:
            print('NO')
    

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)