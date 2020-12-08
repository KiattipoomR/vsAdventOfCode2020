entries = []

with open('day2.txt') as f :
    for line in f :
        valid_range, letter, passcode = line.split()
        valid_first, valid_second = (int(item) for item in valid_range.split('-'))
        letter = letter[:-1]
        entries.append([valid_first, valid_second, letter, passcode])
    
answer = 0

for valid_first, valid_second, letter, passcode in entries :
    match_first = passcode[valid_first - 1]
    match_second = passcode[valid_second - 1]
    
    if (match_first, match_second).count(letter) == 1 :
        answer += 1

print(answer)