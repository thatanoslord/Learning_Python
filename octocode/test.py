print("this program will show you the weather in these 3 cities")
city = input("choose one of these three cities: 'Cairo', 'Tanta' and 'Giza'")
if city.lower() == "cairo":
    print(f"the weather in {city} is warm and sunny")
elif city.lower() == "tanta":
    print(f"the weather in {city} is cold")
elif city.lower() == "giza":
    print(f"the weather in {city} is rainy")
else:
    print(f"the {city} you printed isn't in the list.")
    