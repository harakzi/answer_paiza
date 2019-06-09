
T = int(input())

A = T // 24
B = T % 24

# 余りが24
if B != 0:
    C = A + 1
    print(C)

else:
    print(A)
