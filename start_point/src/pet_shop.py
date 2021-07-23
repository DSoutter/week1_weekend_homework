# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop_name):
    return shop_name["name"]

def get_total_cash(cash_total):
    return cash_total["admin"]["total_cash"]

# function called add_or_remove_cash which has two parameters
# first is the pet shop, the second is 10
# cash should equal the pet shop total plus 10

def add_or_remove_cash(cash_total, extra):
    if extra >= 0:
        cash_total["admin"]["total_cash"]+=extra
    else:
        cash_total["admin"]["total_cash"]-=extra