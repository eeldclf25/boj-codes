import sys
import heapq

def func(inputValue):
    heap = []
    for i in range(1, len(inputValue)):
        heapq.heappush(heap, int(inputValue[i]))
    
    if len(heap) == 1:
        print(0)
        return
    
    count = 0
    while len(heap) != 1:
        temp1 = heapq.heappop(heap)
        temp2 = heapq.heappop(heap)
        count += temp1 + temp2
        currentDeck = temp1 + temp2
        heapq.heappush(heap, currentDeck)
    print(count)
    return
        

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)