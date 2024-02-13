m1 = [
    [1, 2],
    [3, 4],
]

m2 = [
    [10, 20],
    [30, 40],
]
print(m1)
print(m2)
for row in range(2):
    for col in range(2):
        print(m1[row][col] + m2[row][col], end=" ")
    print()

for row in range(2):
    for col in range(2):
        sum = 0
        for i in range(2):
            sum += m1[row][i] * m2[i][col]
        print(sum, end=" ")
    print()

