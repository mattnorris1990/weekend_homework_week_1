# WRITE YOUR FUNCTIONS HERE

# test at line 78
def get_pet_shop_name(name):
    return name["name"]

# test at line 82
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# test at line 87 & line 93
def add_or_remove_cash(pet_shop, amount):
    current_cash = pet_shop["admin"]["total_cash"]
    revised_cash = current_cash + amount
    pet_shop["admin"]["total_cash"] = revised_cash

# test at line 99
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# test at line 104
def increase_pets_sold(pet_shop, amount):
    current_pets_sold = pet_shop["admin"]["pets_sold"]
    revised_pets_sold = current_pets_sold + amount
    pet_shop["admin"]["pets_sold"] = revised_pets_sold

# test at line 110
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# test at line 115 + line 120
def get_pets_by_breed(pet_shop, breed):
    list_of_pets = []
    pets = pet_shop["pets"]

    for pet in pets :
        if pet["breed"] == breed:
            list_of_pets.append(pet)
    return list_of_pets


# test at line 125 & line 130
def find_pet_by_name(pet_shop, name):
    pets = pet_shop["pets"]

    for pet in pets:
        if name == pet["name"]:
            return pet

    # my original solution
    # list_of_pets = []
    # pets = pet_shop["pets"]

    # for pet in pets :
    #     if pet["name"] == name:
    #         list_of_pets.append(pet)
    #         return list_of_pets[0]

    
# test at line 135
def remove_pet_by_name(pet_shop, name):
    pets = pet_shop["pets"]

    for pet in pets :
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)

#  test at 141
def add_pet_to_stock(pet_shop, new_pet):
    pets = pet_shop["pets"]

    pets.append(new_pet)

# test at 147
def get_customer_cash(customer):
    customer_cash = 0 + customer["cash"]
    return customer_cash

#  test at 152
def remove_customer_cash(customer, amount):
    current_cash = customer["cash"]
    revised_cash = current_cash - amount
    customer["cash"] = revised_cash

# test at 158 
def get_customer_pet_count(customers):
    return len(customers["pets"])

# test at 164
def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)
    return len(customer["pets"])

# test at 172, test at 178, test at 184

def customer_can_afford_pet(customer, pet):
    can_buy = None

    if customer["cash"] >= pet["price"]:
        can_buy = True
    else:
        can_buy = False
    return can_buy

def sell_pet_to_customer(pet_shop, pet, customer):
    
    for pets in pet_shop["pets"]:
        if pets == pet:

            pet_cost = pet["price"]
            if customer_can_afford_pet(customer, pet) == True:
            
                add_pet_to_customer(customer, pet)
                increase_pets_sold(pet_shop, 1)
                remove_customer_cash(customer, pet_cost)
                add_or_remove_cash(pet_shop, pet_cost)



        


    









        
    

             
    


