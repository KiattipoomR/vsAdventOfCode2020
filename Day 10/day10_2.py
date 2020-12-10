entries = []
fixed = set()
custom_tribonacci_seq = {0:1, 1:2, 2:4}

def custom_tribonacci(n):
    result = 0
    if n > 2 :
        for i in range(3, n + 1) :
            result = custom_tribonacci_seq[i - 3] + custom_tribonacci_seq[i - 2] + custom_tribonacci_seq[i - 1]
            custom_tribonacci_seq[i] = result
    else :
        result = custom_tribonacci_seq[n]
 
    return result

with open('day10.txt') as f :
    for line in f :
        line = line.strip()
        entries.append(int(line))
    entries.sort()

for idx in range(len(entries) - 1) :
    if entries[idx + 1] - entries[idx] == 3 or (idx == len(entries) - 1) :
        if entries[idx] not in fixed : 
            fixed.add(entries[idx])

        try : fixed.add(entries[idx + 1])
        except IndexError : pass

arrangables = sorted(set(entries).difference(fixed))
answer = 1

combo = 0
for idx in range(1, len(arrangables)) :
    combo += 1
    if arrangables[idx] - arrangables[idx - 1] != 1 or idx == len(arrangables) - 1 :
        combination = custom_tribonacci(combo)
        answer *= combination
        combo = 0

print(answer)