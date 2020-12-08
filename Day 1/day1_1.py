entries = []

with open('day1.txt') as f :
    for line in f :
        try :
            entries.append(int(line))
        except ValueError :
            print('Error occured. Please make sure that the file only has number character.')
            exit(1)

entries_set = set(entries)

for entry in entries :
    expected = 2020 - entry
    if expected in entries_set and entry != expected :
        print(entry, expected, entry * expected)
        break