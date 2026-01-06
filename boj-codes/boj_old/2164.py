import sys
import queue

def func(inputValue):
    n = int(inputValue[0])
    
    que = queue.Queue()
    for i in range(1, n + 1):
        que.put(i)
    
    pop = True
    while que.qsize() > 1:
        if pop == True:
            que.get()
            pop = False
        else:
            que.put(que.get())
            pop = True
            
    print(que.get())

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)