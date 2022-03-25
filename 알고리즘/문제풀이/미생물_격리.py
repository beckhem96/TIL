import sys

sys.stdin = open('미생물_격리_input.txt', 'r')

di, dj = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]
opp = [0, 2, 1, 4, 3]  # 반대방향을 위한 리스트 1이면 2, 2면 2, 3이면 4, 4면 3

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)] # 직접 찍을 필요없음



    for try_n in range(M): # 시간 만큼 실행
        for i in range(len(arr)):
            arr[i][0] = arr[i][0] + di[arr[i][3]] # 좌표 업그레이드
            arr[i][1] = arr[i][1] + dj[arr[i][3]]
            # 약물 처리
            if arr[i][0] == 0 or arr[i][0] == N-1 or arr[i][1] == 0 or arr[i][1] == N-1:
                arr[i][2] = arr[i][2] //2
                arr[i][3] = opp[arr[i][3]]
        # 곂치는거 확인하기 위해 정렬
        arr.sort(key=lambda x:(x[0],x[1],x[2]), reverse=True) # 인덱스랑 개체수 정렬
        # 곂치면
        # for i in range(len(arr)-1): # for로 하면 pop못함
        #     if arr[i][0] == arr[i+1][0] and arr[i][1] == arr[i+1][1]:
        #         if arr[i][2]
        i = 1
        while i < len(arr):
            if arr[i-1][0] == arr[i][0] and arr[i-1][1] == arr[i][1]:
                arr[i-1][2] += arr[i][2]
                if arr[i-1][2] > arr[i][2]:
                    arr.pop(i)
            else:
                i += 1
    result = 0
    for i in range(len(arr)):
        result += arr[i][2]
    print(f'#{tc} {result}')



