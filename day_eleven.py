from utils import read_input_lines
import copy

seating = read_input_lines('day_11.txt')
for i in range(len(seating)):
    seating[i] = list(seating[i])

print(len(seating))
print(len(seating[0]))

def count_occupied_adjacent_seats(seating_state, row, column):
    row_count = len(seating_state)
    column_count = len(seating_state[0])
    occupied_count = 0

    for r in range(row - 1, row + 2):
        for c in range(column - 1, column + 2):
            #out of bound or "target" place
            if r < 0 or r > row_count - 1 or c < 0 or c > column_count - 1 or (c == column and r == row):
                continue
            
            seat = seating_state[r][c]
            if seat == '#':
                occupied_count += 1

    return occupied_count

#to see first seat in the direction
def count_occupied_adjacent_seats_2(seating_state, row, column):
    row_count = len(seating_state)
    column_count = len(seating_state[0])
    occupied_count = 0

    for direction in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        r = row
        c = column
        searching = True
        while searching:
            r += direction[0]
            c += direction[1]
            if r < 0 or r > row_count - 1 or c < 0 or c > column_count - 1:
                searching = False
                break
            place = seating_state[r][c]
            if place == '#':
                occupied_count += 1
                searching = False
            if place == 'L':
                searching = False
                break

    return occupied_count


# assert count_occupied_adjacent_seats_2(seating, 3, 3) == 0
# assert count_occupied_adjacent_seats_2(seating, 1, 2) == 6

example = [['#', '.', '#'],
           ['#', '#', '#'],
           ['#', '.', '#']]

r = count_occupied_adjacent_seats(example, 1, 1) 
print(r)
assert r == 6



def iterate_through_seating(initial_seating):
    
    current_seating = copy.deepcopy(initial_seating)
    count_of_updates = -1

    print("Let's start")
    for l in current_seating:
            print(l)

    while count_of_updates != 0:
        count_of_updates = 0

        new_seating = copy.deepcopy(current_seating)
        row_count = len(new_seating)
        column_count = len(new_seating[0]) 
        for row in range(row_count):
            for column in range(column_count):
                current_seat = current_seating[row][column]
                if current_seat == '.':
                    #do nothing
                    continue
            
                occupied_seats_count = count_occupied_adjacent_seats(current_seating, row, column)
                if current_seat == 'L' and occupied_seats_count == 0:
                    new_seating[row][column] = '#'
                    count_of_updates +=1
                    continue
                if current_seat == '#' and occupied_seats_count >= 4:
                    new_seating[row][column] = 'L'
                    count_of_updates +=1
                    continue
        current_seating = copy.deepcopy(new_seating)
        # print("\n")
        # for l in current_seating:
        #     print(l)
        # print("\n")

    print("reached stable state")
    count_of_occupied = 0
    for row in range(row_count):
        for column in range(column_count):
            if current_seating[row][column] == '#':
                count_of_occupied +=1
    
    return count_of_occupied




def iterate_through_seating_part_2(initial_seating):
    
    current_seating = copy.deepcopy(initial_seating)
    count_of_updates = -1

    print("Let's start")
    for l in current_seating:
            print(l)

    while count_of_updates != 0:
        count_of_updates = 0

        new_seating = copy.deepcopy(current_seating)
        row_count = len(new_seating)
        column_count = len(new_seating[0]) 
        for row in range(row_count):
            for column in range(column_count):
                current_seat = current_seating[row][column]
                if current_seat == '.':
                    #do nothing
                    continue
            
                occupied_seats_count = count_occupied_adjacent_seats_2(current_seating, row, column)
                if current_seat == 'L' and occupied_seats_count == 0:
                    new_seating[row][column] = '#'
                    count_of_updates +=1
                    continue
                if current_seat == '#' and occupied_seats_count >= 5:
                    new_seating[row][column] = 'L'
                    count_of_updates +=1
                    continue
        current_seating = copy.deepcopy(new_seating)
        # print("\n")
        # for l in current_seating:
        #     print(l)
        # print("\n")

    print("reached stable state")
    count_of_occupied = 0
    for row in range(row_count):
        for column in range(column_count):
            if current_seating[row][column] == '#':
                count_of_occupied +=1
    
    return count_of_occupied




# assert count_occupied_adjacent_seats(seating, 0, 0) == 0
# assert count_occupied_adjacent_seats(seating, len(seating), 0) == 0

print(iterate_through_seating_part_2(seating))
"""
--- Day 11: Seating System ---

Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.

Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##

After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##

This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##

#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##

#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##

At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?



--- Part Two ---

As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. For example, the empty seat below would see eight occupied seats:

.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....

The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

.............
.L.L.#.#.#.#.
.............

The empty seat below would see no occupied seats:

.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.

Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##

#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#

#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#

Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?



"""