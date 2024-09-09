india = ["Delhi", "Bangalore", "Mumbai", "Delhi"]
USA = ["New York", "Chicago", "Las vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]

country = input("enter a city name:")

if country in india:
    print(f"{country} is an indian city  ")
elif country in USA:
    print(f"{country} is in USA")
elif country in UK:
    print(f"{country} is in UK")
else:
    print("country is not listed")
