from math import ceil

fin = open('Wq2dJkC1F.txt')
a = fin.readlines()
fin.close()
a = [list(map(int, i.split())) for i in a]
n, k, v = a.pop(0)
m = float('inf')
for i in range(n):
    a[i][1] = ceil(a[i][1] / v)
b = [0] * k
for i in range(n):
    b[a[i][0] % k] = a[i][1]
baza, km, pv = b[0], 0, 0
for i in range(len(b)):
    r = abs(i - km)
    pv += min(k - r, r) * b[i]
ps = [b[0]]
for i in range(1, len(b)):
    ps.append(ps[-1] + b[i])
for i in range(1, len(b)):
    if i <= k // 2:
        minus = ps[i - 1 + k // 2] - ps[i - 1]
        plus = ps[-1] - minus
    else:
        plus = ps[i - 1] - ps[i - 1 - k // 2]
        minus = ps[-1] - plus
    pv = pv - minus + plus
    m = min(m, pv)
print(m)
