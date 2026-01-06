import sys

def func(inputValue):
    studentList = []
    studentList.append([])  # 0은 안쓰고 싶음
    for i in range(1, len(inputValue)):
        myclass = list(map(int, inputValue[i].split()))
        studentList.append([myclass, 0])

    for j in range(1, len(inputValue)):
        for y in range(1, len(inputValue)):
             if j == y:
                  continue
             for i in range(0, 5):
                base = studentList[j][0][i]
                target = studentList[y][0][i]
                if base == target:
                    studentList[j][1] += 1
                    break
    
    max_student = max(studentList[1:], key=lambda x: x[1])
    value = studentList.index(max_student)
    print(value)


if __name__ == '__main__':
    inputValue = sys.stdin.read().splitlines()
    func(inputValue)