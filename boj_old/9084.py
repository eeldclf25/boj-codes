import sys
sys.setrecursionlimit(99999)


def func(inputValue):
    for i in range(1, len(inputValue), 3):
        coinList = list(map(int, inputValue[i + 1].split()))
        amount = int(inputValue[i + 2])
        
        dp = {}
        
        def Recursion(index, total):
            if total == 0:
                return 1
            elif total < 0 or index >= len(coinList):
                return 0
            
            if (index, total) in dp:
                return dp[(index, total)]
            92
            use_it = Recursion(index, total - coinList[index])
            skip_it = Recursion(index + 1, total)
            
            dp[(index, total)] = use_it + skip_it
            
            return use_it + skip_it
        
        print(Recursion(0, amount))
        

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)