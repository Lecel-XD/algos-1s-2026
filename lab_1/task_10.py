def palindrome(string):
    arr = [0] * 26
    for sym in string:
        arr[ord(sym) - ord('A')] += 1
    result = ''
    center = ''
    for i in range(26):
        char, cnt = chr(ord('A') + i), arr[i]
        result +=  char * (cnt // 2)
        if (cnt % 2) and not center:
            center = char
    return result + center + result[::-1]


def main():
    filename = 'input_task10_min'
    with open(filename, 'r', encoding='utf-8') as fi:
        list_size = int(fi.readline())
        symbols = fi.readline().strip()
        print(palindrome(symbols))


if __name__ == '__main__':
    main()