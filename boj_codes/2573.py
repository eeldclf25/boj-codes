import sys

def func(inputValue):
    n, m = map(int, inputValue[0].split())
    
    rowcolumn = []
    for i in range(1, len(inputValue)):
        rowcolumn.append(list(map(int, inputValue[i].split())))

    nodeList = []
    for i in range(n):
        for j in range(m):
            if rowcolumn[i][j] != 0:
                nodeList.append([i, j])

    count = 0
    while nodeList:
        visited = []
        stack = []
        stack.append(nodeList[0])
        visited.append(nodeList[0])
        while stack:
            now = stack.pop()
            right = [now[0], now[1] + 1]
            if rowcolumn[right[0]][right[1]] > 0 and right not in visited:
                stack.append(right)
                visited.append(right)
            left = [now[0], now[1] - 1]
            if rowcolumn[left[0]][left[1]] > 0 and left not in visited:
                stack.append(left)
                visited.append(left)
            down = [now[0] + 1, now[1]]
            if rowcolumn[down[0]][down[1]] > 0 and down not in visited:
                stack.append(down)
                visited.append(down)
            up = [now[0] - 1, now[1]]
            if rowcolumn[up[0]][up[1]] > 0 and up not in visited:
                stack.append(up)
                visited.append(up)
        if len(visited) != len(nodeList):
            print(count)
            break

        for i, j in nodeList:
            iceCount = 0
            if rowcolumn[i][j + 1] <= 0:
                iceCount += 1
            if rowcolumn[i][j - 1] <= 0:
                iceCount += 1
            if rowcolumn[i + 1][j] <= 0:
                iceCount += 1
            if rowcolumn[i - 1][j] <= 0:
                iceCount += 1
            rowcolumn[i][j] -= iceCount
            if rowcolumn[i][j] <= 0:
                nodeList.remove([i, j])
        count += 1
    if not nodeList:
        print(0)



if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)