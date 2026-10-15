def calc_fib_last_digit(n: int) -> int:
    if n < 0:
        raise ValueError('"n" must be non-negative')
    if n < 2: return n
    prev = 0
    curr = 1
    for _ in range(2, n + 1):
        prev, curr = curr, (prev + curr) % 10
    return curr

if __name__ == '__main__':
    print(calc_fib_last_digit(327305))