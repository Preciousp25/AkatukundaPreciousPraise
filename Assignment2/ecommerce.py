#  E-COMMERCE SYSTEM

print("=" * 45)
print("       WELCOME TO SHOPEASE E-COMMERCE")
print("=" * 45)

#  LOGIN SYSTEM

attempts = 0
role = None

while attempts < 3:
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    if username == "admin" and password == "admin123":
        role = "Admin"
    elif username == "customer" and password == "cust123":
        role = "Customer"
    elif username == "cashier" and password == "cash123":
        role = "Cashier"
    else:
        attempts += 1
        remaining = 3 - attempts
        print(f"Invalid login! {remaining} attempt(s) remaining.")
        continue  

    break  

if role is None:
    print("\nToo many failed attempts. Access denied.")
    exit()

print(f"\nLogin successful! Welcome, {role}.")

#  ACCESS LEVEL CHECK
if role == "Admin":
    print("Access: Full access to all features.")
elif role == "Cashier":
    print("Access: Can process payments and view orders.")
elif role == "Customer":
    print("Access: Can shop and view own orders.")


#  PRODUCT SUBTOTAL INPUT
print("\n--- PRODUCT DETAILS ---")

while True:
    try:
        subtotal = float(input("Enter product subtotal: "))
        if subtotal <= 0:
            print("Subtotal must be greater than 0. Try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

#  AUTOMATIC DISCOUNT
auto_discount = 0   

if subtotal >= 500:
    auto_discount = subtotal * 0.15
    print("Auto discount: 15% applied (subtotal >= 500)")
elif subtotal >= 200:
    auto_discount = subtotal * 0.10
    print("Auto discount: 10% applied (subtotal >= 200)")
elif subtotal >= 100:
    auto_discount = subtotal * 0.05
    print("Auto discount: 5% applied (subtotal >= 100)")
else:
    auto_discount = 0
    print("No automatic discount (subtotal below 100)")

#  COUPON CODE
coupon = input("Enter coupon code (or press Enter to skip): ").strip().upper()
coupon_discount = 0   

if coupon == "SAVE10":
    if subtotal >= 100:
        coupon_discount = subtotal * 0.10
        print("Coupon SAVE10: 10% coupon discount applied")
    else:
        coupon_discount = 0
        print("Subtotal too low for SAVE10 (minimum: 100)")

elif coupon == "SAVE20":
    if subtotal >= 200:
        coupon_discount = subtotal * 0.20
        print("Coupon SAVE20: 20% coupon discount applied")
    else:
        coupon_discount = 0
        print("Subtotal too low for SAVE20 (minimum: 200)")

elif coupon == "SAVE30":
    if subtotal >= 300:
        coupon_discount = subtotal * 0.30
        print("Coupon SAVE30: 30% coupon discount applied")
    else:
        coupon_discount = 0
        print("Subtotal too low for SAVE30 (minimum: 300)")

elif coupon == "":
    coupon_discount = 0
    print("No coupon entered.")

else:
    coupon_discount = 0
    print(f"Invalid coupon code: '{coupon}'")


#  FINAL DISCOUNT
if coupon_discount > auto_discount:
    discount = coupon_discount
    discount_source = "Coupon"
elif auto_discount > 0:
    discount = auto_discount
    discount_source = "Automatic"
else:
    discount = 0
    discount_source = "None"

amount_after_discount = subtotal - discount

# TAX CALCULATION
print("\nLocations available: Uganda, Kenya, Tanzania")
location = input("Enter your location: ").strip().capitalize()

if location == "Uganda":
    tax_rate = 0.18
elif location == "Kenya":
    tax_rate = 0.16
elif location == "Tanzania":
    tax_rate = 0.15
else:
    tax_rate = 0.10
    print(f"Unknown location '{location}'. Default tax rate 10% applied.")

tax = amount_after_discount * tax_rate
final_price = amount_after_discount + tax

#  RECEIPT

print("\n" + "=" * 40)
print("            ORDER RECEIPT")
print("=" * 40)
print(f"  User Role      : {role}")
print(f"  Location       : {location}")
print("-" * 40)
print(f"  Subtotal       : {subtotal:.2f}")
print(f"  Discount ({discount_source}): {discount:.2f}")
print(f"  After Discount : {amount_after_discount:.2f}")
print(f"  Tax ({tax_rate*100:.0f}%)        : {tax:.2f}")
print("-" * 40)
print(f"  FINAL PRICE    : {final_price:.2f}")
print("=" * 40)


# PURCHASE MESSAGE
if final_price >= 500:
    print("Premium order! Thank you for your big purchase.")
elif final_price >= 200:
    print("Great order! Thank you for shopping with us.")
elif final_price >= 100:
    print("Good purchase! Come back for more deals.")
else:
    print("Thank you for your purchase!")

print("\n--- END OF TRANSACTION ---")