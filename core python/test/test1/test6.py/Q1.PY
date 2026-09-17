from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def calculate_toll(self, persons):
        pass


# Two Wheeler
class TwoWheeler(Vehicle):

    def calculate_toll(self, persons):
        toll = 20

        if persons > 2:
            toll = toll + (persons - 2) * 10

        return toll


# Three Wheeler
class ThreeWheeler(Vehicle):

    def calculate_toll(self, persons):
        toll = 30

        if persons > 3:
            toll = toll + (persons - 3) * 20

        return toll


# Four Wheeler
class FourWheeler(Vehicle):

    def calculate_toll(self, persons):
        toll = 40

        if persons > 4:
            toll = toll + (persons - 4) * 40

        return toll


# Heavy Vehicle
class HeavyVehicle(Vehicle):

    def calculate_toll(self, persons):
        toll = 60

        if persons > 6:
            toll = toll + (persons - 6) * 100

        return toll

# TOTAL
while True:

    print("\n----- TOLL MENU -----")
    print("1. Two Wheeler")
    print("2. Three Wheeler")
    print("3. Four Wheeler")
    print("4. Heavy Vehicle")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Thank you!")
        break

    persons = int(input("Enter number of persons: "))

    if choice == 1:
        v = TwoWheeler()

    elif choice == 2:
        v = ThreeWheeler()

    elif choice == 3:
        v = FourWheeler()

    elif choice == 4:
        v = HeavyVehicle()

    else:
        print("Invalid choice")
        continue

    print("Total Toll = Rs.", v.calculate_toll(persons))