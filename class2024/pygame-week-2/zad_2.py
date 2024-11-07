from typing import List, Tuple


vehicles = [
    ('Bicikl', 20),
    ('Auto', 200),
    ('Kombi', 3000),
    ('Kamion', 10000),

]

class VehicleFactory:
    def __init__(self, vehicles: List[Tuple[str, int]]):
        self.vehicles = vehicles
        self.vehicles.sort(key=lambda x: x[1])
    
    def create_vehicle(self, weight: int):
        for tup in self.vehicles:
            if tup[1] > weight:
                return tup
        
        raise Exception('To heavy')
        


if __name__ == '__main__':
    vf = VehicleFactory(vehicles)
    while True: 

        weight = int(input())

        vehicle = vf.create_vehicle(weight)

        print(vehicle)
