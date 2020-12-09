entries = []

with open('day9.txt') as f :
# with open('test.txt') as f :
    for line in f :
        line = line.strip()
        entries.append(int(line))

expected = 22477624
found = False

for i in range(0, len(entries)) :
    if not found :
        for j in range(i + 1, len(entries)) :
            sliced = entries[i:j]
            if sum(sliced) == expected :
                print(min(sliced) + max(sliced))
                found = True
                break
    else : 
        break