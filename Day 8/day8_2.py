operations = {}
candidates = {}

with open('day8.txt') as f:
    for i, line in enumerate(f) :
        line = line.strip()
        op_args = line.split()
        operations[i] = [op_args[0], int(op_args[1]), False]
        if op_args[0] != 'acc' :
            candidates[i] = op_args[0]


def change_ops(operations, idx) :
    operations_copy = operations.copy()
    if operations[idx][0] == 'nop' :
        operations_copy[idx][0] = 'jmp'
    else : operations_copy[idx][0] = 'nop'

    return operations_copy

def reset_ops(operations) :
    for key in operations.keys() :
        operations[key][2] = False
    
    return operations


def run_ops(operations) :
    idx = 0
    accumulator = 0
    while True :
        try :
            if operations[idx][2] == True :
                return (0, False)
            
            operations[idx][2] = True
            if operations[idx][0] == 'acc' :
                accumulator += operations[idx][1]
            
            if operations[idx][0] == 'jmp' :
                idx += operations[idx][1]
            else :
                idx += 1
        except KeyError :
            return (accumulator, True)

def solve() :
    for index in sorted(candidates.keys()) :
        operations_copy = operations.copy()
        result = run_ops(change_ops(operations_copy, index))
        if result[1] == True :
            return result[0]
        operations_copy = reset_ops(change_ops(operations_copy, index))

print(solve())