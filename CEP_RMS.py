# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 03:44:03 2024

@author: Jeremy Hong
"""
import numpy as np

# Function to calculate CEP from RMS error and range
def calculate_cep_from_rms(rms_error_degrees, range_km):
    # Convert degrees to radians for the sin function
    radians = np.deg2rad(rms_error_degrees)
    
    # Calculate the CEP
    cep_km = (1.07 * 2 * range_km * np.sin(radians / 2)) / 1.77
    
    return cep_km

# Example usage:
rms_error_degrees = 5  # replace with user input
range_km = 100         # replace with user input

calculate_cep_from_rms(rms_error_degrees, range_km)
