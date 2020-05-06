a = [1, 14, 32, 51, 51, 51, 243, 419, 750, 910]


def isOK(index, key):
    if a[index] >= key:
        return True
    else:
        return False


def binary_search(key):
    left = -1
    right = len(a)

    while(right - left > 1):
        mid = left + (right - left) // 2
        if isOK(mid, key):
            right = mid
        else:
            left = mid

    return right


if __name__ == "__main__":
    print(binary_search(51))
    print(binary_search(1))
    print(binary_search(910))
    print(binary_search(911))
