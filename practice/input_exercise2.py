name = input("商品名称：")
price = float(input("单价:"))
weight = float(input("重量："))
amount = 0.00
amount = price * weight
print("%s单价%.2f元/斤，购买了%.2f斤，需要支付%.2f元" % (name, price, weight, amount))
