import pickle
import streamlit as st
import pandas as pd

with open('model.pkl','rb') as f:
    model =pickle.load(f)

date = st.date_input('select date')


lag_1 = st.number_input("Enter Previous Day Sales (lag_1)")

d1 = st.number_input('sales day 1')
d2 = st.number_input('sales day 2')
d3 = st.number_input('sales day 3')

ma_3 = (d1+d2+d3)/3


if st.button('predication final score'):
         input_df = pd.DataFrame({
          'lag_1': [lag_1],
          'ma_3': [ma_3]
         })
         prediction = model.predict(input_df)
         st.success(f"Predicted Sales: {prediction[0]:.2f}")

