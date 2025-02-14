# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:32:46 2025

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open('C:/Users/HP/OneDrive/Desktop/MachineBreastPred/trained_model.sav', 'rb'))

def breast_pred(input_data):
    # Changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Prediction
    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return 'The Woman has no Breast Cancer...'
    else:
        return 'The Woman has Breast cancer...'

def main():
    # Add custom CSS for styling the background, header, and other elements
    st.markdown("""
        <style>
            body {
                background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFKyii0ettixVpuTZFJtAwM3i4fz7HQr-iZA&s');
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                font-family: 'Arial', sans-serif;
                color: #ffffff;
            }
            .title {
                font-size: 50px;
                font-weight: bold;
                color: #FF6347;  /* Tomato color */
                text-align: center;
                margin-top: 50px;
                font-family: 'Helvetica', sans-serif;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            }
            .input-container {
                background-color: rgba(0, 0, 0, 0.6);
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
                margin-top: 30px;
                width: 50%;
                margin-left: auto;
                margin-right: auto;
            }
            .stButton>button {
                background-color: #FF6347;  /* Tomato color */
                color: white;
                font-size: 20px;
                font-weight: bold;
                padding: 15px 30px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            .stButton>button:hover {
                background-color: #ff4500;  /* Darker Tomato on hover */
            }
            .stTextInput>div>input {
                font-size: 18px;
                padding: 10px;
                border-radius: 5px;
                width: 100%;
            }
            /* Override specific Streamlit component CSS */
            .css-1v3fvcr {  /* Custom button styling */
                background-color: #FF6347;
                color: white;
            }
            .css-1v3fvcr:hover {
                background-color: #ff4500;  /* Darker Tomato on hover */
            }
        </style>
    """, unsafe_allow_html=True)

    # Add a custom title
    st.markdown('<div class="title">Breast Cancer Prediction Web App</div>', unsafe_allow_html=True)

    # Initialize session state variables if not present
    if 'texture_worst' not in st.session_state:
        st.session_state['texture_worst'] = ''
        st.session_state['perimeter_worst'] = ''
        st.session_state['smoothness_worst'] = ''
        st.session_state['concave'] = ''
        st.session_state['symmetry_worst'] = ''
        st.session_state['diagnosis'] = ''

    # Container for inputs with custom styling
    with st.container():
        st.markdown('<div class="input-container">', unsafe_allow_html=True)

        # Taking user input with proper validation and styling
        try:
            texture_worst = st.text_input('Texture of the Subject', value=st.session_state['texture_worst'])
            perimeter_worst = st.text_input('Perimeter of the Subject', value=st.session_state['perimeter_worst'])
            smoothness_worst = st.text_input('Smoothness of the Subject', value=st.session_state['smoothness_worst'])
            concave = st.text_input('Concavity of the Subject', value=st.session_state['concave'])
            symmetry_worst = st.text_input('Symmetry of the Subject', value=st.session_state['symmetry_worst'])
        except ValueError:
            st.error("Please enter valid numeric values.")
            return

        diagnosis = st.session_state['diagnosis']

        # Prediction button
        if st.button('Breast test RESULT'):
            # Convert inputs to float and update session state
            try:
                input_data = [
                    float(texture_worst), float(perimeter_worst), float(smoothness_worst),
                    float(concave), float(symmetry_worst)
                ]
                diagnosis = breast_pred(input_data)
                st.session_state['texture_worst'] = texture_worst
                st.session_state['perimeter_worst'] = perimeter_worst
                st.session_state['smoothness_worst'] = smoothness_worst
                st.session_state['concave'] = concave
                st.session_state['symmetry_worst'] = symmetry_worst
                st.session_state['diagnosis'] = diagnosis
            except ValueError:
                st.error("Please enter valid numeric values.")

        # Reset button to clear inputs and diagnosis
        if st.button('Reset'):
            st.session_state['texture_worst'] = ''
            st.session_state['perimeter_worst'] = ''
            st.session_state['smoothness_worst'] = ''
            st.session_state['concave'] = ''
            st.session_state['symmetry_worst'] = ''
            st.session_state['diagnosis'] = ''

        # Display the result
        st.success(diagnosis)

        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
