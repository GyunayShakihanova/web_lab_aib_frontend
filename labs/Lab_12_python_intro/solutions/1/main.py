inputfile = open('input.txt')
words = inputfile.read()
n, m = map(int, words.split())
a = []
for i in range(n):
    a.append(list([-1 for j in range(m)]))
a[0][0] = 1


def sol(i, j):
    if i >= 0 and j >= 0 and i < n and j < m:
        if a[i][j] == -1:
            a[i][j] = sol(i-2, j-1)+sol(i-1, j-2)
    else:
        return 0
    return a[i][j]


output_file = open('output.txt', 'w')
output_file.write(str(sol(n-1, m-1)))