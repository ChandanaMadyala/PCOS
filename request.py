# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 11:25:42 2021

@author: bawej
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url, json={
    'Follicle_No.(R)': 'value',
    'Follicle_No.(L)': 'value',
    'Weight_gain(Y/N)': 'value',
    'Skin_darkening (Y/N)': 'value',
    'Hair Growth (Y/N)': 'value',
    'Irregular_Cycle(Y/N)': 'value',
    'Fast_food_(Y/N)': 'value',
    'Pimples (Y/N)': 'value',
    'AMH(ng/mL)': 'value'
})


print(r.json())