n = int(input())
arr = list(map(int, input().split()))
print(arr)
max_score = max(arr)

while max_score in arr:
    arr.remove(max_score)

print(max(arr))