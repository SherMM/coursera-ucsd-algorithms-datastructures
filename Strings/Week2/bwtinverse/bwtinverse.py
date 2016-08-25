# python3
import sys
from collections import defaultdict


def generate_substrings(text):
    items = list(text)
    items.sort()
    return ''.join(items)

def assign_appearance_count(text):
    '''
    Returns list of tuples, where the first item 
    is the letter in text and the second item
    is an integer showing which appearance of that
    letter the current letter is (ex. the k-th a,
    the k-th g, etc.)
    '''
    count = defaultdict(int)
    tups = []
    for letter in text:
        tups.append((letter, count[letter]))
        count[letter] += 1
    return tups


def map_first_to_last(first, last):
    f_pos = assign_appearance_count(first)
    l_pos = assign_appearance_count(last)
    
    # set up mapping of first to last
    conv = dict(zip(f_pos, l_pos))
    start = f_pos[0]
    curr, cycle = start, False
    s = [start[0]]
    while not cycle:
        ptr = conv[curr]
        if ptr != start:
            s.append(ptr[0])
        else:
            cycle = True
        curr = ptr
    return ''.join(s[::-1])
    


def inverse_bwt(bwt):
    first = generate_substrings(bwt)
    return map_first_to_last(first, bwt)


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(inverse_bwt(bwt))
