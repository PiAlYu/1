from math import ceil

fin = open('q1adcTG-b.txt')
a = fin.readlines()
fin.close()
n, k, v = list(map(int, a.pop(0).split()))
a = [list(map(int, i.split())) for i in a]
m = 10 ** 20
for i in range(n):
    a[i][1] = ceil(a[i][1] / v)
for i in range(n):
    center = a[i][0]
    s = 0
    for j in range(n):
        r = abs(center - a[j][0])
        s += a[j][1] * min(r, k - r)
    m = min(m, s)
print(m)
