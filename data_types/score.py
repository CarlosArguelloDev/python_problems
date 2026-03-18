n = int(input())
arr = list(map(int, input().split()))

max = runnerUp = float('-inf')
for i in range(len(arr)):
    if arr[i] > max:
        runnerUp = max
        max = arr[i]
    elif arr[i] > runnerUp < max:
        runnerUp = arr[i]

print(runnerUp)