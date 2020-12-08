class Passport :
    def __init__(self, args) :
        fields = set()
        values = {}

        for arg in args :
            field = arg[:3]
            if field != 'cid' : 
                fields.add(field)
            
            if field == 'hgt' :
                values[field] = (arg[4:-2], arg[-2:])
            elif field != 'cid' :
                values[field] = arg[4:]
        
        self.fields = fields
        self.values = values
    
    def check_present(self) :
        return len(self.fields) == 7

    def check_valid(self) :
        if not self.check_present() : return False
        
        for key, value in self.values.items() :
            if key == 'byr' and not 1920 <= int(value) <= 2002 : 
                print(key)
                return False
            elif key == 'iyr' and not 2010 <= int(value) <= 2020 : 
                print(key)
                return False
            elif key == 'eyr' and not 2020 <= int(value) <= 2030 : 
                print(key)
                return False
            elif key == 'hgt' :
                if value[1] == 'cm' :
                        if not 150 <= int(value[0]) <= 193 :
                            print(key, value[1])
                            return False
                elif value[1] == 'in' :
                        if not 59 <= int(value[0]) <= 76 :
                            print(key, value[1])
                            return False
                else :
                    print(key)
                    return False
            elif key == 'hcl' :
                if len(value) != 7 :
                    print(key)
                    return False
                elif value[0] == '#' :
                    check = '1234567890abcdef'
                    for letter in value[1:] :
                        if letter not in check :
                            print(key)
                            return False
            elif key == 'ecl' and ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth').count(value) == 0 :
                print(key)
                return False
            elif key == 'pid' and len(value) != 9 :
                print(key)
                return False

        return True

file_rows = 999
passport_args = []
passport_list = []

with open('day4.txt') as f :
    for row, line in enumerate(f) :
        if line != '\n' :
            line_args = line.strip().split()
            passport_args += line_args
        if line == '\n' or file_rows - row == 1 :
            passport_list.append(Passport(passport_args))
            passport_args.clear()

answer = 0

for passport in passport_list :
    if passport.check_valid() :
        answer += 1

print(answer)