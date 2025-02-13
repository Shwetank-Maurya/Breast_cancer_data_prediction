# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
loaded_model=pickle.load(open('C:/Users\HP/OneDrive/Desktop/fgvyjtfdtyt/trained_model_pred.sav','rb'))


input_data = (17.33,184.60,0.16220,0.2654,0.41915)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The Woman has no Breast Cancer...')
else:
  print('The Woman has Breast cancer...')