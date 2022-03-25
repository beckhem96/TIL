num_pattern = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
               '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}


def bit_to_num(arr):
    s = ''
    for i in range(len(arr)):
        s += str(arr[i])
    if s in num_pattern:
        return num_pattern[s]
    else:
        return -1
def sum_confirm(temp):
    if temp and (((temp[0] + temp[2] + temp[4] + temp[6]) * 3) + temp[1] + temp[3] + temp[5] + temp[7]) % 10 == 0:
        return sum(temp)
    return 0

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N은 배열의 세로 크기, M은 배열의 가로크기
    # 16진수라 str로 받음
    for _ in range(N):
        a = list(input())
        for i in range(M):
            a[i] = int(f'{int(a[i], 16):04b}') #이거 다하면 M은 4배가 됨
        j = 0
        temp = []
        while j < len() - 7:
            if b[j:j+7] in num_pattern: # 7칸으로
                temp.append(num_pattern[b[j:j+7]])
                j += 6
            else:
                j += 1

        if temp and (((temp[0] + temp [2] + temp[4] + temp[6]) * 3) + temp[1] + temp[3] + temp[5] + temp[7]) % 10 == 0:
            result = sum(temp)
    print(result)
    #             b.reverse()
    #             for j in range(len(b)):
    #                 if b[j] == '1':
    #                     s += 2**j
    #             temp.append(s)
    #             print(temp)
    # print()


