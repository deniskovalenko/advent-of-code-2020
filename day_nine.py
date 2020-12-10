from utils import read_input_numbers

numbers = read_input_numbers("day_9.txt")

#find "first" number that doensn't consist of a pair of past 25 numbers.

def find_first_invalid_number(numbers, window_size):
    preamble = numbers[:window_size]
    rest = numbers[window_size:]

    #brute force -> build "past N" elements array every time, go through it N^2 to find pairs matching the "current number"
    #N^2 * M where M is length and N is window_size
    #Another thing -> keep "hashmap" of past N elements, removing the first one and adding the last one. 
    #then I can go through it once and search for "matching element Sum - current". N * M. 
    #problem is how to delete elements from hashmap in order of addition. Can be also a queue, that tells the "key" of the last-added
    #number. Why do I need map then? Just set would do. 
    #but can there be only unique numbers in the WINDOW??? If not hashmap works, but poorely


    #wait, why do I need queue if I have array and I can have pointers? :) 
    matching_numbers = {}
    for i in range(len(preamble)):
        matching_numbers[preamble[i]] = i

    left_most_elemen_index = 0
    rightmost_index = window_size - 1
    for i in range(window_size, len(rest)):
        found = False
        target_sum = numbers[i]
        for j in range(left_most_elemen_index, left_most_elemen_index + window_size):
            current_number = numbers[j]
            missing_match =  target_sum - current_number
            if missing_match in matching_numbers and j != matching_numbers[missing_match]:
                found = True
                break
        
        if not found:
            return numbers[i]
        
        del matching_numbers[numbers[left_most_elemen_index]]
        left_most_elemen_index+=1
        rightmost_index += 1
        matching_numbers[numbers[rightmost_index]] = rightmost_index

    return None

# print(find_first_invalid_number(numbers, 25))


def find_subsequence(numbers, target_sum):
    left = 0
    sum = 0

    for right in range(len(numbers)):
        sum += numbers[right]

        while sum > target_sum:
            sum -= numbers[left]
            left += 1
        
        if sum == target_sum and left < right:
            return (left, right + 1)

    return None

assert(find_subsequence([3, 2, 5, 6], 7)  == (1,3))
assert(find_subsequence([3, 2, 5, 6], 20) is None)

#part 2
def find_contigious_sequence_summing_to_invalid_num(numbers, window_size):
    invalid_number = find_first_invalid_number(numbers, window_size)
    min,max = find_subsequence(numbers, invalid_number)
    print("Found sequence ",  min, max)
    subsequence = numbers[min:max]
    print(type(subsequence))
    print(subsequence)
    # m = min(list(subsequence))
    # ma = max(list(subsequence))
    return subsequence


seq = find_contigious_sequence_summing_to_invalid_num(numbers, 25)
print(min(seq))
print(max(seq))

    
    

        


"""
--- Day 9: Encoding Error ---

With your neighbor happily enjoying their video game, you turn your attention to an open data port on the little screen in the seat in front of you.

Though the port is non-standard, you manage to connect it to your computer through the clever use of several paperclips. Upon connection, the port outputs a series of numbers (your puzzle input).

The data appears to be encrypted with the eXchange-Masking Addition System (XMAS) which, conveniently for you, is an old cypher with an important weakness.

XMAS starts by transmitting a preamble of 25 numbers. After that, each number you receive should be the sum of any two of the 25 immediately previous numbers. The two numbers will have different values, and there might be more than one such pair.

For example, suppose your preamble consists of the numbers 1 through 25 in a random order. To be valid, the next number must be the sum of two of those numbers:

    26 would be a valid next number, as it could be 1 plus 25 (or many other pairs, like 2 and 24).
    49 would be a valid next number, as it is the sum of 24 and 25.
    100 would not be valid; no two of the previous 25 numbers sum to 100.
    50 would also not be valid; although 25 appears in the previous 25 numbers, the two numbers in the pair must be different.

Suppose the 26th number is 45, and the first number (no longer an option, as it is more than 25 numbers ago) was 20. Now, for the next number to be valid, there needs to be some pair of numbers among 1-19, 21-25, or 45 that add up to it:

    26 would still be a valid next number, as 1 and 25 are still within the previous 25 numbers.
    65 would not be valid, as no two of the available numbers sum to it.
    64 and 66 would both be valid, as they are the result of 19+45 and 21+45 respectively.

Here is a larger example which only considers the previous 5 numbers (and has a preamble of length 5):

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576

In this example, after the 5-number preamble, almost every number is the sum of two of the previous 5 numbers; the only number that does not follow this rule is 127.

The first step of attacking the weakness in the XMAS data is to find the first number in the list (after the preamble) which is not the sum of two of the 25 numbers before it. What is the first number that does not have this property?


--- Part Two ---

The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

Again consider the above example:

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576

In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127. (Of course, the contiguous set of numbers in your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number in this contiguous range; in this example, these are 15 and 47, producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?


"""