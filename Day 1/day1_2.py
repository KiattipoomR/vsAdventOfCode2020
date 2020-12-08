entries = []

with open('day1.txt') as f :
    for line in f :
        try :
            entries.append(int(line))
        except ValueError :
            print('Error occured. Please make sure that the file only has number character.')
            exit(1)

entries_set = set(entries)
answer_found = False

for first_idx, first_entry in enumerate(entries) :
    for second_idx, second_entry in enumerate(entries):
        if not answer_found and first_idx != second_idx :
            expected = 2020 - first_entry - second_entry
            if expected in entries_set and expected != first_entry and expected != second_entry :
                print(first_entry, second_entry, expected, expected * first_entry * second_entry)
                answer_found = True
                break
        else : continue
print("Success !")