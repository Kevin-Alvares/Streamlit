import pandas as pd
import streamlit as st
import datetime
import pickle 

# . = current directory
# .. = parent directory
cars_df = pd.read_csv("./car_price.csv")

st.write(
    """
    # Used Car - Price Predictor
    """
)

st.dataframe(cars_df.head())

# maintain the order in which you trained the features otherwise 
# weight w1 will be assigned to the wrong feature
col_1,col_2 = st.columns(2)

fuel_type = col_1.selectbox("Select the fuel type",
                     ("Petrol","Diesel","CNG","LPG","Electric"))

engine = col_1.slider("Set the Engine Power", 500, 5000, 100)

transmission_type = col_2.selectbox("Select the transmission type", cars_df.transmission_type.unique())
       #              ("Manual","Automatic"))

seats = col_2.selectbox("Enter the number of seats",(4,5,7,9,11))

encode_dict = {
    "fuel_type":{'Diesel':1,'Petrol':2,'CNG':3,'LPG':4,'Electric':5},
    "seller_type":{'Dealer':1,'Individual':2,'Trustmark Dealer':3},
    "transmission_type":{'Manual':1,'Automatic':0}
}

def model_pred(fuel_type,transmission_type,engine,seats):

    # load the model
    with open("car_pred",'rb') as file:
        reg_model= pickle.load(file)
        input_features = [[2018.0,1,4000,fuel_type,transmission_type,19.70,engine,86.30,seats]]

        return reg_model.predict(input_features)

if (st.button("Predict Price")):

    fuel_type = encode_dict['fuel_type'][fuel_type]
    transmission_type = encode_dict['transmission_type'][transmission_type]

    price = model_pred(fuel_type,transmission_type,engine,seats)

    st.text(f"The price of the car is {price[0].round(2)} lakh rupees")