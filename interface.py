from flask import Flask, jsonify,request, render_template
import config 
from project_app.utils import CarPrice

app = Flask(__name__)


########################### Homepage API ####################################

@app.route('/')
def car_price_prediction_model():
    print('Welcome to the prediction model')

    return render_template('index.html')


########################### Model API ####################################

@app.route('/predict', methods= ['POST','GET'])
def get_car_price():
    if request.method == 'POST':
        print('We are in POST method')
        data= request.form
        
        Car_ID = eval(data['Car_ID'])
        Year = eval(data['Year'])
        Kilometers_Driven = eval(data['Kilometers_Driven'])
        Fuel_type = data['Fuel_type']
        Transmission = data['Transmission']
        Owner_type = data['Owner_type']
        Mileage = eval(data['Mileage'])
        Engine = eval(data['Engine'])
        Power = eval(data['Power'])
        Seats = eval(data['Seats'])
        Brand = data['Brand']
        
        #print(data)

        car_pr = CarPrice(Car_ID,Year,Kilometers_Driven,Fuel_type,Transmission,Owner_type,Mileage,Engine,Power,Seats,Brand)
        price = car_pr.get_predicted_price()
        return jsonify({'Result':f'Price of the car is: {round(price,2)}'})

    else:
        print('We are in GET method')
        data1 = request.args
        Car_ID = int(data1.get('Car_ID'))
        Year = int(data1.get('Year'))
        Kilometers_Driven = int(data1.get('Kilometers_Driven'))
        Fuel_type = data1.get('Fuel_type')
        Transmission = data1.get('Transmission')
        Owner_type = data1.get('Owner_type')
        Mileage = int(data1.get('Mileage'))
        Engine = int(data1.get('Engine'))
        Power = int(data1.get('Power'))
        Seats = int(data1.get('Seats'))
        Brand = data1.get('Brand')

        car_pr1 = CarPrice(Car_ID,Year,Kilometers_Driven,Fuel_type,Transmission,Owner_type,Mileage,Engine,Power,Seats,Brand)
        price1 = car_pr1.get_predicted_price()
        return jsonify({'Result':f'Price of the car is: {round(price1,2)}'})
             


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.PORT_NUMBER, debug=False) 