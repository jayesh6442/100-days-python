total_bill = float(input("Enter the Totol bill: "))
tip_percentage = int(input("Enter the tip in percentage 12 15 20: "))
while tip_percentage not in [12,15,10]:
    tip_percentage = int(input("Enter the tip in  12% 15% 20%: "))
tip_amount =  total_bill * (tip_percentage / 100)
final_bill = total_bill + tip_percentage
print("Final bill is ",final_bill)
person = int(input("Enter How many people will divide the bill: "))
per_person = final_bill/person
final_round = round(per_person,2)
print("Each person should pay: ", final_round);