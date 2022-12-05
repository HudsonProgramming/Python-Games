import pickle
import os
os.system("clr")

# List
fruit_basket = ["Apple","Pear","Kiwi","Banana","Strawberry"]

# Prints The List
print("Fruit Basket:")
print(fruit_basket)

# Saves The List
pickle.dump(fruit_basket,open("Fruit_Basket.dat","wb"))

# Removes "Kiwi" From List
fruit_basket.remove("Kiwi")

# Prints The List
print("Fruit Basket:")
print(fruit_basket)

# Loads The Saved Data
fruit_basket = pickle.load(open("Fruit_Basket.dat","rb"))

# Prints The List
print("Fruit Basket:")
print(fruit_basket)
