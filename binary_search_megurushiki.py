a = [1, 14, 32, 51, 51, 51, 243, 419, 750, 910]


def binary_search(key, list_):
    def isOK(index, key):
        if a[index] >= key:
            return True
        return False
    ng = -1
    ok = len(list_)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if isOK(mid, key):
            ok = mid
        else:
            ng = mid
    return ok


if __name__ == "__main__":
    print(binary_search(51, a))  # Output : 3
    print(binary_search(1, a))  # Output : 0
    print(binary_search(52, a))  # Output : 6
