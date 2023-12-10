# def sortwyb(a):
#     for i in range(len(a) - 1):
#         pom = i
#
#         for j in range(i + 1, len(a)):
#             if a[j] < a[pom]:
#                 pom = j
#
#         a[i], a[pom] = a[pom], a[i]
#     return a


def simple_sort(a):
    return sorted(a, reverse=True)


a = "dubovyi"

# print(f"lyceum result: {sortwyb(a)}")
print(f"simple sort: {simple_sort(a)}")

