import sys

def func(inputValue):
    n, k = map(int, inputValue[0].split())
    
    queue = []
    popList = []
    deleteIndex = []
    
    for i in range(n):
        queue.append(i + 1)
    
    index = 0
    while len(queue) != 0:
        index += (k-1)
        index = index % len(queue)
        popList.append(queue.pop(index))
        
    pop = ', '.join(map(str, popList))
    print(f'<{pop}>')

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)