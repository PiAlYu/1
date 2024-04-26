from math import ceil

fin = open('27_B.txt')
a = fin.readlines()
fin.close()
a = [list(map(int, i.split())) for i in a]
n, k = a.pop(0)
for i in a:
    i[1] = ceil(i[1] / 2)
a.sort()
b = [0] * k
for i in a:
    b[i[0]] = i[1]
ps = [b[0]]
for i in range(1, len(b)):
    ps.append(ps[-1] + b[i])
pv, mn = 0, float('inf')
for i in range(len(b)):
    pv += min(k - i, i) * b[i]
for i in range(1, len(b)):
    if i <= k // 2:
        d = b[i + k // 2]
        minus = ps[i - 1 + k // 2] - ps[i - 1]
        plus = ps[-1] - minus - d
    else:
        d = b[i - k // 2 - 1]
        plus = ps[i - 1] - ps[i - 1 - k // 2]
        minus = ps[-1] - plus - d
    pv = pv + plus - minus
    mn = min(mn, pv)
print(mn)
