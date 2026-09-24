# Read and validate the order total

order_price_total_valid = True

raw = input("Enter order price total: ")

try:
    order_price_total = float(raw)
except ValueError:
    print("Invalid order total. Please enter a number.")
    order_price_total_valid = False

if order_price_total_valid:
    if order_price_total < 0:
        print("Invalid order total. Please enter $0 or more.")
        order_price_total_valid = False

   
# Read and validate the delivery day

day_valid = True

day = input("Enter the delivery day (all the letters lowercase): ")
if not (day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday" or day == "saturday" or day == "sunday"):
    print("Invalid delivery day. Please enter a day from Monday to Sunday.")
    day_valid = False

# Combine the two values

if order_price_total_valid and day_valid:

    if order_price_total < 50 and (day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday"):
        delivery_fee = 10
  
    elif order_price_total < 50 and (day == "saturday" or day == "sunday"):
        delivery_fee = 20

    elif order_price_total >= 50 and (day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday"):
        delivery_fee = 5

    else:
        delivery_fee = 0

# Display the result

    print(f"Order price total: ${order_price_total:.1f}")
    print(f"Delivery day: {day}")
    print(f"Delivery fee: ${delivery_fee:.1f}")
   

