def linear_search(arr, v):
    indexes = []
    for idx in range(len(arr)):
        if arr[idx] == v:
            indexes.append(idx + 1)
    return indexes

def main():
    filename = 'input_task4_min'
    with open(filename, 'r', encoding='utf-8') as fi:
        input_list = fi.readline().split()
        v = fi.readline().strip()
        result = linear_search(input_list, v)
        if not result:
            print(-1)
        elif len(result) == 1:
            print(result[0])
        else:
            print(len(result), ', '.join(map(str, result)), sep='\n')


if __name__ == '__main__':
    main()