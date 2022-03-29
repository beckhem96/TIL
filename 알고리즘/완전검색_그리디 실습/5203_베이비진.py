import sys

sys.stdin = open('5203_베이비진.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input().split()))
    a, b = [], []
    v_a, v_b = [0] * 10, [0] * 10
    out = False
    winner = 0
    while num:
        a = num.pop(0)
        v_a[a] += 1
        if 3 in v_a:
            winner = 1
            break
        for i in range(len(v_a)-2):
            if 0 not in v_a[i:i+3]:
                winner = 1
                out = True
                break
        if out:
            break
        b = num.pop(0)
        v_b[b] += 1
        if 3 in v_b:
            winner = 2
            break
        for i in range(len(v_b)-2):
            if 0 not in v_b[i:i+3]:
                winner = 2
                break
                out = True
                break
        if out:
            break
    print(f'#{tc} {winner}')

