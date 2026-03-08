distance = int(input("How far are you travelling?"))
mileage = int(input("What is our car mileage?"))
petrol_price = int(input("How much does petrol cost per litre"))
litres_needed = (distance)/(mileage)
total = (litres_needed)*(mileage)
print(f"""
DETAILS
Distance: {distance}
Mileage: {mileage}
Fuel Needed: {litres_needed}
Total Cost: {total}
""")