# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop_name):
    return shop_name["name"]

def get_total_cash(cash_total):
    return cash_total["admin"]["total_cash"]

# function called add_or_remove_cash which has two parameters
# first is the pet shop, the second is 10
# cash should equal the pet shop total plus 10

def add_or_remove_cash(cash_total, extra):
    cash_total["admin"]["total_cash"]+=extra


def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

def increase_pets_sold(current_sold, just_sold):
    current_sold["admin"]["pets_sold"]+= just_sold

def get_stock_count(stock):
    return len(stock["pets"])

#I want to count all the British Shorthairds (dog_breed)
#create a list to add them to it and loop through


def get_pets_by_breed(pet_shop, dog_breed):
    list_of_dog_breed = []
    for breed in pet_shop["pets"]:
        if breed["breed"] == dog_breed:       
            list_of_dog_breed.append(dog_breed)
    return list_of_dog_breed

#the answer needs to be a key as "Arthur" = pet["name"]
# it needs to be pet_shop = ["pets"][3]

def find_pet_by_name(pet_shop, dog_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == dog_name:
            return pet

#a function to remove arthur from the list if it exists
#the above function

def remove_pet_by_name(pet_shop, dog_name):
    dog_dict = find_pet_by_name(pet_shop,dog_name)
    if dog_dict["name"] == dog_name:
        pet_shop["pets"].remove(dog_dict)
        
    # slower way of doing above:
    #  for pet in pet_shop["pets"]:
    #     if pet["name"] == dog_name:
    #         print(pet)
    #         pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(cust_cash):
    return cust_cash["cash"]

