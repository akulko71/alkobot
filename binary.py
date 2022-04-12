N, M = map(int, input().split())
pattern = '.|.'
des = '-'
welcome = 'WELCOME'
kpat = 3
for i in range(0, int(N/2)):
    kdes = M - kpat
    res = ''
    for j in range(0,int(kdes/2)):
    	res += des
    for j in range(0,int(kpat/3)):
    	res += pattern
    for j in range(0,int(kdes/2)):
    	res += des
    print(res)
    kpat += 6