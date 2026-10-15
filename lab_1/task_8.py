def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(f'Swap elements at indices {i + 1} and {min_idx + 1}.')


def main():
    filename = 'input_task8_max'
    with open(filename, 'r', encoding='utf-8') as fi:
        list_size = int(fi.readline())
        input_list = list(map(int, fi.readline().split()))
        selection_sort(input_list)
        print('No more swaps needed.')


if __name__ == '__main__':
    main()