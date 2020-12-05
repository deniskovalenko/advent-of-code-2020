
from math import floor, ceil
#128 rows, binary split, 7 chars F/B, F - lower half. 3 chars -> R / L. one of 8 seats in a row. R - upper half

def read_boarding_passes():
    filename = 'day_5_input.txt'

    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    return content

def decode_seat_id(row, column):
    return row*8+column


def decode_boarding_pass(p):
    min = 0 #32
    max = 127 #47

    #todo kinda duplication, but screw it
    for i in range(7):
        front_or_back = p[i]
        
        if front_or_back == 'F':
            max = min + floor((max - min) / 2)
        else:
            min = min + ceil((max - min) / 2)
    
    row = max

    min = 0
    max = 7
    for i in range(7, 10):
        left_or_right = p[i]
        if left_or_right == 'L':
            max = min + floor((max - min) / 2)
        else:
            min = min + ceil((max - min) / 2)
    column = max
    print(p, row, column, decode_seat_id(row, column))
    return (row, column)

assert(decode_boarding_pass('FBFBBFFRLR') == (44, 5))
assert(decode_boarding_pass('FFFBBBFRRR') == (14, 7))
assert(decode_boarding_pass('BBFFBBFRLL') == (102, 4))


def find_higher_seat_id_on_boarding_passes():
    passes = read_boarding_passes()
    # print(passes)
    
    max_id = 0
    for p in passes:
        row, column = decode_boarding_pass(p)
        seat_id = decode_seat_id(row, column)
        if seat_id > max_id:
            max_id = seat_id

    return max_id


print(find_higher_seat_id_on_boarding_passes())

def find_my_seat():
    passes = read_boarding_passes()
    rows_columns = [decode_boarding_pass(x) for x in passes] 
    ids = [decode_seat_id(*x) for x in rows_columns]
    
    #the seats with IDs +1 and -1 from yours will be in your list... 
    # I need to find a "gap' of 1 in seatIDs -> 456, 458 and then I'm 457. 
    # Can sort all the seats and find a gap...
    sorted_elements = sorted(ids)
    print(sorted_elements)
    prev_id = sorted_elements[0]
    for current in sorted_elements:
        if prev_id < (current -1):
            print(prev_id, current)
            return current - 1
        prev_id = current
    
    return None

print(find_my_seat())


"""
--- Part Two ---

Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?

"""



"""
--- Day 5: Binary Boarding ---

You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control.

You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input); perhaps you can find your seat through process of elimination.

Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.

The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

    Start by considering the whole range, columns 0 through 7.
    R means to take the upper half, keeping columns 4 through 7.
    L means to take the lower half, keeping columns 4 through 5.
    The final R keeps the upper of the two, column 5.

So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.

As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

"""