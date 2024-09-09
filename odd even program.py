
height = int(input("Enter Height:"))
weight = int(input("Enter Weight:"))

BMI = weight/(height)**2

if BMI > 30  :
    print("obesity")
elif BMI > 25 and BMI < 29:
    print("overweight")
elif BMI >18.5 and BMI < 25:
    print("normal")
elif BMI < 18.5:
    print("underweight")