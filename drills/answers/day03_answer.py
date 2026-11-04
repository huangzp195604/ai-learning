# -*- coding: utf-8 -*-
"""
P2 · 列表 list（33 题）参考答案
写完 33 题后才许打开这个文件
"""

# ---------- 1 ----------
skus = ["A001", "A002", "A003"]
print(skus)

# ---------- 2 ----------
print(len(skus))

# ---------- 3 ----------
print(skus[0])

# ---------- 4 ----------
print(skus[-1])

# ---------- 5 ----------
print(skus[1])

# ---------- 6 ----------
print(skus[:2])

# ---------- 7 ----------
print(skus[-2:])

# ---------- 8 ----------
print(skus[1:3])

# ---------- 9 ----------
skus = ["A001", "A002", "A003"]
skus.append("A004")
print(skus)

# ---------- 10 ----------
skus = ["A001", "A002", "A003"]
skus[0] = "A000"
print(skus)

# ---------- 11 ----------
skus = ["A001", "A002", "A003"]
skus.insert(1, "A999")
print(skus)

# ---------- 12 ----------
skus = ["A001", "A002", "A003"]
skus.remove("A002")
print(skus)

# ---------- 13 ----------
skus = ["A001", "A002", "A003"]
last = skus.pop()
print(last)

# ---------- 14 ----------
a = ["A001", "A002"]
b = ["B001", "B002"]
print(a + b)

# ---------- 15 ----------
skus = ["A001", "A002", "A003"]
for s in skus:
    print(s)

# ---------- 16 ----------
print("A002" in skus)

# ---------- 17 ----------
print("B001" in skus)

# ---------- 18 ----------
for i, s in enumerate(skus, start=1):
    print(i, s)

# ---------- 19 ----------
prices = [19.99, 45.0, 12.5, 30.0]
print(sum(prices))

# ---------- 20 ----------
print(max(prices))

# ---------- 21 ----------
print(min(prices))

# ---------- 22 ----------
print(f"{sum(prices) / len(prices):.2f}")

# ---------- 23 ----------
sales = [100, 200, 100, 300]
print(sales.count(100))

# ---------- 24 ----------
skus = ["A001", "A002", "A003"]
print(skus.index("A002"))

# ---------- 25 ----------
prices = [19.99, 45.0, 12.5, 30.0]
print(sorted(prices, reverse=True))

# ---------- 26 ----------
high = []
for p in prices:
    if p > 20:
        high.append(p)
print(high)

# ---------- 27 ----------
count = 0
for p in prices:
    if p > 20:
        count = count + 1
print(count)

# ---------- 28 ----------
nums = [1, 2, 3]
for i in range(len(nums)):
    nums[i] = nums[i] * 2
print(nums)

# ---------- 29 ----------
skus = ["A001", "A002", "A003"]
print("-".join(skus))

# ---------- 30 ----------
s = "A001,A002,A003"
print(s.split(","))

# ---------- 31 ----------
stocks = [120, 35, 80, 12, 55]
for s in stocks:
    if s < 50:
        print(f"{s} 该补货")
    else:
        print(f"{s} 充足")

# ---------- 32 ----------
prices = [19.99, 45.0, 12.5, 30.0]
print([p * 2 for p in prices])

# ---------- 33 ----------
a = [1, 2, 3]
b = a[:]
b[0] = 99
print(a)
print(b)
