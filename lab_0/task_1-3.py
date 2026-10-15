def main():
    filename = 'input_task1-3_max'
    with open(filename, 'r', encoding='utf-8') as fi:
        a, b = map(int, fi.readline().split())
    print(a + b)

if __name__ == '__main__':
    main()