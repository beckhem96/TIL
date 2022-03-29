def perm( n,  k ): # p[n]을 채워서 k개의 숫자로 만드는 순열, 인덱스가 사전순으로 생성
    if n == k:
        print(p)
    else:
        for i in range(k):		# 모든 원소에 대해
            if used[i] == 0:    # 사용된 적이 없으면
                p[n] = arr[i]	# 순열에 사용
                used[i] = 1 	# 사용됨으로 표시
                perm(n+1, k)
                used[i] = 0	# 다른 자리에서 사용가능

arr = [1,2,3]
p = [0]*3
used = [0]*3
perm(0, 3)

