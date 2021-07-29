# WAPP to demonstrate Nesting of Lists & Dictionaries

facebook = { 'username': 'Jack123', 'password': '123'}
twitter = {'username': 'Jack456', 'password': '456'}
social_media = [facebook, twitter]
print(social_media)

pizza = {
       'crust': 'thick',
       'toppings': ['mushrooms', 'extra cheese']
}
print(pizza)
print(pizza['toppings'])
