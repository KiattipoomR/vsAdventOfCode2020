file_rows = 999
passport_args = []
passport_list = []

with open('day4.txt') as f :
    for row, line in enumerate(f) :
        if line != '\n' :
            line_args = [args[:3] for args in line.strip().split()]
            passport_args += line_args
        if line == '\n' or file_rows - row == 1 :
            passport_list.append(set(passport_args))
            passport_args.clear()

answer = 0

for passport in passport_list :
    try :
        passport.remove('cid')
    except KeyError :
        pass
    
    if len(passport) == 7 :
        answer += 1

print(answer)