import sys


def func(inputValue):
    posList = []
    for i in range(1, len(inputValue)):
        posList.append(list(map(int, inputValue[i].split())))
    
    minimumPath = {}
    
    def dfs(now, visited):
        if visited == (1<<int(inputValue[0])) -1:
            if posList[now][0]:
                return posList[now][0]
            else:
                return int(1e9)
        
        if (now, visited) in minimumPath:
            return minimumPath[(now, visited)]
            
        min_cost = int(1e9)
        
        for next in range(1, int(inputValue[0])):
            if posList[now][next] == 0 or visited & (1<<next): 
                continue
            cost = dfs(next, visited | (1<<next)) + posList[now][next]
            min_cost = min(cost, min_cost)
        
        minimumPath[(now, visited)] = min_cost
        return min_cost
    
    
    print(dfs(0,1))

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)