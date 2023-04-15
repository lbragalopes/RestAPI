import json

class Vehicle:
    def __init__(self, registration_number, year_of_production, passenger, mass):
        self.registration_number = registration_number
        self.year_of_production = year_of_production
        self.passenger = passenger
        self.mass = mass

class VehicleEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Vehicle):
            passenger = True if obj.passenger =='y' else False
            return {'registration_number': obj.registration_number, 'year_of_production': obj.year_of_production, 'passenger': obj.passenger, 'mass': obj.mass}
        return super().default(obj)


if __name__ == '__main__':
    while True:
        option = input(" What can I do for you?:\n 1 - produce a JSON string describing a vehicle. \n 2 - decode a JSON string into vehicle data.\n Your choice: ")

        if option == "1":
            registration_number = input("Registration number: ")
            year_of_production = input("Year of production: ")
            passenger = input("Passengers [y/n]: ")
            mass = input("Vehicle mass: ")

            vehicle = Vehicle(registration_number, year_of_production, passenger, mass)

            vehicle_json = json.dumps(vehicle, cls=VehicleEncoder)
            print("Result JSON string is:")
            print(vehicle_json)
            print("Done")
            break
        elif option == "2":
            vehicle_json_str = input("Enter vehicle JSON string: ")
            dict_obj = json.loads(vehicle_json_str)
            print(dict_obj)
            print("Done")
            break
        else:
            print(" Invalid option.")
