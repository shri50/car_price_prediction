import pickle
import json
import config
import numpy as np


class CarPrice():
    
    def __init__(self,Car_ID,Year,Kilometers_Driven,Fuel_type,Transmission,Owner_type,Mileage,Engine,Power,Seats,Brand):
        self.Car_ID = Car_ID
        self.Year = Year
        self.Kilometers_Driven = Kilometers_Driven
        self.Fuel_type = Fuel_type
        self.Transmission = Transmission
        self.Owner_type = Owner_type
        self.Mileage = Mileage
        self.Engine = Engine
        self.Power = Power
        self.Seats = Seats
        self.Brand = 'Brand_' + Brand

    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.project_data = json.load(f)

    def get_predicted_price(self):
        self.load_model()
        test_array = np.zeros(len(self.project_data['columns']))

        test_array[0] = self.Car_ID
        test_array[1] = self.Year
        test_array[2] = self.Kilometers_Driven
        test_array[3] = self.project_data['Fuel_type'][self.Fuel_type]
        test_array[4] = self.project_data['Transmission'][self.Transmission]
        test_array[5] = self.project_data['Owner_type'][self.Owner_type]
        test_array[6] = self.Mileage
        test_array[7] = self.Engine
        test_array[8] = self.Power
        test_array[9] = self.Seats
        #brand_val = 'Brand_' + Brand
        brand_index = self.project_data['columns'].index(self.Brand)
        test_array[brand_index] = 1

        print('Test Array: ',test_array)

        predit_car_price =self.model.predict([test_array])[0]
        print(f'Price of the car is: {round(predit_car_price,2)}')
        return predit_car_price

if __name__ == '__main__':
     
    Car_ID=1.0
    Year=2018.0
    Kilometers_Driven=47000.0
    Fuel_type='Petrol'
    Transmission='Manual'
    Owner_type='First'
    Mileage=15.0
    Engine=1498.0
    Power=108.0
    Seats=5.0
    Brand='Toyota'

    car_pr = CarPrice(Car_ID,Year,Kilometers_Driven,Fuel_type,Transmission,Owner_type,Mileage,Engine,Power,Seats,Brand)
    car_pr.get_predicted_price()