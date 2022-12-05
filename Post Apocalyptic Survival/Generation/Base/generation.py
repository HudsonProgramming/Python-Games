import random

##### LAND TYPE #####
land_type = ["Residential","Commercial","Industrial","Agricultural","Government"]

##### RESIDENTIAL #####
residential_building_choice = ["House","Flat","Apartment","Bungalow","Shack"]
residential_building_extra = ["Garage","Shed"]

##### COMMERCIAL #####
commercial_building_choice = ["Store","Supermarket","Shopping Centre","Office","Warehouse","Hotel","Pub","Resturant","Cafe","Gym","Medical Centre","Hospital","Nursing Home","Hair Salon","Theme Park","Bank","Stall","Kennel","Vehicle Repair Garage","Florist"]
store_name = ["Gerald's","Larry's","Fabien's","Grace's","Donnie's","Alex's","Sam's","Luke's","David's","Smith's","Burn's","Ellie's","Sarah's","Max's","Bob's","Tinks'","Zoe's","Rose's","Walter's","Philips'","Jose's","Antonio's","Juan's","Manuel's","Maria's","Anna's","Daniel's","Danny's","Jack's","Isabel's","Laura's","Shannon's"]
store_type = ["Hardware","Clothing","Drug","Grocery","Charity","Electronic","DIY","2nd Hand","Book","Gardening","Jewelery","Music","Game","Bicycle","Sports"]
commercial_building_extra = ["Parking Lot"]

##### INDUSTRIAL #####
industrial_building_choice = ["Manufacturing Factory","Warehouse","Power Station","Construction Site","Brewery","Nuclear Power Plant"]
factory_type = ["Petroleum","Chemical","Plastic","Food","Clothing","Textile","Metal","Electronic","Vehicle","Wood","Paper","Cardboard","Ceramic","Glass"]
industrial_building_extra = ["Warehouse"]

##### AGRICULTURAL #####
agricultural_building_choice = ["Farm","Forestry"]
agricultural_building_extra = ["Barn"]

##### GOVERNMENT #####
government_building_choice = ["Post Office","Police Station","School","Airport","Military Base"]
government_building_extra = ["Parking Lot"]

#####      MILITARY      #####

military_base_extra = ["Airfield"]
military_air_field = ["Hangar","Landling Pad", "Fuel Tank"]
military_air_facilities = ["Aircraft Repair & Maintenance"]
military_base_buildings = ["Barrack","Mess Hall","Office","Gym","Field","Facility","Hospital","Watch Tower","Bunker","Fuel Tank"]
military_base_building_default = ["Entrance Checkpoint"]
militrary_facilities = ["Ammunation Storage", "Weapon Storage","Military Intelligence","Vehicle Repair & Maintenance","Vehicle Storage","Weapon Repair & Maintenance"]

##### SIZE #####
building_size = ["Small","Medium","Large"]

# Used to store current counter of how many buildings have been generated
current_building_counter = 1

while True:
    user_input = int(input("\nEnter number of generated buildings: "))
    for i in range(user_input):
            print("")
            print("Building Number:",current_building_counter)
            current_building_counter = current_building_counter + 1
            bc = random.randint(0,100) # Generates building Condition 0% - 100%
            ec = random.randint(0,100) # Generates extra Condition 0% - 100%
            lt = random.choice(land_type) # Generates Land Type
            bss = 2 # Small buildings capped at 2 floors
            bsm = random.randint(2,4) # Generates floors for medium buildings
            bsl = random.randint(3,5) # Generates floors for large buildings
            multiple_stories = True # Multiple floors?
            extras_enabled = True # Extras?
            extra_true_or_false = random.randint(1,4)
            building_counter = random.randint(4,16)

            ################## VARIABLES ###################
            ################################################
            ################ FUNCTIONALITY ################

            # BUILDING CONDITION / SIZE FUNCTIONALITY
            if bc <= 25:
                bs = "Destroyed"
            else:
                bs = random.choice(building_size)

            if ec <= 25:
                ec = "Destroyed"
            else:
                ec = ec

            if extra_true_or_false == 1:
                extras_enabled = True
            else:
                extras_enabled = False

            if lt == "Residential":
                rbc = random.choice(residential_building_choice)

        ########################################################################################
        ########################################################################################
        ########################################################################################
        ########################################################################################
                # HOUSE OPTION
                if rbc == "House":
                    
            ########################################################################################
            ########################################################################################
                    #EXTRAS ENABLED
                    
                    if extras_enabled == True:
                         rbe = random.choice(residential_building_extra)
                         
            ########################################################################################
                    #HOUSE DESTROYED
                         
                         if bs == "Destroyed":
                             
            ########################################################################################
                     #HOUSE DESTROYED AND BUILDING EXTRA DESTROYED
                             
                            if ec == "Destroyed": 
                                 print(bs,rbc,"with a",ec,rbe)

            ########################################################################################
                     #HOUSE DESTROYED BUT BUILDING EXTRA NOT DESTROYED

                            else:
                                print(bs,rbc,"with a",rbe) 
                                print("(",rbe,"Condition: "+str(ec)+"% )")
                                

            ########################################################################################
                     #HOUSE NOT DESTROYED
                                
                         else:

            ########################################################################################
                     #HOUSE NOT DESTROYED BUT BUILDING EXTRA DESTROYED
                             
                             if ec == "Destroyed":

            ########################################################################################
                     #HOUSE WITH MULTIPLE FLOORS NOT DESTROYED BUT BUILDING EXTRA DESTROYED
                                 
                                 if multiple_stories == True:
                                    if bs == "Small":
                                        print(rbc,"with a",ec,rbe)
                                        print("( Size: "+str(bs)+" )")
                                        print("( Floors: "+str(bss)+" )")
                                        print("(",rbc,"Condition: "+str(bc)+"% )")
                                    elif bs == "Medium":
                                        print(rbc,"with a",ec,rbe)
                                        print("( Size: "+str(bs)+" )")
                                        print("( Floors: "+str(bsm)+" )") 
                                        print("(",rbc,"Condition: "+str(bc)+"% )")
                                    elif bs == "Large":
                                        print(rbc,"with a",ec,rbe)
                                        print("( Size: "+str(bs)+" )")
                                        print("( Floors: "+str(bsl)+" )") 
                                        print("(",rbc,"Condition: "+str(bc)+"% )")        
                                 elif multiple_stories == False:
                                    print(bs,rbc,"("+str(bc)+"%) with a",ec,rbe)
                                    print(rbc,"with a",ec,rbe)
                                    print("( Size: "+str(bs)+" )")
                                    print("( Floors: 1 )") 
                                    print("(",rbc,"Condition: "+str(bc)+"% )")

            ########################################################################################
                     #HOUSE WITH 1 FLOOR NOT DESTROYED BUT BUILDING EXTRA NOT DESTROYED

                             else:
                                    if multiple_stories == True:
                                        if bs == "Small":
                                            print(rbc,"with a",rbe)
                                            print("( Size: "+str(bs)+" )")
                                            print("( Floors: "+str(bss)+" )") 
                                            print("(",rbc,"Condition: "+str(bc)+"% )")
                                            print("(",rbe,"Condition: "+str(ec)+"% )")
                                        elif bs == "Medium":
                                            print(rbc,"with a",rbe)
                                            print("( Size: "+str(bs)+" )")
                                            print("( Floors: "+str(bsm)+" )") 
                                            print("(",rbc,"Condition: "+str(bc)+"% )")
                                            print("(",rbe,"Condition: "+str(ec)+"% )")
                                        elif bs == "Large":
                                            print(rbc,"with a",rbe)
                                            print("( Size: "+str(bs)+" )")
                                            print("( Floors: "+str(bsl)+" )") 
                                            print("(",rbc,"Condition: "+str(bc)+"% )")
                                            print("(",rbe,"Condition: "+str(ec)+"% )")
                                    elif multiple_stories == False:
                                        print(rbc,"with a",rbe)
                                        print("( Size: "+str(bs)+" )")
                                        print("( Floors: 1 )") 
                                        print("(",rbc,"Condition: "+str(bc)+"% )")
                                        print("(",rbe,"Condition: "+str(ec)+"% )")
            ########################################################################################
            ########################################################################################
                    #EXTRAS NOT ENABLED
                                        
                    else:

            ########################################################################################
                    #HOUSE DESTROYED
                        
                        if bs == "Destroyed":
                            print(bs,rbc)

            ########################################################################################
                    #HOUSE NOT DESTROYED

                        else:

            ########################################################################################
                    #HOUSE WITH MULTIPLE FLOORS NOT DESTROYED
                            
                            if multiple_stories == True:
                                if bs == "Small":
                                    print(rbc)
                                    print("( Size: "+str(bs)+" )")
                                    print("( Floors: "+str(bss)+" )") 
                                    print("(",rbc,"Condition: "+str(bc)+"% )")
                                elif bs == "Medium":
                                    print(rbc)
                                    print("( Size: "+str(bs)+" )")
                                    print("( Floors: "+str(bsm)+" )") 
                                    print("(",rbc,"Condition: "+str(bc)+"% )")
                                elif bs == "Large":
                                    print(rbc)
                                    print("( Size: "+str(bs)+" )")
                                    print("( Floors: "+str(bsl)+" )") 
                                    print("(",rbc,"Condition: "+str(bc)+"% )")

            ########################################################################################
                    #HOUSE WITH 1 FLOOR NOT DESTROYED

                            elif multiple_stories == False:
                                print(rbc)
                                print("( Size: "+str(bs)+" )")
                                print("( Floors: 1 )") 
                                print("(",rbc,"Condition: "+str(bc)+"% )")

        ########################################################################################
        ########################################################################################
        ########################################################################################
        ########################################################################################
                    #BUILDING WITH 1 FLOOR NOT DESTROYED

                else:
                    if bs == "Destroyed":
                        print(bs,rbc)
                    else:
                        print(rbc)
                        print("( Size: "+str(bs)+" )")
                        print("( Floors: 1 )") 
                        print("(",rbc,"Condition: "+str(bc)+"% )")
                    

            ########################################################################################   

            elif lt == "Commercial":
                rbc = random.choice(commercial_building_choice)
                #rbc = "Store"
                if extras_enabled == True:
                    rbe = random.choice(commercial_building_extra)

                    # Store Settings
                    
                    if rbc == "Store":
                        rsn = random.choice(store_name)
                        rft = random.choice(store_type)
                        if bs == "Destroyed": 
                                 print(bs,rbc,"with a",rbe)
                        else:
                                 print(rsn,rft,rbc,"with a",rbe)
                                 print("( Size: "+str(bs)+" )")
                                 print("( Condition: "+str(bc)+"% )")

                    # Florist Settings
                    
                    elif rbc == "Florist":
                        rsn = random.choice(store_name)
                        if bs == "Destroyed": 
                                 print(bs,rbc,"with a",rbe)
                        else:
                                 print(rsn,rbc,"with a",rbe)
                                 print("( Size: "+str(bs)+" )")
                                 print("( Condition: "+str(bc)+"% )")

                    # Hair Salon Settings
                    
                    elif rbc == "Hair Salon":
                        rsn = random.choice(store_name)
                        if bs == "Destroyed": 
                                 print(bs,rbc,"with a",rbe)
                        else:
                                 print(rsn,rbc,"with a",rbe)
                                 print("( Size: "+str(bs)+" )")
                                 print("( Condition: "+str(bc)+"% )")

                    # Stall Settings
                    
                    elif rbc == "Stall":
                        rsn = random.choice(store_name)
                        rft = random.choice(store_type)
                        if bs == "Destroyed": 
                                 print(bs,rbc,"with a",rbe)
                        else:
                                 print(rsn,rft,rbc,"with a",rbe)
                                 print("( Size: "+str(bs)+" )")
                                 print("( Condition: "+str(bc)+"% )")

                    # OTHER BUILDING SETTINGS

                    else:
                        if bs == "Destroyed": 
                                 print(bs,rbc,"with a",rbe)
                        else:
                                 print(rbc,"with a",rbe)
                                 print("( Size: "+str(bs)+" )")
                                 print("( Condition: "+str(bc)+"% )")


    #########################################################################################

                else:

                    # Store Settings
                    
                    if rbc == "Store":
                        rft = random.choice(store_type)
                        rsn = random.choice(store_name)
                        if bs == "Destroyed": 
                                 print(bs,rbc)
                        else:
                                 print(rsn,rft,rbc)
                                 print("( Size: "+str(bs)+" )")
                                 print("( Condition: "+str(bc)+"% )")
                    
                     # Florist Settings
                    
                    elif rbc == "Florist":
                        rsn = random.choice(store_name)
                        if bs == "Destroyed": 
                                 print(bs,rbc)
                        else:
                                print(rsn,rbc)
                                print("( Size: "+str(bs)+" )")
                                print("( Condition: "+str(bc)+"% )")

                    # Hair Salon Settings
                    
                    elif rbc == "Hair Salon":
                        rsn = random.choice(store_name)
                        if bs == "Destroyed": 
                                 print(bs,rbc)
                        else:
                                 print(rsn,rbc)
                                 print("( Size: "+str(bs)+" )")
                                 print("( Condition: "+str(bc)+"% )")

                    # Stall Settings
                    
                    elif rbc == "Stall":
                        rsn = random.choice(store_name)
                        rft = random.choice(store_type)
                        if bs == "Destroyed": 
                                 print(bs,rbc)
                        else:
                                 print(rsn,rft,rbc)
                                 print("( Size: "+str(bs)+" )")
                                 print("( Condition: "+str(bc)+"% )")             
                    
                    # OTHER BUILDING SETTINGS
                    
                    else:
                        if bs == "Destroyed":                    
                                print(bs,rbc)
                        else:
                                print(rbc) # ISSUE ( displays store )
                                print("( Size: "+str(bs)+" )")
                                print("( Condition: "+str(bc)+"% )")
                                     
            elif lt == "Industrial":
                rbc = random.choice(industrial_building_choice)
                if extras_enabled == True:
                    rbe = random.choice(industrial_building_extra)
                    if rbc == "Manufacturing Factory":
                        rft = random.choice(factory_type)
                        if bs == "Destroyed": 
                                 print(bs,rft,rbc,"with a",rbe)
                        else:
                                 print(rft,rbc,"with a",rbe)
                                 print("( Size: "+str(bs)+" )")
                                 print("( Condition: "+str(bc)+"% )")
                    else:
                        if bs == "Destroyed": 
                                 print(bs,rbc,"with a",rbe)
                        else:
                                 print(rbc,"with a",rbe)
                                 print("( Size: "+str(bs)+" )")
                                 print("( Condition: "+str(bc)+"% )")
                else:
                    if rbc == "Manufacturing Factory":
                        rft = random.choice(factory_type)
                        if bs == "Destroyed": 
                                 print(bs,rft,rbc)
                        else:
                                 print(rft,rbc)
                                 print("( Size: "+str(bs)+" )")
                                 print("( Condition: "+str(bc)+"% )")
                    else:
                        if bs == "Destroyed": 
                                 print(bs,rbc)
                        else:
                                 print(rbc)
                                 print("( Size: "+str(bs)+" )")
                                 print("( Condition: "+str(bc)+"% )")

            elif lt == "Agricultural":
                rbc = random.choice(agricultural_building_choice)
                if bs == "Destroyed":
                                print(bs,rbc)
                else: 
                                print(rbc)
                                print("( Size: "+str(bs)+" )")
                                print("( Condition: "+str(bc)+"% )")

            elif lt == "Government":
                rbc = random.choice(government_building_choice)
                if rbc == "Military Base":
                    if bs == "Destroyed":
                        print(bs,rbc)
                    else:

                        # MAX STRUCTURE LIMIT = 16
                        # MINIMUM STRUCTURE LIMIT = 4
                        building_counter = random.randint(4,16)
                        bcount = building_counter
                        mbbd = military_base_building_default[0]
                        updatedbcount = bcount + 1
                        
                        print(rbc)
                        print("( Size: "+str(bs)+" )")
                        print("( Condition: "+str(bc)+"% )")
                        print("( Structures: "+str(updatedbcount)+" )")
                        print("-------------------------")
                        print(mbbd)
                        for x in range(bcount):
                            mbb = random.choice(military_base_buildings)
                            print(mbb)
                            
                else:
                    if bs == "Destroyed": 
                                    print(bs,rbc)
                    else:
                                    print(rbc)
                                    print("( Size: "+str(bs)+" )")
                                    print("( Condition: "+str(bc)+"% )")
