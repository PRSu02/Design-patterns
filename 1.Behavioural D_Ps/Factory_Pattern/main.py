from factory import VehicleFactory

if __name__ == "__main__":
    vehicle1 = VehicleFactory.get_vehicle("car")
    print(vehicle1.drive())

    vehicle2 = VehicleFactory.get_vehicle("bike")
    print(vehicle2.drive())