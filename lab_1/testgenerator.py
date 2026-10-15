with open('input_task8_max', 'w', encoding='utf-8') as fo:
    r = list(map(str, range(10**9, 10**9 - 5000, -1)))
    print(len(r), file=fo)
    print(' '.join(r), file=fo)