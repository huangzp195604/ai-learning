# -*- coding: utf-8 -*-
"""
P1 参考答案 —— 写完 day01.py 全部 20 题之后才许看

用法：
  1. 先自己把 20 题写完并跑通（哪怕写得丑）
  2. 打开这个文件，逐题对
  3. 对不上的题，抄一遍正确答案，然后【关掉这个文件，从空白重写一遍】
     写不出来 = 那道题你还是没会，明天重做
"""

# 1
print("Hello Python")

# 2
name = "huangzhipeng"
print(name)

# 3
a = 15
b = 27
print(a + b)

# 4
price = 12.5
qty = 8
print(price * qty)

# 5
print("Amazon" + " " + "FBA")

# 6
name = "女士卫裤"
price = 19.99
print(f"{name} 售价 {price}")

# 7
print(f"{3.14159:.2f}")

# 8
n = int(input("请输入整数："))
print(n + 10)

# 9
p = float(input("请输入价格："))
print(p * 0.8)

# 10
print(17 % 5)

# 11
print(17 // 5)

# 12
print(2 ** 10)

# 13
s = "hello"
print(len(s))

# 14
s = "fba"
print(s.upper())

# 15
s = "SKU-001"
print(s.replace("-", ""))

# 16
a, b = 3, 7
print(a, b, a + b)

# 17
a, b = 3, 7
a, b = b, a
print(a, b)

# 18
r = 5
print(3.14 * r ** 2)

# 19
cost = 45
price = 143.93
print(f"{(price - cost) / price * 100:.1f}%")

# 20
cost = float(input("成本："))
price = float(input("售价："))
print(f"利润 {price - cost:.2f}")
print(f"利润率 {(price - cost) / price * 100:.1f}%")
