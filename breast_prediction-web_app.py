# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 01:01:54 2025

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open('C:/Users\HP/OneDrive/Desktop/fgvyjtfdtyt/trained_model_pred.sav','rb'))

def breast_pred(input_data):
     

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return'The Woman has no Breast Cancer...'
    else:
      return'The Woman has Breast cancer...'
      
      
   
      
def main():
    
    st.title('Breast Cancer prediction')
   
    texture_worst=st.text_input('texture worst') 
    perimeter_worst=st.text_input('perimeter')
    smoothness_worst=st.text_input('smoothness')               
    concavepoints_worst=st.text_input('concave')    
    symmetry_worst=st.text_input('symmetry')    
    
    diagnosis=''
    
    if st.button('Breast Test Result'):
        diagnosis= breast_pred([texture_worst,perimeter_worst,smoothness_worst,concavepoints_worst,symmetry_worst])
    
    st.success(diagnosis)
    
    
    
if __name__== '__main__':
    main()