cost=45.0
shopping=8.0
price=19.99
rate=7.2
commission=0.15
revenue=price*rate
profit=revenue*(1-commission)-cost-shopping
profit_margin=profit/revenue*100
print(f"单件利润:{profit:.2f}元")
print(f"利润率:{profit_margin:.1f}%")
if profit_margin<20:
    print("不建议上架")