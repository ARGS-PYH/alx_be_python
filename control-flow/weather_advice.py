weather = input("What's the weather like today? (sunny/rainy/cold): ")
if weather.lower() == "sunny":
    print(f"Wear a t-shirt and sunglasses.")
elif weather.lower() == "rainy":
    print(f"Don't forget your umbrella and a raincoat.")
elif weather.lower() == "cold":
    print(f"Make sure to wear a warm coat and a scarf.")
else:
    print(f"Sorry, I don't have recommendations for this weather.")