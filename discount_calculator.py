def  calculate_discount(price, discount_percent):
    if( discount_percent >= 20):
        return price - (price * discount_percent/100 )
    else:
        return price
    
pri = int(input("Enter the price: "))
percent = float(input("Enter the discount: "))

print("Final price",calculate_discount(pri, percent))