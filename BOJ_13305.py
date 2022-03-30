# BOJ 13305 : 주유소

import sys

# input
city = int(sys.stdin.readline())
space = list(map(int, sys.stdin.readline().split(' ')))
fuel = list(map(int, sys.stdin.readline().split(' ')))

# progress
distance = 0    # 누적 거리 변수 초기화
now_fuel = 0    # 현재 기름값 변수 선언
price = 0   # 누적 가격 변수 선언

low_fuel = fuel[0]  # 최초 기름 최저가 설정 (당장엔 1번 도시 주유소가 최저가임)

for i in range(1, len(fuel)):   # 2번째 주유소부터 판별 시작
    now_fuel = fuel[i]
    distance += space[i - 1]    # 거리 누적
    if now_fuel >= low_fuel:    # 현재 기름가와 최저가를 비교, 현재가 더 비싸면 continue
        if i == len(fuel) - 1:  # 다만 끝까지 그대로 갈 수 있으니 마지막일때는 그냥 연산
            price += distance * low_fuel
        continue
    else:   # 현재가 더 싸면 지금까지 기록된 거리를 지금까지 기록된 최저가에 곱해서 가격에 연산
        price += distance * low_fuel
        distance = 0    # 누적 거리 0으로 초기화하고
        low_fuel = now_fuel # 최저 유가는 현재 유가가 됨

# output
print(price)
