matrix = [list(map(int, input().split())) for _ in range(9)]
max_list = []

### max값 뽑아내기 위해 각 행을 뽑아내고 max값 뽑기
for i in range(9):
    max_list.append(max(matrix[i]))

print(max(max_list))

### 인덱스 추출을 위해 중첩 for문 이용
for row in range(9):
    for col in range(9):
        if max(max_list) == matrix[row][col]:
            print(row+1, col+1)