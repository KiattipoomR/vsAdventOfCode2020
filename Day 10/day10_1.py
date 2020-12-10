entries = []
jolt_diff = {1:0, 2:0, 3:0}

with open('day10.txt') as f :
    for line in f :
        line = line.strip()
        entries.append(int(line))
    entries.append(max(entries) + 3)
    entries.sort()

current_jolt = 0
for adapter in entries :
    diff = adapter - current_jolt
    jolt_diff[diff] += 1
    current_jolt = adapter

print(jolt_diff[1] * jolt_diff[3])