# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 03:45:27 2024

@author: Jeremy Hong
"""

import numpy as np

# Function to calculate the receiver dynamic range from the number of quantizing bits
def calculate_dynamic_range(bits):
    # Calculate the dynamic range in dB
    dynamic_range_db = 20 * np.log10(2**bits)
    
    return dynamic_range_db

# Example usage:
number_of_bits = 8  # replace with user input

calculate_dynamic_range(number_of_bits)
