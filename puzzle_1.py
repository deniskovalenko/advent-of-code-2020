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
  

elements = [
1082,
1770,
1104,
1180,
1939,
1952,
1330,
1569,
1120,
1281,
1144,
1091,
2008,
1967,
1863,
1819,
1813,
1986,
1099,
1860,
1686,
1063,
1620,
1107,
1095,
951,
1897,
1246,
1264,
1562,
1151,
1980,
1942,
1416,
1170,
1258,
1075,
1882,
1329,
2003,
66,
1249,
1302,
1221,
1828,
1154,
1662,
1103,
1879,
1205,
1936,
1472,
1816,
1071,
1237,
1467,
1919,
942,
74,
1178,
1949,
1947,
1613,
1931,
1332,
24,
1987,
1796,
1256,
1981,
1158,
1114,
2004,
1696,
1775,
1718,
1102,
1998,
1540,
1129,
1870,
1841,
1582,
1173,
1417,
1604,
1214,
1941,
1440,
1381,
1149,
1111,
1766,
1747,
1940,
960,
1449,
1171,
1584,
1926,
1065,
1832,
1633,
1245,
1889,
1906,
1198,
1959,
1340,
1951,
1347,
1097,
1660,
1957,
1134,
1730,
1105,
1124,
1073,
1679,
1397,
1963,
1136,
1983,
1806,
1964,
1821,
1997,
1254,
1823,
1092,
1119,
2000,
1089,
1933,
1478,
1923,
1576,
1571,
415,
1875,
1937,
1112,
1831,
1969,
1506,
1929,
1960,
1322,
110,
1141,
1080,
1603,
1126,
1036,
1762,
1904,
1122,
1988,
1962,
1958,
1953,
1068,
1188,
1483,
1518,
1471,
1961,
1217,
1559,
1789,
1523,
2007,
1093,
1745,
1955,
1948,
1474,
1628,
691,
1398,
1876,
1650,
1838,
1950,
1088,
1697,
1977,
1364,
1966,
1945,
1975,
1606,
1974,
1847,
1570,
1148,
1599,
1772,
1970
]

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