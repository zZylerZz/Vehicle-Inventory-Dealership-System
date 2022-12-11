# https://pastebin.com/ThHqvmcR
# Should I make a customer & admin classes?
# https://github.com/SoumenNath/Python-Car-Dealership/blob/master/SoumenNath_CarDealership.py
# want it to be like this^ but without csv and imported modules

# Check the chat also in repl



# 2022-12-09T07:57:00Z: check choice 2, you have an unnecessary continue statement that is exiting the control flow statement and returning to the main menu
print('Vehicle Inventory')
vehicles = []
car = {}


class Vehicle_Screen:
    def __init__(self):
        self._make = ''
        self._model = ''
        self._year = 0
        self._color = ''
        self._price = 0

    def add_car(self):
        try:
            self._make = input('Enter vehicle make: ')
            self._model = input('Enter vehicle model: ')
            self._year = int(input('Enter vehicle year: '))
            self._color = input('Enter vehicle color: ')
            self._price = int(input('Enter vehicle price: '))
            return True
        except ValueError:
            print('Please try entering vehicle information again using only whole numbers for mileage and year')
            return False

    def __str__(self):
        return '\t'.join(str(a) for a in [self._make, self._model, self._year, self._color, self._price])

 

class Car_Inventory:
    def __init__(self):
        self.cars = []

    def add_car(self):
        vehicle = Vehicle_Screen()
        if vehicle.add_car() == True:
            self.cars.append(vehicle)
            print('\nThis vehicle has been added, Thank you')

    def display_car_inventory(self):
        print('\t'.join(['', 'Make', 'Model', 'Year', 'Color', 'Price']))
        for idx, vehicle in enumerate(self.cars):
            print(idx + 1, end='\t')
            print(vehicle)



inventory = Car_Inventory()

while True:

 

  print('Choice 1: Add Vehicle to Inventory')

  print('Choice 2: Delete Vehicle from Inventory')

  print('Choice 3: View Current Inventory')

  print('Choice 4: Update Vehicle in Inventory')

  print('Choice 5: Export Current Inventory')

  print('Choice 6: Purchase A Vehicle')
  
  user_choice = input('Please Enter your Choice from one of the above options: ')
  if user_choice == "1":

#add a vehicle11111

    inventory.add_car()

  elif user_choice == '2':
    inventory.display_car_inventory()

#delete a vehicle

    if len(inventory.cars) < 1:

        print('Sorry there are no vehicles currently in inventory')

    

    

    product = int(input('Please enter the number associated with the vehicle to be removed: '))

    if product - 1 > len(inventory.cars):

        print('This is an invalid number')

    else:

        inventory.cars.remove(inventory.cars[product - 1])

        print()

        print('This vehicle has been removed')

  elif user_choice == '3':

#list all the vehicles

    if len(inventory.cars) < 1:

        print('Sorry there are no vehicles currently in inventory')

        continue

    inventory.display_car_inventory()

  elif user_choice == '4':

#edit vehicle

    if len(inventory.cars) < 1:

        print('Sorry there are no vehicles currently in inventory')

        continue

    inventory.display_car_inventory()

    product = int(input('Please enter the number associated with the vehicle to be updated: '))

    if product - 1 > len(inventory.cars):

        print('This is an invalid number')

    else:

        auto_vehicle = Vehicle_Screen()

        if auto_vehicle.add_car() == True :

            inventory.cars.remove(inventory.cars[product - 1])

            inventory.cars.insert(product - 1, auto_vehicle)

            print()

            print('This vehicle has been updated')

  elif user_choice == '5':

#export inventory to file

    if len(inventory.cars) < 1:

        print('Sorry there are no vehicles currently in inventory')

        continue

    file = open('vehicle_inventory.txt', 'w')

    file.write('\t'.join(['Make', 'Model', 'Year', 'Color', 'Price']))

    file.write('\n')

    for car_v in inventory.cars:

        file.write('%s\n' % car_v)

    file.close()

    print('The vehicle inventory has been exported to a file')



#THIS IS THE MAIN THING TO FIX

#purchase a car    
  elif user_choice == '6':
    print('Purchase A Vehicle')
    inventory.display_car_inventory()
    purchase_car = input('Which car would you like to purchase? ')
    for vehicle in vehicles:
      if purchase_car.lower() == car['make'].lower() :
        if vehicle['quantity'] != 0 :
          print('Pay ', vehicle['price'] , 'at the dealership.')
          vehicle['quantity'] -= 1
        else:
          print('This car is not in stock')
          break
      else:
          print('This is an invalid input. Please try again.')
