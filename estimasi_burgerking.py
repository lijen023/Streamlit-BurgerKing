import pickle
import streamlit as st

model = pickle.load(open('estimasi_burgerking.sav', 'rb'))

st.title('Estimasi Jumlah Kalori Menu Burger King')
Cholesterol = st.number_input('Input Kolesterol (mg)')
Total_Carb = st.number_input('Input Total Karbohidrat (g)')
Sugars = st.number_input('Input Jumlah Gula (g)')
Protein = st.number_input('Input Jumlah Protein (g)')

predict = ''

if st.button('Estimasi Kalori'):
    predict = model.predict(
        [[Cholesterol, Total_Carb, Sugars, Protein]]
        )
    st.write ('Estimasi Jumlah Kalori Menu Burger King : ', predict)