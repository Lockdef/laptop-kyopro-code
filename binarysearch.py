a = [1, 14, 32, 51, 51, 51, 243, 419, 750, 910]


def binary_search(key):
    left = 0  # 配列aの左端
    right = len(a) - 1  # 配列aの右端
    while (right >= left):
        mid = left + (right - left) // 2  # 区間の真ん中
        if a[mid] == key:
            return mid
        elif a[mid] > key:
            right = mid - 1
        elif a[mid] < key:
            left = mid + 1
    return -1


if __name__ == "__main__":
    print(51, binary_search(51))
    print(1, binary_search(1))
    print(910, binary_search(910))
    print(52, binary_search(52))
