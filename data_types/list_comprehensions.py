x = int(input())
y = int(input())
z = int(input())
n = int(input())

dummy = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            print(i,j,k)
            if i+j+k != n:
                dummy.append([i,j,k])
print(dummy)