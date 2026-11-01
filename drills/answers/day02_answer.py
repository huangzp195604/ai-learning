# -*- coding: utf-8 -*-
"""
P1 巩固篇 参考答案 —— 40 题全部写完并跑通之后才许打开

用法：
  1. 自己写完 40 题（哪怕写得丑）
  2. 打开这个文件逐题对
  3. 对不上的：抄一遍 → 关掉 → 从空白重写 → 写不出来就是还没会，明天重做
"""

# 1
print("Python\n2026")

# 2
x = 10
y = 3
print(x * y)

# 3
print("Ha" * 3)

# 4
a = 2
b = 3
c = 4
print(a + b * c)

# 5
print((2 + 3) * 4)

# 6
name = "Amazon"
days = 30
print(f"{name} 库存周转 {days} 天")

# 7
print(f"{1234.5678:.2f}")

# 8
print(f"{0.256 * 100:.1f}%")

# 9
print("结果：" + str(10 + 5))

# 10
print(round(3.14159, 2))

# 11
s = "  FBA  "
print(s.strip())

# 12
s = "Hello World"
print(s.lower())

# 13
s = "python"
print(s.capitalize())

# 14
s = "a,b,c"
print(s.split(","))

# 15
s = "SKU-2024-001"
print(s.split("-"))

# 16
print("amazon" in "amazon fba")

# 17
s = "abcdef"
print(s[0])

# 18
print(s[-1])

# 19
print(s[:3])

# 20
s = "SKU001"
print(s[-3:])

# 21
name = input("请输入名字：")
print(f"你好，{name}")

# 22
a = int(input("第一个整数："))
b = int(input("第二个整数："))
print(a + b)

# 23
r = float(input("半径："))
print(f"{2 * 3.14 * r:.2f}")

# 24
cost = float(input("成本："))
price = float(input("售价："))
print(f"{price - cost:.2f}")

# 25
usd = float(input("美元金额："))
print(f"{usd * 7.2:.2f}")

# 26
sales = float(input("销售额："))
rate = float(input("佣金率："))
print(f"{sales * rate:.2f}")

# 27
price = float(input("原价："))
discount = float(input("折扣："))
print(f"{price * discount:.2f}")

# 28
qty = int(input("数量："))
price = float(input("单价："))
print(f"{qty * price:.2f}")

# 29
n = int(input("请输入整数："))
print(n % 2)

# 30
a = int(input("第一个整数："))
b = int(input("第二个整数："))
print(max(a, b))

# 31
cost = 45
shipping = 8
price_usd = 19.99
rate = 7.2
commission = 0.15
revenue = price_usd * rate
profit = revenue * (1 - commission) - cost - shipping
print(f"{profit:.2f}")

# 32
print(f"{19.99:>8}")

# 33
print(f"{1234567:,}")

# 34
a = 100
b = 25
print(a - b)
print(a / b)

# 35
count = 3
total = 59.97
print(f"共 {count} 件，合计 {total:.2f} 元")

# 36
a = 10
b = 20
a, b = b, a
print(a, b)

# 37
print(17 // 5)
print(17 % 5)

# 38
days = int(input("天数："))
print(days * 86400)

# 39
a = float(input("第一个数："))
b = float(input("第二个数："))
c = float(input("第三个数："))
print(f"{(a + b + c) / 3:.1f}")

# 40
name = input("商品名：")
price = float(input("单价："))
qty = int(input("数量："))
print(f"{name} × {qty} 件，单价 {price:.2f}，合计 {price * qty:.2f}")
