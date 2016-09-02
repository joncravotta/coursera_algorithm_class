# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

# result = 0
#
# for i in range(0, n):
#     for j in range(i+1, n):
#         if a[i]*a[j] > result:
#             result = a[i]*a[j]
# print(result)


# Faster soulution
result = 0
max_first = int(0)
max_second = int(0)
for i in range(0, n):
    if a[i] > max_first:
        max_second = max_first
        max_first = a[i]
    elif a[i] > max_second:
        max_second = a[i]
result = max_first * max_second
print(result)
