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
        #else:
         #   dog_name = None

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

#below could be DRYer
def remove_customer_cash(cust_cash, amount):
    if get_customer_cash(cust_cash) >= amount:
        cust_cash["cash"] -= amount 
    
    # if cust_cash["cash"]>= amount:
    #     cust_cash["cash"] -= amount

def get_customer_pet_count(cust_pet_amount):
    return len(cust_pet_amount["pets"])

def add_pet_to_customer(cust, new_pet):
    cust["pets"].append(new_pet)

def customer_can_afford_pet(cust, new_pet):
    if get_customer_cash(cust) >= new_pet["price"]:
        return True
    else:
        return False

#need to add 1 to cust pet count
#need to add 1 to pets sold
#need to remove cost of pet from cust cash
#need to add cash to pet shop account

def sell_pet_to_customer(pet_shop, new_pet, cust):
    if new_pet == None or cust["cash"] < new_pet["price"] or new_pet in cust["pets"]:
        return None
    else:
        cust["pets"].append(new_pet)
        increase_pets_sold(pet_shop, 1)
        cust["cash"]-= new_pet["price"]
        pet_shop["admin"]["total_cash"]+= new_pet["price"]

# for second last question, I need to make it not run the else statement
# this is due to "Dave" the pet not existing
# try and get it to skip if         