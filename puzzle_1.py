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
    if missing_delta in delta_map:
      return missing_delta * current_number
    delta_map[current_number] = i
      
  return None
  

elements = [1721, 979,   366,  299,  675,  1456 ]

print(find_two_elements_that_sum_up_to_n(elements, 2020))


"""--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""

def find_three_elements_that_sum_up_to_n(elements, sum):
  # idea #1 -> compute all 2-sums, then do as in first part (N^2)
  # idea #2 -> sort maybe? Then I kind of know where to look roughly with binary search?        (N logN + N)
  # elements = [1721, 979,   366,  299,  675,  1456 ]
  # sorted = [299, 366, 675, 979, 1456, 1721]
  #how do I find three-sum? 
  #we should look at elements < 2020 (target sum) (if we have positive integer limitation)
  #for every element:
  #     we need to find 2 elements that sum to 2020 - element (which is linear problem according to previous solution)
  for i in range(len(elements)):
    elements_to_the_right = elements[i+1:]
    current_el = elements[i]
    target_2_sum = sum - current_el
    two_sum_product = find_two_elements_that_sum_up_to_n(elements_to_the_right, target_2_sum)
    if two_sum_product is not None:
      return current_el * two_sum_product
  return None


print(find_three_elements_that_sum_up_to_n(elements, 2020))