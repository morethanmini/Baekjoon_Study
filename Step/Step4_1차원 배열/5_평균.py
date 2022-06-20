n = int(input())
point = list(map(int, input().split()))
m = max(point)
arr = []

for i in point:
    arr.append(i / m * 100)

print(sum(arr) / n)