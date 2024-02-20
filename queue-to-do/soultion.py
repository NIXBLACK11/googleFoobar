# 17 18 19 20 /
# 21 22 23 / 24
# 25 26 / 27 28
# 29 / 30 31 32

# This solution is slow

# def solution(start, length):
#     ans = 0
#     num = start
#     for i in range(0, length):
#         for j in range(i, length):
#             # print(num," ", end="")
#             ans = ans^num
#             num = num+1
#         # print()
#         num = num+i
#     return ans



# This solution uses the xor property


def solution(start, length):
    ans = 0

    for i in range(0, length):
        first = start + (length * i)
        last = first + (length - i) - 1

        xor = []
        if first % 2 == 0:
            xor = [last, 1, last + 1, 0]
        else:
            xor = [first, first ^ last, first - 1, (first - 1) ^ last]

        ans = ans ^ xor[(last - first) % 4]

    return ans

print(solution(0, 3))
print(solution(17, 4))