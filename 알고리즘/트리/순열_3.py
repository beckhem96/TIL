def pem(i, N):
    if i==N:
        print(p)
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            pem(i+1, N)
            p[i], p[j] = p[j], p[i]
p = [1,2,3]

pem(0, len(p))