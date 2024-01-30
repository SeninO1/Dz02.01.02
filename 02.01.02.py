x = int(input())
a = []
if x <= 2000000000:
    for i in range(1, x + 1):
        if x % i == 0:
            a.append(i)
print(len(a))