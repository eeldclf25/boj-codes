import sys
import heapq

def func(inputValue):
    maxHeap = []
    minHeap = []
    
    for i in range(1, len(inputValue)):
        value = int(inputValue[i])
        
        if not maxHeap or value <= -maxHeap[0]:
            heapq.heappush(maxHeap, -value)
        else:
            heapq.heappush(minHeap, value)
        
        if len(maxHeap) > len(minHeap) + 1:
            temp = heapq.heappop(maxHeap)
            heapq.heappush(minHeap, -temp)
        elif len(maxHeap) < len(minHeap):
            temp = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -temp)

        print(-maxHeap[0])
            
        

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)