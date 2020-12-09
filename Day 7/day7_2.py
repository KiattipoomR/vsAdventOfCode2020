from collections import defaultdict

bag_graph = defaultdict(dict)

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
            processed_bags[idx] = {bag[first:last - 4]: int(bag[:first - 1])}
        else : 
            processed_bags[idx] = None

    return processed_bags    

with open('day7.txt') as f :
    for line in f :
        line = line.strip()
        bag, bag_args = line.split(' contain ')
        bag = bag[:-5]
        bag_args = process_bags(bag_args.split(', '))
        for bag_arg in bag_args :
            if bag_arg != None :
                bag_graph[bag].update(bag_arg)

expected_bag = 'shiny gold'
answer = 0

def dfs(key) :
    stored_bags = 0
    for bag, amount in bag_graph[key].items() :
        stored_bags += (dfs(bag) * amount) + amount
    return stored_bags

print(dfs(expected_bag))