N, M = map(int, input().split())
pattern = ".|."
des = "-"
welcome = "WELCOME"
rdyStr = []
kpat = 3
for i in range(0, int(N/2)):
    kdes = M - kpat
    res = ""
    for j in range(0,int(kdes/2)):
    	res += des
    for j in range(0,int(kpat/3)):
    	res += pattern
    for j in range(0,int(kdes/2)):
    	res += des
    rdyStr.append(res)
    kpat += 6
res = ""
for i in range(0, int((M - 7)/2)):
	res += des

rdyStr.append(res + welcome + res)
for i in range(0, len(rdyStr)):
	print(rdyStr[i])
for i in range(len(rdyStr)-1, 0, -1):
	print(rdyStr[i-1])