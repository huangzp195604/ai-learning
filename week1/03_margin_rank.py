# -*- coding: utf-8 -*-
"""10 个在卖 SKU 的利润率排名
决策口径：利润率 > 40% 加大投放；< 20% 且单件利润 < 60 清仓；其余维持
"""

RATE = 7.2          # 汇率
COMMISSION = 0.15   # 平台佣金率

BOOST_MARGIN = 40   # 利润率高于此值 → 加大投放
CLEAR_MARGIN = 20   # 利润率低于此值 且 利润额也低 → 清仓
CLEAR_PROFIT = 60

# 列表套字典：有序、方便排序；02 用的是字典套字典，那种靠 key 取值，排序要 .values()
products = [
    {"sku": "hzp20260725", "name": "女士卫裤",     "price_usd": 19.99, "cost": 45.0,  "shipping": 8.0},
    {"sku": "hzp20260812", "name": "女士运动鞋",   "price_usd": 32.99, "cost": 118.0, "shipping": 25.0},
    {"sku": "hzp20260802", "name": "男士风衣",     "price_usd": 45.99, "cost": 160.0, "shipping": 30.0},
    {"sku": "hzp20260901", "name": "男士卫衣",     "price_usd": 24.99, "cost": 62.0,  "shipping": 12.0},
    {"sku": "hzp20260625", "name": "男士皮鞋",     "price_usd": 38.99, "cost": 135.0, "shipping": 22.0},
    {"sku": "hzp20261005", "name": "女士针织开衫", "price_usd": 21.99, "cost": 38.0,  "shipping": 9.0},
    {"sku": "hzp20261118", "name": "儿童羽绒服",   "price_usd": 42.99, "cost": 175.0, "shipping": 35.0},
    {"sku": "hzp20260708", "name": "女士打底裤",   "price_usd": 12.99, "cost": 18.0,  "shipping": 6.0},
    {"sku": "hzp20260520", "name": "男士休闲短裤", "price_usd": 16.99, "cost": 40.0,  "shipping": 8.0},
    {"sku": "hzp20260915", "name": "女士牛仔外套", "price_usd": 36.99, "cost": 96.0,  "shipping": 18.0},
]


def calc_margin(p):
    """算单个 SKU 的销售额 / 单件利润 / 利润率（%）"""
    revenue = p["price_usd"] * RATE
    profit = revenue * (1 - COMMISSION) - p["cost"] - p["shipping"]
    margin = profit / revenue * 100
    return revenue, profit, margin


# 1. 遍历算利润率，结果写回每个字典
for p in products:
    p["revenue"], p["profit"], p["margin"] = calc_margin(p)

# 2. sorted() 返回排好序的新列表，不动原列表；key 告诉它按什么排
ranked = sorted(products, key=lambda x: x["margin"], reverse=True)

# 3. 输出完整排名
print("=" * 74)
print("SKU 利润率排行榜")
print("=" * 74)
print(f"{'排名':<4}{'SKU':<12}{'品名':<14}{'售价$':>8}{'销售额¥':>10}{'单件利润¥':>11}{'利润率':>9}")
print("-" * 74)

for i, p in enumerate(ranked, start=1):
    print(f"第{i:<3}{p['sku']:<12}{p['name']:<14}{p['price_usd']:>8.2f}"
          f"{p['revenue']:>10.2f}{p['profit']:>11.2f}{p['margin']:>8.1f}%")

print("-" * 74)
avg = sum(p["margin"] for p in ranked) / len(ranked)
print(f"共 {len(ranked)} 个 SKU，平均利润率 {avg:.1f}%")

# 4. 双条件判断：效率低 + 赚得少，两个都占才砍
# TODO: 加大投放 6 个偏多（占 60%），等于没策略。后续应按利润额或「利润率 × 利润额」综合分排序取前 3
for p in ranked:
    if p["margin"] < CLEAR_MARGIN and p["profit"] < CLEAR_PROFIT:
        p["decision"] = "清仓"
    elif p["margin"] > BOOST_MARGIN:
        p["decision"] = "加大投放"
    else:
        p["decision"] = "维持"

print()
print("=" * 74)
print("【决策建议】")
print("=" * 74)

for label in ["加大投放", "维持", "清仓"]:
    group = [p for p in ranked if p["decision"] == label]
    print(f"▶ {label}（{len(group)} 个）：")
    if not group:
        print("   （无）")
    for p in group:
        print(f"   {p['sku']} {p['name']}：利润率 {p['margin']:.1f}%，单件利润 ¥{p['profit']:.2f}")

# 5. 换个口径看看：按「单件利润额」排序
by_profit = sorted(products, key=lambda x: x["profit"], reverse=True)
print()
print("=" * 74)
print("【对比】按单件利润额排序 TOP 3（不是按利润率）")
print("=" * 74)
for i, p in enumerate(by_profit[:3], start=1):
    print(f"   {i}. {p['sku']} {p['name']}：单件利润 ¥{p['profit']:.2f}，利润率 {p['margin']:.1f}%")
