import sys

def func(inputValue):
    n, k = map(int, inputValue[0].split())
    itemList = []
    for i in range(1, len(inputValue)):
        weight, price = map(int, inputValue[i].split())
        itemList.append([weight, price])
        
    dp = {}
    
    def Recursion(index, backpack, totalPrice):
        if backpack < 0 or index >= len(itemList):
            return 0
        
        # if (index, total) in dp:
        #     return dp[(index, total)]
        
        currentItem = itemList[index]
        currentBackPack = backpack - currentItem[0]
        currentTotalPrice = totalPrice + currentItem[1]
        
        if currentBackPack < 0:
            return 0
        
        putItem = Recursion(index + 1, currentBackPack, currentTotalPrice)
        passItem = Recursion(index + 1, backpack, totalPrice)
        
        # dp[(index, total)] = use_it + skip_it
        
        qqq = max(currentTotalPrice, putItem, passItem)
        return qqq
    
    print(Recursion(0, 1))

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)