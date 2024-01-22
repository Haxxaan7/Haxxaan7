def calculate_electricity_bill(units):
    if units <= 100:
        rate = 10
    elif units <= 200:
        rate = 20
    elif units <= 300:
        rate = 30
    else:
        rate = 40

    bill_amount = units * rate
    gst = 0.2 * bill_amount  # GST is 20% of the bill amount

    total_bill = bill_amount + gst

    return total_bill

# Example: Calculate bill for 150 units
units_consumed = 150
electricity_bill = calculate_electricity_bill(units_consumed)

print(f"Electricity Bill: Rs. {electricity_bill:.2f}")
