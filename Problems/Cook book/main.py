pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

ingredient = input()
lista = [pasta, apple_pie, ratatouille, chocolate_cake, omelette]
list_str = {pasta: "pasta", apple_pie: "apple pie", ratatouille: "ratatouille", chocolate_cake: "chocolate cake",
            omelette: "omelette"}
num = 0
for food in lista:
    if ingredient in food:
        dish = list_str[food]
        print(dish, "time!")
