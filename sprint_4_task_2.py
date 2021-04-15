from string import ascii_lowercase
from itertools import permutations
import random


arr_seq = {}


def gen_arr():
    for c in ascii_lowercase:
        arr_seq[c] = poly_hash(c)


def r():
    ar1 = ''.join([random.choice(ascii_lowercase) for _ in range(20)])
    ar2 = ''.join([random.choice(ascii_lowercase) for _ in range(20)])
    ph1 = poly_hash(ar1)
    ph2 = poly_hash(ar2)
    d = 0
    while ph1 != ph2:
        print(ar1, ar2)
        ar1 = ''.join([random.choice(ascii_lowercase) for _ in range(20)])
        ar2 = ''.join([random.choice(ascii_lowercase) for _ in range(20)])
        ph1 = poly_hash(ar1)
        ph2 = poly_hash(ar2)
        d += 1
        if d >= 100000:
            print(d)
            break


def poly_hash(s):
    a = 1000
    m = 123987123
    if len(s) > 0:
        p_hash = ord(s[0])
        for c in s[1:]:
            p_hash = (p_hash * a + ord(c)) % m
        return p_hash % m
    return 0


def main():
    # abcdefghijklmnopqrstuvwxyz

    a = 'ezhgeljkablzwnvuwqvp'
    b = 'gbpdcvkumyfxillgnqrv'

    r()



if __name__ == '__main__':
    main()
