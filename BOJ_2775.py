# 백준 2775번 : 부녀회장이 될테야

num = int(input()) # 테스트 케이스 개수 인풋
answer = [] # 정답을 받아둘 임시 리스트

for i in range(num):
    floor = int(input())
    room = int(input())

    apt = [[]] # 아파트를 2차원 리스트 형태로 표현
    for j in range(1, room + 1): # 우선 0층에 기본값 입주시킴
        apt[0].append(j)

    for k in range(floor): # 그리고 각 층 1호에 1명씩 입주시킴
        apt.append([1])

    for l in range(1, floor + 1): # 1층부터 꼭대기층까지 반복
        for m in range(room - 1): # 1호에는 이미 입주했으므로 1개 방을 뺀 수만큼 반복
            apt[l].append(apt[l][m] + apt[l - 1][m + 1])
            # n층의 k번째 방에는 (n층의 k-1번째 방 + n-1층의 k번째 방) 명이 들어간다.
    
    answer.append(apt[floor][room - 1]) # 최종 목표 방 인원을 뽑아 정답 임시 리스트에 투입

for n in answer:
    print(n)
