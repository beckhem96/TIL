# 교수님 풀이
def solve(lst3):
    for i in range(len(lst2)):
        # 1비트 값만 바꿔서 10진수 값으로 변환
        lst2[i] = (lst2[i] + 1) % 2

        dec = 0 # 10진수 변환
        for idx in range(len(lst2)):
            dec = dec * 2 + lst2[idx]

        s = [] # 3진수로 변환
        ret = dec

        while dec > 0:
            s.append(dec%3)
            dec //= 3
        lst3 = lst3[::-1] # 이게 나랑 다른가?

        cnt = 0
        for idx in range(min(len(s), len(lst3))):
            if s[idx] != lst3[idx]:
                cnt += 1
        cnt += abs(len(s) - len(lst3)) # 길이가 다르다면 다른 값

        if cnt == 1:
            return ret
        lst2[i] = (lst2[i] + 1) % 2 # 원래대로 복구

T = int(input())
for tc in range(1, T+1):
    lst2 = list(map(int, input()))
    lst3 = list(map(int, input()))
    ans = solve(lst3)
    print(f'#{tc} {ans}')

# import copy
#
# def sol(lst2, lst3):
#     for i in range(len(lst2)):
#         s1 = ''
#         lst2[i] = int(not lst2[i]) # 한자리 바꿔주고
#         for k in lst2: # 문자열로 변경
#             s1 += str(k)
#         bitV = int(s1, 2) # 10진수로 저장하고
#         for j in range(len(lst3)): # 2진수 한자리 바뀐 상태로 3진수의 모든 자리 하나씩 계산 계산
#             tmp = copy.copy(lst3)
#             while lst3[j] != 0: # 0이면 그 자리의 값이 0이니 그만
#                 lst3[j] -= 1
#                 s2 = ''
#                 for z in lst3:  # 문자열로 변경
#                     s2 += str(z)
#                 if int(s2, 3) == bitV:
#                     return int(s2, 3)
#             lst3 = tmp
#         lst2[i] = int(not lst2[i])
#
# T = int(input())
# for tc in range(1, T+1):
#     lst2 = list(map(int, input()))
#     lst3 = list(map(int, input()))
#     print(f'#{tc} {sol(lst2, lst3)}')
