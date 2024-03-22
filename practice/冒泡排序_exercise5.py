arr = [60, 34, 5, 6, 7, 14, 78, 90, 100]
n = len(arr)
print(n)
# 遍历数组。 遍历(Traversal)，是指沿着某条搜索路线，依次对树中每个结点均做一次且仅做一次访问。访问结点所做的操作依赖于具体的应用问题。（先序，中序，后序，广度，深度）
for i in range(n):
    for j in range(0, n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)

# 可以直接用函数.sort()从大到小排列

arr = [3, 6, 12, 3, 145, 123, 456, 122, 109]
arr.sort()
print(arr)
