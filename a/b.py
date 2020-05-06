n = int(input())
a = list(map(int, input().split()))


# def f(sum_n):
#     temp = 0
#     if(sum_n % 2 != 0):
#         return False
#     sum_n = sum_n / 2
#     for i in a:
#         temp += i
#         if (temp == sum_n):
#             return True

#     return False


if (sum(a) % 2 == 0):
    result = 0
else:
    count = 0

    sum_n = sum(a) // 2

    temp = 0

    temp_b = 0

    pos = 0

    for i in a:
        temp += i
        if (temp > sum_n):
            pos = count
            break
        temp_b = temp
        count += 1

    result = temp - temp_b - 1

print(result)
