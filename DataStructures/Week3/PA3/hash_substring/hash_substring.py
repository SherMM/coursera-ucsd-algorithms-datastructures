# python3
import string
import random

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def precompute_hashes(text, psize, p, x):
    hashes = [0] * (len(text) - psize + 1)
    s = text[len(text)-psize: len(text)]
    hashes[len(text)-psize] = poly_hash(s, p, x)
    y = 1
    for i in range(0, psize):
        y = (y * x) % p
    for i in range(len(text)-psize-1, -1, -1):
        hashes[i] = (x * hashes[i+1] + ord(text[i]) - y * ord(text[i+psize])) % p
    return hashes

def poly_hash(pattern, p, x):
    h_val = 0
    for i in range(len(pattern)-1, -1, -1):
        h_val = (h_val * x + ord(pattern[i])) % p
    return h_val

def get_occurrences(pattern, text):
    p = 1000000007
    x = random.randrange(1, p)
    phash = poly_hash(pattern, p, x)
    hashes = precompute_hashes(text, len(pattern), p, x)
    indexes = []
    for i in range(len(hashes)):
        if phash == hashes[i]:
            indexes.append(i)
    return indexes

def test():
    alpha = string.ascii_lowercase
    n = 5*(10**5)
    p = 100000
    patt = [random.choice(alpha) for _ in range(p)]
    text = [random.choice(alpha) for _ in range(n)]
    text[50:50+p] = patt
    patt = ''.join(patt)
    text = ''.join(text)
    print(get_occurrences(patt, text))



if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
    #test()
