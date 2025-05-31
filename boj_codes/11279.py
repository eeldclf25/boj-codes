import sys
import heapq

def func(inputValue):
    heap = []
    for i in inputValue[1:]:
        if int(i) == 0:
            if heap:
                print(heapq.heappop(heap)[1])
                continue
            else:
                print(0)
                continue
        
        heapq.heappush(heap, [(0 - int(i)),int(i)])

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)