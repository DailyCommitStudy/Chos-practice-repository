matrix = []
max_length = 0  # 최대 행 길이를 저장할 변수

# 입력 받으면서 최대 행 길이를 찾음
for i in range(5):
    row = list(map(str, input().strip()))
    matrix.append(row)
    max_length = max(max_length, len(row))

# 행의 길이를 최대 길이에 맞게 조절
for i in range(5):
    matrix[i] += [''] * (max_length - len(matrix[i]))

# 열 먼저 출력
for i in range(max_length):  # 열
    for j in range(5):  # 행
        print(matrix[j][i], end='')
