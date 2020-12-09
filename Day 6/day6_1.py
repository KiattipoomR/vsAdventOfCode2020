file_rows = 2147
question_args = set()
question_list = []

with open('day6.txt') as f :
    for row, line in enumerate(f) :
        line.strip()
        if line != '\n' :
            question_args.update(line)
        if line == '\n' or file_rows - row == 1 :
            try :
                question_args.remove('\n')
            except KeyError :
                pass

            question_list.append(set(question_args))
            question_args.clear()

answer = 0

for question in question_list :
    answer += len(question)

print(answer)