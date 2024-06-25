def fct(i, j):
    if i + 1 < r and mtx[i + 1][j] > mtx[i][j] and tmp[i + 1][j] < tmp[i][j] + 1:
        tmp[i + 1][j] = tmp[i][j] + 1
        fct(i + 1, j)
    if i - 1 >= 0 and mtx[i - 1][j] > mtx[i][j] and tmp[i - 1][j] < tmp[i][j] + 1:
        tmp[i - 1][j] = tmp[i][j] + 1
        fct(i - 1, j)
    if j + 1 < c and mtx[i][j + 1] > mtx[i][j] and tmp[i][j + 1] < tmp[i][j] + 1:
        tmp[i][j + 1] = tmp[i][j] + 1
        fct(i, j + 1)
    if j - 1 >= 0 and mtx[i][j - 1] > mtx[i][j] and tmp[i][j - 1] < tmp[i][j] + 1:
        tmp[i][j - 1] = tmp[i][j] + 1
        fct(i, j - 1)
    return 0


r, c = map(int, input().split())
mtx, tmp0, mx, mn, lst, ans = [], [], 0, 0, [], 0
for i0 in range(r):
    mtx.append(tuple(map(int, input().split())))
    tmp0.append([0] * c)
for i0 in range(r):
    for j0 in range(c):
        if (i0 + 1 == r or mtx[i0 + 1][j0] > mtx[i0][j0]) and (i0 == 0 or mtx[i0 - 1][j0] > mtx[i0][j0]) and (
                j0 + 1 == c or mtx[i0][j0 + 1] > mtx[i0][j0]) and (j0 == 0 or mtx[i0][j0 - 1] > mtx[i0][j0]):
            lst.append((i0, j0))
for t in lst:
    tmp = tmp0[:]
    a = fct(t[0], t[1])
    for i0 in range(r):
        for j0 in range(c):
            mx = max(mx, tmp[i0][j0])
    ans = max(ans, mx)
print(ans + 1)
