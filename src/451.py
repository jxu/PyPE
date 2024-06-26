# Finding largest squareroot of 1 mod n, != -1 mod n
# By Chinese Remainder Theorem, x^2 = 1 mod n can be determined uniquely by
# x^2 = 1 mod p1^e1, = 1 mod p2^e2, ...
# For odd p, it can be shown the only sols for x^2 = 1 mod p^e are +-1:
# p^e | (x+1)(x-1) => p | (x+1)(x-1)
# Since p is odd, p divides exactly one of (x+1), (x-1)
# All copies of p in p^e divide one of (x+1), (x-1)
# For p = 2, the squareroots for e >= 3 are +-1 and 2^(e-1) +- 1
# https://math.stackexchange.com/q/2693243
# So try all combinations of squareroots for prime powers and combine with CRT
# (I(n) given by A284254)

from number import linear_sieve, linear_sieve_factors, crt
from itertools import product

lp = linear_sieve(2 * 10**7)

def I(n):
    pp = linear_sieve_factors(lp, n)
    rs_list = []
    ms = [p**e for p,e in pp.items()]
    for p, e in pp.items():
        if p == 2:
            if e == 1: rs = (1,)
            elif e == 2: rs = (1,-1)
            else: rs = (1, -1, 2**(e-1) + 1, 2**(e-1) - 1)
        else:
            rs = (1, -1)
        rs_list.append(rs)

    max_r = 0
    for rs in product(*rs_list):
        r, m = crt(rs, ms)
        if (r % m) != m-1:
            max_r = max(max_r, r)

    return max_r


print(sum(I(n) for n in range(3, 2 * 10**7 + 1)))
