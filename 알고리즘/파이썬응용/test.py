import sys

sys.stdin = open('hex_code_scan.txt', 'r')
num_pattern = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4,
               '231': 5, '114': 6, '312': 7, '213': 8, '112': 9}
hex_to_bin = {'0':'0000', '1':'0001', '2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000',
              '9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}

def sum_confirm(arr):
    arr.reverse()
    if (((arr[0] + arr[2] + arr[4] + arr[6]) * 3) + arr[1] + arr[3] + arr[5] + arr[7]) % 10 == 0:
        return sum(arr)
    return 0

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N은 배열의 세로 크기, M은 배열의 가로크기
    # 16진수라 str로 받음
    result = 0
    no_double = []
    for _ in range(N):
        a = list(input())
        if a not in no_double:
            sum_value = []
            b = ''
            for i in range(M):
                b += hex_to_bin[a[i]] #이거 다하면 M은 4배가 됨
            n = M*4-1
            while n != 0: # 암호코드는 0으로 시작해서 1로 끝남 그러니 뒤에서부터 1을 찾자 0101순
                # 숫자 하나 확인하는 if문
                if b[n] == '1': # 첫 1을 만나면
                    c1, c2, c3 = 0, 0, 0
                    while b[n] != '0': # 0을 만날 때까지 반복
                        b[n].replace('1', '0')
                        c3 += 1
                        n -= 1
                    # 0을 마난 빠져 나오면
                    while b[n] != '1': # 1을 만날떄까지 반복
                        c2 += 1
                        n -= 1
                    while b[n] != '0': # 0을 만날 때까지 반복
                        b[n].replace('1', '0')
                        c1 += 1
                        n -= 1
                    was_1 = min(c1, c2, c3) # 1이 무조건 있어야되는데 1이 아니라면 제일 작은 수가 배수인 것이다.
                    pattern = str(c1//was_1) + str(c2//was_1) + str(c3//was_1) # 비율 나눠줌
                    sum_value.append(num_pattern[pattern]) # 코드 하나 넣고 다시 반복

                n -= 1
            if sum_value:
                for i in range(len(sum_value)//8):
                    if sum_value[i*8:i*8+8] not in no_double:
                        sum_confirm(sum_value[i*8:i*8+8])
                        if sum_confirm(sum_value[i*8:i*8+8]) != 0:
                            result += sum_confirm(sum_value[i*8:i*8+8])
                            no_double.append(sum_value[i*8:i*8+8])

    print(f'#{tc} {result}')
