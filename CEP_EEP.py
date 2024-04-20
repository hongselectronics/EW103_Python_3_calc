# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 03:40:32 2024

@author: Jeremy Hong
"""
import numpy as np

# Function to calculate CEP from the long and short axis of EEP
def calculate_cep(long_axis_km, short_axis_km):
    # Calculate the CEP
    cep_km = 0.75 * np.sqrt((long_axis_km / 2)**2 + (short_axis_km / 2)**2)
    
    return cep_km

# Example usage:
long_axis_km = 10  # replace with user input
short_axis_km = 5   # replace with user input

calculate_cep(long_axis_km, short_axis_km)
