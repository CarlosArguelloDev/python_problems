records = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name,score])

lowest = float('inf')
second_lowest = float('inf')

for name, score in records:
    if score < lowest:
        second_lowest = lowest
        lowest = score
    elif lowest < score < second_lowest:
        second_lowest = score

print('\n'.join(sorted(name for name, score in records if score == second_lowest)))

