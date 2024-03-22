# 1. 整型和浮点型可以相互转换
# 2.有的字符串可以转换成整型，本身就是字符串的不可以转换为整型
'''
a = "193"
c = int(a)
print(c)
print(type(a))
print(type(c))
'''
'''
# b="a"
# d=int(b)
# print(d)
'''

a, b, c = input().split()
if b == "0" and c == "/":
    print("不成立！")
elif c not in "+-*/":
    print("不成立！")
else:
    print(int(eval(a+c+b)))

