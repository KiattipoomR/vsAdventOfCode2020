from collections import defaultdict

bag_graph = defaultdict(lambda: [])
reverse_bag_graph = defaultdict(lambda: [])

def process_bags(bag_arg) :
    # The format is 'X type-bag(s)
    processed_bags = list(bag_arg)
    for idx, bag in enumerate(bag_arg) :
        first = bag.find(' ') + 1
        last = 0

        if len(set(bag[-2:]).intersection({'s','.'})) == 2 :
            last = -2
        elif len(set(bag[-2:]).intersection({'s','.'})) == 1 :
            last = -1
        else : last = len(bag)

        if 'no other bags' not in bag :
            processed_bags[idx] = bag[first:last - 4]
        else : 
            processed_bags[idx] = None

    return processed_bags    

with open('day7.txt') as f :
    for line in f :
        line = line.strip()
        bag, bag_args = line.split(' contain ')
        bag = bag[:-5]
        bag_args = process_bags(bag_args.split(', '))
        # print('{}-{}'.format(bag, bag_args))
        for bag_arg in bag_args :
            if bag_arg != None :
                bag_graph[bag].append(bag_arg)
                reverse_bag_graph[bag_arg].append(bag)

expected_bag = 'shiny gold'
answer = 0
traveled_bag = set()

def dfs(key) :
    global answer
    if key not in traveled_bag :
        print(key)
        if key != expected_bag :
            answer += 1
        traveled_bag.add(key)
        for node in reverse_bag_graph[key] :
            dfs(node)

dfs(expected_bag)
print(answer)