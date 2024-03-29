#Erik's Groceries Project

import operator


# groceries.py

#from pprint import pprint

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output




def prod_name(product):
    return product['name']

def prod_dept(product):
    return product['department']

def prod_aisle(product):
    return product['aisle']

def prod_price(product):
    return product['price']

products2 = sorted(products, key=prod_name)
#print("test")
#print(products2[0]['name'], products2[0]['price'])

prod_count = 0
total_products = len(products)

print("")
print("---------------------")
#print("There are " + str(total_products) + " Products")
print(f"There are {total_products} Products")
print("---------------------")
print("")


while prod_count < total_products:    #put in a variable here later that counts the number of products
    print(f"   + {products2[prod_count]['name']} (${products2[prod_count]['price']})")
       
    prod_count = prod_count + 1

print("")
print("")





#def team_name(team):
#    return team["name"]

#sorted(products, key = operator.itemgetter('name'))
# USERING OPERATOR ITEM GETTING
#print(products[0]['name'])

#Other way of doing it

# for item in products:  (or for i in products)
    # print(item)
    # print(item['name])




#prod_count = 0

#listing the departments - to be completed




#while prod_count < total_products:    #put in a variable here later that counts the number of products
#    print(f"   + {products2[prod_count]['name']} (${products2[prod_count]['price']})")
#       
#    prod_count = prod_count + 1
#
#print("")
#print("")

dept_list = []
for i in products:
    if i['department'] not in dept_list:
        dept_list.append(i["department"])

numdepts = len(dept_list)

print("")
print("---------------------")

print(f"There are {numdepts} Departments")
print("---------------------")
print("")

sort_dept = sorted(dept_list)

#FROM SCREENCAST

for d in sort_dept:
   matching_products = [p for p in products if p["department"] == d]
   matching_products_count = len(matching_products)
   if matching_products_count > 1:
       label = "products"
   else:
       label = "product"
   print(" +++ " + d.title() + " (" + str(matching_products_count) + " " + label + ")")
print("")
