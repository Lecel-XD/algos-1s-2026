def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


def main():
    filename = 'input_task1_max'
    with open(filename, 'r', encoding='utf-8') as fi:
        items_amount = int(fi.readline())
        input_list = list(map(int, fi.readline().split()))
        result = insertion_sort(input_list)
    with open('output.txt', 'w', encoding='utf-8') as fo:
        print(' '.join(map(str, result)), file=fo)

if __name__ == '__main__':
    main()


