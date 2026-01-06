import sys
from collections import deque

def func(inputValue):
    n = int(inputValue[0])
    k = int(inputValue[1])
    appleList = []
    for i in range(2, k + 2):
        appleList.append(list(map(int, inputValue[i].split())))
    snakeCommand = []
    for i in range(k + 3, len(inputValue)):
        time, arrow = map(str, inputValue[i].split())
        snakeCommand.append([int(time), arrow])
    appleList.sort()
    appleList.reverse()
    snakeCommand.sort()
    snakeCommand.reverse()
    
    snake = deque()
    snake.append([1, 1])
    snakeHead = 0
    isLife = True
    second = 0
    while isLife:
        if snakeCommand and int(snakeCommand[-1][0]) == second:
            arrow = snakeCommand.pop()
            if arrow[1] == 'D':
                snakeHead += 1
            elif arrow[1] == 'L':
                snakeHead -= 1
            if snakeHead == 4:
                snakeHead = 0
            elif snakeHead == -1:
                snakeHead = 3
        
        if snakeHead == 0:
            snake.appendleft([snake[0][0] + 1, snake[0][1]])
        elif snakeHead == 1:
            snake.appendleft([snake[0][0], snake[0][1] + 1])
        elif snakeHead == 2:
            snake.appendleft([snake[0][0] - 1, snake[0][1]])
        elif snakeHead == 3:
            snake.appendleft([snake[0][0], snake[0][1] - 1])
        else:
            snake.appendleft([snake[0][0] - 1, snake[0][1] - 1])
        
        if snake[0][0] == 0 or snake[0][0] == n + 1 or snake[0][1] == 0 or snake[0][1] == n + 1:
            isLife = False
        for i in range(1, len(snake)):
            if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                isLife = False
        
        isApple = False
        for i in range(0, len(appleList)):
            if snake[0][0] == appleList[i][1] and snake[0][1] == appleList[i][0]:
                appleList.pop(i)
                isApple = True
                break
        if isApple == False:
            snake.pop()
        

        second += 1
    print(second)
        
        
        
    

if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)