# Uses python3

def calc_fib_fast(n):
    seq = [0, 1]
    while len(seq) < n + 1:
        seq += [seq[len(seq)-1] + seq[len(seq)-2]]
    return seq[n]

n = int(input())
print(calc_fib_fast(n))
