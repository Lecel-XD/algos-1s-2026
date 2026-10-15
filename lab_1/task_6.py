def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

def main():
    filename = 'input_task5_min'
    with open(filename, 'r', encoding='utf-8') as fi:
        list_size = int(fi.readline())
        input_list = list(map(int, fi.readline().split()))
        bubble_sort(input_list)
        print(*input_list)


if __name__ == '__main__':
    main()