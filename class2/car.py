class Car():
 
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        print("Gas tank is being filled")

class ElectricCar(Car):
    
    def __init__(self, make, model, year):
 
        super().__init__(make, model, year)
        #super()takes you to the parent class initializer
        self.battery = Battery('Exide', 27, 200)
        #Exide Chalti Jaye!!
        self.tyre = Tyre('Bridgestone', 205, 15, 8.4, 84)
        #Solutions for your journey !!
        
    def batterysize(self):
        return f'This Car has a {self.battery_size} kwh-sized battery!'
    
    def fill_gas_tank(self):
        return "This car doesn't need a tank!"
    

class Battery():
    def __init__(self, manufacture, cell, power_amp):
        self.manufacture = manufacture
        self.cell = cell
        self.power_amp = power_amp
        
    def battery_power(self):
        print(f"{self.power_amp}")
    
    def Battery_description(self):
        
        print(f"""
        Manufacturer: {self.manufacture}
        Number of Cells: {self.cell}
        """)

class Tyre():
     
    def __init__(self, manufacturer, width, rim_diameter, grip_score, load):
        self.width = width
        self.rim_diameter = rim_diameter
        self.grip_score = grip_score
        self.load = load
        self.manufacturer = manufacturer
        
    def tyre_load(self):
        print(f"This tyre can pick upto {self.load} tons of load in a single time! ")
    
    def tyre_description(self):
        print(f"""
        Manufacturer: {self.manufacturer}
        Grip Score of Tyre: {self.grip_score}
        Width of Tyre : {self.width}
        Rim Diameter of Tyre: {self.rim_diameter}
        """)
