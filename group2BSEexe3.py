'''#This is the part for the residential
customer_code = input("Enter customer code: ")
beginning_meter_reading = int(input("Enter beginning meter reading: "))
ending_meter_reading = int(input("Enter ending meter reading:    "))
print("")

print("Customer code: ", customer_code)
print("Beginning meter reading: ", beginning_meter_reading)
print("Ending meter reading:    ", ending_meter_reading)
Gallons_of_water_used = (ending_meter_reading-beginning_meter_reading)*0.1
print("Gallons of water used: ", round(Gallons_of_water_used,1))
if customer_code == 'r':
   first_amount = 5.00
   second_amount = 0.0005*Gallons_of_water_used
   amount = first_amount+second_amount
#elif customer_code == 'c':
  #  first_amount = 1000.00
   # second_amount = 0.00025*Gallons_of_water_used
   # amount = first_amount+second_amount
# This is the part for the commercial part c
print("Amount billed:", round(amount,2))
print("")
customer_code1 = input("Enter customer code: ")
beginning_meter_reading1 = int(input("Enter beginning meter reading: "))
ending_meter_reading1 = int(input("Enter ending meter reading:    "))
print("")
print("Customer code: ", customer_code1)
print("Beginning meter reading: ", beginning_meter_reading1)
print("Ending meter reading:    ", ending_meter_reading1)
beginning_meter_reading1 = 1000000000-beginning_meter_reading1
ending_meter_reading1 = ending_meter_reading1
Gallons_of_water_used = (ending_meter_reading1+beginning_meter_reading1)*0.1
if Gallons_of_water_used <=4000000:
    print("Gallons of water used: ", round(Gallons_of_water_used,1))
else: print('error')

if customer_code1 == 'c':
    first_amount1 = 1000.00
    second_amount1 = 0.00025*Gallons_of_water_used
    amount1 = first_amount1+second_amount1
    print("Amount billed:", round(amount1,2))
print("\n")
# This is the section for the industrial part i
print("Amount billed:", round(amount,2))
print("")
customer_code1 = input("Enter customer code: ")
beginning_meter_reading1 = int(input("Enter beginning meter reading: "))
ending_meter_reading1 = int(input("Enter ending meter reading:    "))
print("")
print("Customer code: ", customer_code1)
print("Beginning meter reading: ", beginning_meter_reading1)
print("Ending meter reading:    ", ending_meter_reading1)
beginning_meter_reading1 = 1000000000-beginning_meter_reading1
ending_meter_reading1 = ending_meter_reading1
Gallons_of_water_used = (ending_meter_reading1+beginning_meter_reading1)*0.1
if Gallons_of_water_used <=4000000:
    print("Gallons of water used: ", round(Gallons_of_water_used,1))
else: print('error')

if customer_code1 == 'c':
    first_amount1 = 1000.00
    second_amount1 = 0.00025*Gallons_of_water_used
    amount1 = first_amount1+second_amount1
    print("Amount billed:", round(amount1,2))
print("\n")
customer_code1 = input("Enter customer code: ")
beginning_meter_reading1 = int(input("Enter beginning meter reading: "))
ending_meter_reading1 = int(input("Enter ending meter reading:    "))
print("")
print("Customer code: ", customer_code1)
print("Beginning meter reading: ", beginning_meter_reading1)
print("Ending meter reading:    ", ending_meter_reading1)
beginning_meter_reading1 = 1000000000-beginning_meter_reading1
ending_meter_reading1 = ending_meter_reading1
Gallons_of_water_used1 = (ending_meter_reading1+beginning_meter_reading1)*0.1
if Gallons_of_water_used1 <=4000000:
    print("Gallons of water used: ", round(Gallons_of_water_used1,1))
else: print('error')

if customer_code1 == 'c':
    first_amount1 = 1000.00
    second_amount1 = 0.00025*Gallons_of_water_used1
    amount1 = first_amount1+second_amount1
    print("Amount billed:", round(amount1,2))
print("\n") '''
# This is the section for the industrial part i
print("")
customer_code2 = input("Enter customer code: ")
beginning_meter_reading2 = int(input("Enter beginning meter reading: "))
ending_meter_reading2 = int(input("Enter ending meter reading:    "))
print("")
print("Customer code: ", customer_code2)
print("Beginning meter reading: ", beginning_meter_reading2)
print("Ending meter reading:    ", ending_meter_reading2)
Gallons_of_water_used2 = (ending_meter_reading2 - beginning_meter_reading2)*0.1
if customer_code2 == 'i':
 if Gallons_of_water_used2 <= 4000000:
    print("Gallons of water used: ", round(Gallons_of_water_used2,1))
    first_amount2 = 1000.00
    second_amount2 = 0.00025*Gallons_of_water_used2
    amount2 = first_amount2+second_amount2
    print("Amount billed:", round(amount2,2))
elif Gallons_of_water_used2 > 4000000 & Gallons_of_water_used2 <= 10000000 :
    amount2 = 2000.00
    print("Amount billed: ",amount2)
else:
    first_amount2 = 2000.00
    second_amount2 = 0.00025*Gallons_of_water_used2
    amount2 = first_amount2+second_amount2
print("Amount billed", amount2)




