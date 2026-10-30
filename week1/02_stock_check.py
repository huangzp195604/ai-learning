# -*- coding: utf-8 -*-
"""判断哪些 SKU 库存低于安全线
安全线 = 日均销量 × 补货周期天数
输出：还能撑几天 / 补货清单 / 紧急程度
"""

skus = {
    "SKU-A001": {"name": "女士卫裤hzp20260725",   "stock": 120, "daily_sales": 15, "lead_time": 7},
    "SKU-A002": {"name": "女士运动鞋hzp20260812", "stock": 40,  "daily_sales": 12, "lead_time": 7},
    "SKU-B001": {"name": "男士风衣hzp20260802",   "stock": 500, "daily_sales": 30, "lead_time": 10},
    "SKU-B002": {"name": "男士卫衣hzp20260901",   "stock": 60,  "daily_sales": 25, "lead_time": 5},
    "SKU-C001": {"name": "男士皮鞋hzp20260625",   "stock": 200, "daily_sales": 8,  "lead_time": 14},
}

low_count = 0        # 低于安全线的 SKU 数量
restock_list = []    # 收集需要补货的 SKU，供第二轮遍历使用

print("=" * 72)
print("【第一轮】逐个检查")
print("=" * 72)

for sku_id, info in skus.items():
    stock = info["stock"]
    daily_sales = info["daily_sales"]
    lead_time = info["lead_time"]

    safety_line = daily_sales * lead_time                                  # 安全线
    days_left = stock // daily_sales if daily_sales > 0 else float("inf")     # 还能撑几天（整除）

    if stock < safety_line:
        low_count += 1
        gap = safety_line - stock                                          # 缺口
        level = "紧急" if gap * 2 > safety_line else "关注"                   # 缺口超过安全线一半 → 紧急
        restock_list.append({
            "sku_id": sku_id, "name": info["name"], "stock": stock,
            "safety_line": safety_line, "gap": gap,
            "days_left": days_left, "lead_time": lead_time, "level": level,
        })
        status = "该补货了"
    else:
        status = "库存充足"

    d = "∞" if days_left == float("inf") else days_left
    print(f"{sku_id} {info['name']:<20} 库存{stock:>4} | 安全线{safety_line:>4} "
          f"| 还能撑 {d:>3} 天 | {status}")

print("-" * 72)
print(f"共检查 {len(skus)} 个 SKU，其中 {low_count} 个低于安全线。")

# 第二轮遍历：只处理需要补货的 SKU
print()
print("=" * 72)
print("【第二轮】补货清单")
print("=" * 72)

if low_count == 0:
    print("全部 SKU 库存充足，无需补货。")
else:
    restock_list.sort(key=lambda x: x["gap"], reverse=True)  # 按缺口从大到小，最紧急的排最前
    for item in restock_list:
        d = "∞" if item["days_left"] == float("inf") else item["days_left"]
        print(f"[{item['level']}] {item['sku_id']} {item['name']}："
              f"缺口 {item['gap']}，还能撑 {d} 天，补货周期 {item['lead_time']} 天")
    print("-" * 72)
    print(f"合计 {low_count} 个 SKU 需要补货。")
