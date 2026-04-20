import streamlit as st
import numpy as np
import pandas as pd
import joblib
st.title("House price Prediction")

# Load the model and columns
model= joblib.load("model.pkl")
columns= joblib.load("columns.pkl")

#-------USER INPUT -------
area = st.number_input('Area',min_value=1650,max_value=16200)
bedrooms = st.number_input('Bedrooms',min_value=1,max_value=6)
bathrooms = st.number_input('Bathrooms',min_value=1,max_value=4)
stories = st.number_input('Stories',min_value=1,max_value=4)
parking = st.number_input('Parking',min_value=0,max_value=3)
mainroad = st.selectbox('Main Road', ['Yes', 'No'])
guestroom = st.selectbox('Guest Room', ['Yes', 'No'])
basement = st.selectbox('Basement', ['Yes', 'No'])
airconditioning = st.selectbox('Air Conditioning', ['Yes', 'No'])
hotwaterheating = st.selectbox('Hot Water Heating', ['Yes', 'No'])

prefarea = st.selectbox('Preferred Area', ['Yes', 'No'])
furnishing = st.selectbox('Furnishing Status', 
                                 ['Unfurnished', 'Semi-furnished', 'furnished'])


#------------ CONVERTS INPUTS--------------
def yes_no(val):
    return 1 if val == "Yes" else 0

mainroad = yes_no(mainroad)
guestroom = yes_no(guestroom)
basement = yes_no(basement)
airconditioning = yes_no(airconditioning)
hotwaterheating = yes_no(hotwaterheating)
prefarea = yes_no(prefarea)



#-------- Prepropessing ------

# log trasnform ( same as training)
area_log = np.log1p(area)

# one-hot encoding for furnishing status
semi= 1 if furnishing == 'semi-furnished' else 0
unfinished= 1 if furnishing == 'Unfurnished'else 0
    

#-----------Building input dict ---------    
input_dict ={
"area_log":area_log,
"bedrooms":bedrooms,
'bathrooms':bathrooms,
"stories":stories,
"parking":parking,
"mainroad":mainroad,
"guestroom":guestroom,
'basement':basement,
'airconditioning':airconditioning,
"hotwaterheating":hotwaterheating,
"prefarea":prefarea,
"furnishingstatus_semi-furnished":semi,
"furnishingstatus_unfurnished":unfinished}

# Convert to DataFrame
input_df= pd.DataFrame([input_dict])

#Ensure column order matches training columns exactly and fill missing columns with 0
input_df = input_df.reindex(columns=columns, fill_value=0)


#------Predict --------
if st.button('Predict'):
    log_price = model.predict(input_df)
    real_price = np.expm1(log_price) # convert log price back to real price

    st.success(f'Estimated price:{real_price[0]:,.0f}')
