def calc_fib(n: int) -> int:
    if n < 0:
        raise ValueError('"n" can\'t be negative')
    if n < 2: return n
    prev = 0
    curr = 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

if __name__ == '__main__':
    print(calc_fib(45))