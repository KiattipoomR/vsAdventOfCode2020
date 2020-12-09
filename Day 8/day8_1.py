idx = 0
accumulator = 0
operations = {}

with open('day8.txt') as f:
# with open('test.txt') as f:
    for i, line in enumerate(f) :
        line = line.strip()
        op_args = line.split()
        operations[i] = [op_args[0], int(op_args[1]), False]

while True :
    print('Current index : {}, current operation : {}'.format(idx, operations[idx][0]))
    if operations[idx][2] == True :
        break
    
    operations[idx][2] = True
    if operations[idx][0] == 'acc' :
        accumulator += operations[idx][1]
    
    if operations[idx][0] == 'jmp' :
        idx += operations[idx][1]
    else :
        idx += 1
    
print(accumulator)