'Print the dish name using IF ELIF OR ELSE'

indian = ["samosa", "daal", "naan"]
chinese = ["egg roll", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]

dish = input ("enter a dish  name")

if dish in indian:
    print(f"{dish} in indian")
elif dish in chinese:
    print(f"{dish} in chinese")
elif dish in italian:
    print(f"{dish} in italian")
else:
    print("i don't know which cuisine is this!")


