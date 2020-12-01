"""
Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?


"""

#can there be negatives? floating points?

def find_two_elements_that_sum_up_to_n(elements, sum):
  delta_map = {}
  for i in range(len(elements)):
    current_number = elements[i]
    missing_delta = sum - current_number
    print(missing_delta)
    if missing_delta in delta_map:
      return missing_delta * current_number
    delta_map[current_number] = i
    print(delta_map)
      
  return None
  

elements = [
  1721,
  979,
  366,
  299,
  675,
  1456
]

print(find_to_elements_that_sum_up_to_n(elements, 2020))
