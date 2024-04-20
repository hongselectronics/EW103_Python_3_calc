# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 04:01:41 2024

@author: Jeremy Hong
"""

import numpy as np

# Function to calculate the line of sight loss in dB for a one-way link
def calculate_line_of_sight_loss(distance_km, frequency_mhz):
    # Calculate the line of sight loss using the given formula
    loss_db = 32.44 + 20 * np.log10(distance_km) + 20 * np.log10(frequency_mhz)
    
    return loss_db

# Example usage:
link_distance_km = 1  # replace with actual value
frequency_mhz = 1     # replace with actual value

# Calculate line of sight loss
line_of_sight_loss = calculate_line_of_sight_loss(link_distance_km, frequency_mhz)
line_of_sight_loss
