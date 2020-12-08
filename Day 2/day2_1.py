entries = []

with open('day2.txt') as f :
    for line in f :
        valid_range, letter, passcode = line.split()
        valid_least, valid_most = (int(item) for item in valid_range.split('-'))
        letter = letter[:-1]
        entries.append([valid_least, valid_most, letter, passcode])
    
answer = 0

for valid_least, valid_most, letter, passcode in entries :
    letter_count = passcode.count(letter)
    if valid_least <= letter_count <= valid_most :
        answer += 1

print(answer)