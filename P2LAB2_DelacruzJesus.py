
# Jesus Delacruz
# 09 October 2024
# P2LAB2_DelacruzJesus
# how to write code that uses a dictionary to store user input and displays output to the user


# List of car models as keys and their MPG (miles per gallon)

vehicle_mpg ={
    "Camaro": 18.21,
    
    "Prius": 52.36,
    
    "Model S": 110,
    
    "Silverado": 26
}



# Variable that holds all keys in the dictionary
vehicle_keys = vehicle_mpg.keys()

# Variable that holds the keys
print(vehicle_keys)

# Enter 1 of the vehicles from the dictionary
vehicle = input("Enter one of the vehicles Above to view its MPG: ")

# Verify if vehicle is in the dictionary
if vehicle in vehicle_mpg:
    mpg = vehicle_mpg[vehicle]
    print(f"The Miles Per Gallon for the {vehicle} are {mpg}.")

    # How many miles the does the driver, drive the vehicle
    miles = float(input("How many miles you will drive: "))

    # Add up the gallons of gas needed
    gallons_needed = miles / mpg

    # Total the gallons of gas needed (rounded to two decimal places)
    print(f"You will need {gallons_needed:.2f} gallons of gas.")
