# n = int(input())
# s = 0
# a = 0
# for i in range(n):
#     s += int(input())
#     a = s / n
# print(s, '%.5f' % float(a))

# while循环
num = 10
i = 1
while i <= num:
    i += 1
    if i % 2 == 0:
     print("我是双数：%d" % i)
    # continue #跳出当前循环，继续执行下面的循环
    break #跳出循环并且终止循环

# for循环
s="python"
for s1 in s:
    print(s1,end=' ')
print("\n",len(s),sep='')
print(s[1])

# 嵌套循环
lists=["a","b","c"]
i=0
while True:
    for list in lists:
        print(list)
        if list == "a":
            break
    if i>=2:
         break
    i+=1

