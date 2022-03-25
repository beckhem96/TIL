# 수영장 문제
import sys

sys.stdin = open('water_pool.txt', 'r')

# 백트래킹, 모든 경우의 수 계산
def DFS(n, ssum):
    global ans
    if n>12:
        if ans > ssum:
            ans = ssum
        return

    DFS(n+1, ssum+plan[n] * day)
    DFS(n + 1, ssum + month)
    DFS(n + 3, ssum + three_month)
    DFS(n + 12, ssum + year)

T = int(input())
for tc in range(1, T+1):
    day, month, three_month, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    ans = 12345678
    DFS(1, 0)
    print(f'#{tc} {ans}')

# # 동적계획법
T = int(input())
for tc in range(1, T+1):
    day, month, three_month, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    v = [0] * 13  # 이용권 가격 누적저장

    for i in range(1, 13):
        minV = v[i-1] + plan[i] * day # 누적요금에 현재 1일권 더해서 저장
        minV = min(minV, v[i-1] + month) # 누적요금에 1달 이용권이랑 day랑 비교해서 작은거 저장

        if i >= 3: # 3개월 이상이면
            minV = min(minV, v[i-3] + three_month) # 지금까지 누적요금에 3달권 저장해서 위의 연산으로 이루어진 최소값 비교
        if i >= 12: # 12개월 이상이면
            minV = min(minV, v[i-12] + year) # 위의 누적 요금과 1년권 비교해서 작은거 저장

        v[i] = minV # 최소 누적요금 저장

    print(f'#{tc} {v[12]}')