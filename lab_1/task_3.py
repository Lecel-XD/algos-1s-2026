def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] < key:
            swap(arr, i + 1, i)
            i -= 1


def recursive_insertion_sort(arr, idx=None):
    if idx is None: idx = len(arr)
    if idx == 1: return
    recursive_insertion_sort(arr, idx - 1)
    key = arr[idx - 1]
    i = idx - 2
    while i >= 0 and arr[i] < key:
        arr[i + 1] = arr[i]
        i -= 1
    arr[i + 1] = key
    return

def main():
    filename = 'input_task3_max'
    with open(filename, 'r', encoding='utf-8') as fi:
        items_amount = int(fi.readline())
        input_list = list(map(int, fi.readline().split()))
        # recursive_insertion_sort(input_list)
        insertion_sort(input_list)
        print(input_list)

if __name__ == '__main__':
    main()