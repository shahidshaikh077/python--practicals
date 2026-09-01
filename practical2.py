rice_price = 60
sugar_price = 45
salt_price = 20
oil_price = 150


rice_qty = float(input("Enter Rice Quantity (kg): "))
sugar_qty = float(input("Enter Sugar Quantity (kg): "))
salt_qty = float(input("Enter Salt Quantity (kg): "))
oil_qty = float(input("Enter Oil Quantity (liters): "))


rice_total = rice_qty * rice_price
sugar_total = sugar_qty * sugar_price
salt_total = salt_qty * salt_price
oil_total = oil_qty * oil_price

print("\n************* Bill Detail *************")
print("Rice:", rice_total)
print("Sugar:", sugar_total)
print("Salt:", salt_total)
print("Oil:", oil_total)


Total_Bill = rice_total + sugar_total + salt_total + oil_total
print("Total Bill:", Total_Bill)

print("=========== Final Discount ============")
Discount = 0

if Total_Bill >= 2000:
    Discount = Total_Bill * 0.10
elif Total_Bill >= 1000:
    Discount = Total_Bill * 0.05
else:
    print("No Discount")

if Discount > 0:
    print("Discount:", Discount)

print("=========== Final Bill ============")
Final_Bill = Total_Bill - Discount
print("Final Bill:", Final_Bill)