entries = []

with open('day9.txt') as f :
# with open('test.txt') as f :
    for line in f :
        line = line.strip()
        entries.append(int(line))

preamble = 25
for i in range(preamble, len(entries)) :
    start, end = i - preamble, i - 1
    valid = False
    pool = entries[start:end + 1]
    
    for item in pool :
        check = entries[i] - item
        if check in set(pool) and check != item :
            valid = True
    
    if not valid :
        print(entries[i])
        break