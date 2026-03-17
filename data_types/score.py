n = int(input())
arr = list(map(int, input().split()))

max = arr[0]
runnerUp = 0
for i in range(len(arr)):
    if arr[i] > max:
        runnerUp = max
        max = arr[i]
    elif arr[i] > runnerUp and arr[i] != max:
        runnerUp = arr[i]


print(runnerUp)