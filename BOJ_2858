# 2858번 // 기숙사 바닥

input_a, input_b = map(int, input().split(' ')) # input a와 b에 입력값 저장

area = input_a + input_b # 인풋받은 두 값을 더하면 전체 넓이가 됨
height = 3 # 최소 세로길이 설정

while True: # 아래 조건을 만족하는 동안
    if area % height == 0: # 넓이를 세로길이로 나눴을 때, 나누어 떨어지면
        if (height - 2) * (int(area / height) - 2) == input_b: # 세로에서 2를 뺀 값과 넓이를 세로-2로 나눈 값이 내부 크기가 된다면
            print(int(area / height), height) # 출력
            break
    height += 1
