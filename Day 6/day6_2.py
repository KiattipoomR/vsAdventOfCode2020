question_list = {}
group = 0

with open('day6.txt') as f :
    for row, line in enumerate(f) :
        line.strip()
        if line != '\n' :
            question_args = set()
            question_args.update(line)
            
            try :
                question_args.remove('\n')
            except KeyError :
                pass

            try :
                question_list[group] = question_list[group]
            except KeyError :
                question_list[group] = []
            question_list[group].append(question_args)

        else:
            group += 1

answer = 0

for key, value in question_list.items() :
    
    matched_question = value[0]
    for question in value :
        matched_question = matched_question.intersection(question)
    answer += len(matched_question)

print(answer)