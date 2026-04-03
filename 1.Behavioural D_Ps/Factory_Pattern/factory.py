from car import Car
from bike import Bike

class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type.lower() == "car":
            return Car()
        elif vehicle_type.lower() == "bike":
            return Bike()
        else:
            raise ValueError("Unknown vehicle type")