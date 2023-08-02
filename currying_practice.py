def discount_price(discount):

    price = 100
    
    def sale(new_price):
        price = new_price - (new_price * discount)
        return price
    
    return sale

# cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
# cost_05 = discount_price(0.05)  

# price = 10
print(discount_price(0.15)(10)) # 85.0
print(discount_price(0.15))
print(cost_10(200))
print(cost_10)
# print(cost_10(price)) # 90.0
# print(cost_05(price)) # 95.0