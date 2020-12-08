from typing import TypeVar, List, Sequence, Dict

#You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the !!!outermost!!!!! bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)
#don't care of "how many" bags can bag contain, only unique colors (might be for later), unless it can contain 0...
#sounds like a graph/tree progblem, and I want # of unique paths that "finish" in targetColor. 
#so I kind of do BFS/DFS, and when reach gold stop and increment counter


# class Tree(object):
#     def __init__(self):
#         self.color: str = None
#         self.childNodes: Sequence[Tree] = None


#do I actually need to build a tree, or traverse kind of virtual tree, aka knowing the color I can find colors it containes from "rule" (aka 1 level tree, and for each child I can do the same... 
# what if there's a cycle? 



class Rule(object):
    def __init__(self):
        self.color = None
        self.count = None
        self.child_nodes = {}


    def __str__(self):
        return self.color + str(self.count) + str(self.child_nodes)

    def __repr__(self):
        return "Color: " + self.color + ", count: " + str(self.count) + ", child_nodes: " + str(self.child_nodes) + "\n"

def read_rules():
    filename = 'day_7_input.txt'

    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    # print(content)
    return content

def parse_rule(rule):
    # print(rule)
    #very dirty and a lot of assumptions
    tokens = rule.split(' ')
    # print(tokens)

    rule = Rule()
    rule.color = tokens[0] + ' ' + tokens[1]
    if tokens[4] == "no":
        rule.child_nodes = {}
        return rule
        
    read_further = True
    offset = 4
    while read_further:
        count = int(tokens[offset])
        color = tokens[offset+1] + ' ' + tokens[offset+2]
        r = Rule()
        r.color = color
        r.count = count
        rule.child_nodes[color] = r

        split_symbol = tokens[offset+3]

        if split_symbol == "bags." or split_symbol == "bag.":
            read_further = False
        else:
            offset = offset + 4
    
    return rule
    


def parse_rules(rules: Sequence[str]):
    rules = [parse_rule(x) for x in rules]
    rule_map = {}
    for r in rules:
        rule_map[r.color] = r
    return rule_map

# def build_tree_from_rules(rules) -> Tree:
#     return None

def check_bag_can_contain_color(rules: Dict[str, Rule], current_color: str, target_color: str) -> bool:
    count = 0
    if target_color in rules[current_color].child_nodes:
        return 1

    for r in rules[current_color].child_nodes.values():
        rule = rules[r.color]
        count += check_bag_can_contain_color(rules, rule.color, target_color)

    # print(current_color.color, count)
    return 1 if count > 0 else 0
            

def count_unique_path_parts_finishing_in_target_color(rules: Dict[str, Rule], target_color):
    count = 0

    #now some kind of search...
    for rule in rules.values(): #dark orange
        count += check_bag_can_contain_color(rules, rule.color, target_color)

    return count


rules_str = read_rules()
rules = parse_rules(rules_str)
print(rules.values())

# tree = build_tree_from_rules(rules)
my_color = "shiny gold"
result = count_unique_path_parts_finishing_in_target_color(rules, my_color)
print(result)


def count_how_many_bags_my_bag_should_contain(rules: Dict[str, Rule], target_color):
    top_level_bag = rules[target_color]
    count = 0
    for bag_to_put_inside in top_level_bag.child_nodes.values():
        how_many_bags_like_this_i_need = top_level_bag.child_nodes[bag_to_put_inside.color].count
        count += how_many_bags_like_this_i_need
        bags_inside_the_bag = count_how_many_bags_my_bag_should_contain(rules, bag_to_put_inside.color)
        count += bags_inside_the_bag * how_many_bags_like_this_i_need
    #cry in programmers
    return count


print(count_how_many_bags_my_bag_should_contain(rules, my_color))

"""
--- Day 7: Handy Haversacks ---

You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

    A bright white bag, which can hold your shiny gold bag directly.
    A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
    A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
    A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.

So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)



--- Part Two ---

It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

    faded blue bags contain 0 other bags.
    dotted black bags contain 0 other bags.
    vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
    dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.

So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.

In this example, a single shiny gold bag must contain 126 other bags.

"""