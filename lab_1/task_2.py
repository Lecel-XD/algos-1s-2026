def insertion_sort(arr):
    new_indexes = [1]
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
        new_indexes.append(i + 2)
    return new_indexes, arr


def main():
    filename = 'input_task2_ex'
    with open(filename, 'r', encoding='utf-8') as fi:
        items_amount = int(fi.readline())
        input_list = list(map(int, fi.readline().split()))
        indexes, new_list = insertion_sort(input_list)
        print(*indexes)
        print(*new_list)

if __name__ == '__main__':
    main()


