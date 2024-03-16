height =  float(input("Enter the height in meters: "))
weight =  float(input("Enter the weight in kg: "))

bmi  =  weight / (height **2);

final_bmi = round(bmi,2)
print(f"Your BMI is {final_bmi}")