# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

import random

# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

with open("Buildings_generated.txt", "a+") as f:
    f.truncate(0)

# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Land type
land_type_list = ["Residential","Commercial","Industrial","Agricultural","Government"]

# Residential
residential_building_choice = ["House","Flat","Apartment","Bungalow","Shack"]
residential_building_extra = ["Garage","Shed"]

# Commercial
commercial_building_choice = ["Store","Supermarket","Shopping Centre","Office","Warehouse","Hotel","Pub","Resturant","Cafe","Gym","Medical Centre","Hospital","Nursing Home","Hair Salon","Theme Park","Bank","Stall","Kennel","Vehicle Repair Garage","Florist"]
store_name = ["Gerald's","Larry's","Fabien's","Grace's","Donnie's","Alex's","Sam's","Luke's","David's","Smith's","Burn's","Ellie's","Sarah's","Max's","Bob's","Tinks'","Zoe's","Rose's","Walter's","Philips'","Jose's","Antonio's","Juan's","Manuel's","Maria's","Anna's","Daniel's","Danny's","Jack's","Isabel's","Laura's","Shannon's"]
store_type = ["Hardware","Clothing","Drug","Grocery","Charity","Electronic","DIY","2nd Hand","Book","Gardening","Jewelery","Music","Game","Bicycle","Sports"]
commercial_building_extra = ["Parking Lot"]

# Industrial
industrial_building_choice = ["Manufacturing Factory","Warehouse","Power Station","Construction Site","Brewery","Nuclear Power Plant"]
factory_type = ["Petroleum","Chemical","Plastic","Food","Clothing","Textile","Metal","Electronic","Vehicle","Wood","Paper","Cardboard","Ceramic","Glass"]
industrial_building_extra = ["Warehouse"]

# Agricultural
agricultural_building_choice = ["Farm","Forestry"]
agricultural_building_extra = ["Barn"]

# Government
government_building_choice = ["Post Office","Police Station","School","Airport"]
government_building_extra = ["Parking Lot"]

# Military
military_building_choice = ["Military Base"]
military_base_extra = ["Airfield"]
military_air_field = ["Hangar","Landling Pad", "Fuel Tank"]
military_air_facilities = ["Aircraft Repair & Maintenance"]
military_base_buildings = ["Barrack","Mess Hall","Office","Gym","Field","Facility","Hospital","Watch Tower","Bunker","Fuel Tank"]
military_base_building_default = ["Entrance Checkpoint"]
militrary_facilities = ["Ammunation Storage", "Weapon Storage","Military Intelligence","Vehicle Repair & Maintenance","Vehicle Storage","Weapon Repair & Maintenance"]

# Size
building_size = ["Small","Medium","Large"]

# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Used to store current counter of how many buildings have been generated
#current_building_counter = 1

# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

while True:
    
    while True:

        # / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        
        try:
            
            user_input = int(input("> Generated Buildings: ")) # Gets user input as an integer and stores it
            for i in range(user_input): # Generates specified number of buildings

                def save_data():
                    with open("Buildings_generated.txt", "a+") as f:
                        f.seek(0)
                        data = f.read(100)
                        if len(data) > 0:
                            f.write("\n")
                        f.write("\n")
                        if random_building_choice == "House":

                            if extras_enabled == True:

                                if building_condition_size == "Destroyed":

                                    if extra_condition_type == "Destroyed":
                                        f.write(building_generated_condition)
                        else:
                            f.write(building_generated)
                
                #print("Building Number:",current_building_counter) # Prints the current building number to screen
                #current_building_counter = current_building_counter + 1 # Adds +1 to the current_building_counter
                building_condition = random.randint(0,100) # Generates building Condition 0% - 100%
                extra_condition = random.randint(0,100) # Generates extra Condition 0% - 100%
                land_type = random.choice(land_type_list) # Generates Land Type
                building_size_small = 2 # Small buildings capped at 2 floors
                building_size_medium = random.randint(2,4) # Generates floors for medium buildings
                building_size_large = random.randint(3,5) # Generates floors for large buildings
                multiple_stories = True # Multiple floors?
                extras_enabled = True # Extras?
                extra_true_or_false = random.randint(1,4) # extra_true_or_false can be any number from 1 - 4
                building_counter = random.randint(4,16) # building_counter can be any number 4 - 16

                # / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

                # This is used to determine if a building is destroyed or not
                if building_condition <= 25:
                    building_condition_size = "Destroyed"
                else:
                    building_condition_size = random.choice(building_size)

                # This is used to determine if an extra is destroyed or not
                if extra_condition <= 25:
                    extra_condition_type = "Destroyed"
                else:
                    extra_condition_type = random.choice(building_size)

                # This is used to determine if extras_enabled is true or false
                if extra_true_or_false == 1:
                    extras_enabled = True
                else:
                    extras_enabled = False

                # / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

                land_type = "Residential"
                
                #Used to generate a residential building if land_type is Residential
                if land_type == "Residential":
                    
                    random_building_choice = random.choice(residential_building_choice)

                    random_building_choice = "House"
                    if random_building_choice == "House":

                        extras_enabled = True
                        if extras_enabled == True:
                                
                            random_build_extra = random.choice(residential_building_extra)

                            building_condition_size = "Destroyed"
                            if building_condition_size == "Destroyed":

                                if extra_condition_type == "Destroyed":
                                        
                                    building_generated = str(building_condition_size,random_building_choice,"with a",extra_condition_type,random_build_extra)
                                    building_generated_condition = strbuilding_condition_size,"Condition: "+str(building_condition)+"% )"
                                    save_data()
                                    
                                else:
                                    building_generated = building_condition_size,random_building_choice,"with a",extra_condition_type,random_build_extra
                                    save_data()
                                    
                #Used to generate a residential building if land_type is Commercial
                elif land_type == "Commercial":
                    random_building_choice = random.choice(commercial_building_choice)
                    building_generated = random_building_choice
                    save_data()

                #Used to generate a residential building if land_type is Industrial
                elif land_type == "Industrial":
                    random_building_choice = random.choice(industrial_building_choice)
                    building_generated = random_building_choice
                    save_data()

                #Used to generate a residential building if land_type is Agricultural
                elif land_type == "Agricultural":
                    random_building_choice = random.choice(agricultural_building_choice)
                    building_generated = random_building_choice
                    save_data()

                #Used to generate a residential building if land_type is Government
                elif land_type == "Government":
                    random_building_choice = random.choice(government_building_choice)
                    building_generated = random_building_choice
                    save_data()

                #Used to generate a residential building if land_type is Military
                elif land_type == "Military":
                    random_building_choice = random.choice(military_building_choice)
                    building_generated = random_building_choice
                    save_data()

                # / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

        # If user_input isn't an integer then
        except ValueError:
          print("> Please input an integer.")  

        # / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        
    print("/ | END | \ ")

print("/ | END | \ ")

























    
