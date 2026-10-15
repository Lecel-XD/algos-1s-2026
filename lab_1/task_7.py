# def insertion_sort(arr):
#     for j in range(1, len(arr)):
#         key = arr[j]
#         i = j - 1
#         while i >= 0 and arr[i][0] > key[0]:
#             arr[i + 1] = arr[i]
#             i -= 1
#         arr[i + 1] = key
#
#
# def main():
#     filename = 'input_task7_max'
#     with open(filename, 'r', encoding='utf-8') as fi:
#         list_size = int(fi.readline())
#         citizens = [(float(v), n) for n, v in enumerate(fi.readline().split(), 1)]
#         insertion_sort(citizens)
#         print(citizens[0][1], citizens[list_size // 2][1], citizens[-1][1])


def insertion_sort(arr):
    n = len(arr)
    order = list(range(n))
    for j in range(1, n):
        key = order[j]
        i = j - 1
        while i >= 0 and arr[order[i]] > arr[key]:
            order[i + 1] = order[i]
            i -= 1
        order[i + 1] = key
    return order


def main():
    filename = 'input_task7_ex'
    with open(filename, 'r', encoding='utf-8') as fi:
        list_size = int(fi.readline())
        citizens = list(map(float, fi.readline().split()))
        order = insertion_sort(citizens)
        print(order[0] + 1, order[list_size // 2] + 1, order[-1] + 1)


if __name__ == '__main__':
    main()