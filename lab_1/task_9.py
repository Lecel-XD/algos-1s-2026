def add_binary(num1: str, num2: str) -> str:
    n = len(num1)
    carry = 0
    result = [0] * (n + 1)
    for i in range(-1, - n - 1, -1):
        s = int(num1[i]) + int(num2[i]) + carry
        result[i] = s % 2
        carry = s // 2
    result[0] = carry
    return ''.join(map(str, result))



def main():
    filename = 'input_task9_min'
    with open(filename, 'r', encoding='utf-8') as fi:
        num1, num2 = fi.readline().split()
        print(add_binary(num1, num2))


if __name__ == '__main__':
    main()