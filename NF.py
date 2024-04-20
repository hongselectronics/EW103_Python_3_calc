# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 04:03:20 2024

@author: Jeremy Hong
"""

import numpy as np

# Function to calculate the receiver system noise figure in dB
def calculate_receiver_noise_figure(loss_before_preamplifier_db, preamplifier_gain_db, 
                                    preamplifier_noise_figure_db, loss_between_preamplifier_and_receiver_db, 
                                    receiver_noise_figure_db):
    
    # Convert all dB values to linear scale for calculation
    L1 = 10 ** (loss_before_preamplifier_db / 10)
    G1 = 10 ** (preamplifier_gain_db / 10)
    N1 = 10 ** (preamplifier_noise_figure_db / 10)
    L2 = 10 ** (loss_between_preamplifier_and_receiver_db / 10)
    N2 = 10 ** (receiver_noise_figure_db / 10)
    
    # Perform the noise figure calculation on a linear scale
    noise_figure_linear = L1 + N1 + (N2 * L2 / G1)
    
    # Convert the result back to dB
    receiver_system_noise_figure_db = 10 * np.log10(noise_figure_linear)
    
    return receiver_system_noise_figure_db

# Example usage with placeholders for input values
loss_before_preamplifier_db = 1    # replace with actual value
preamplifier_gain_db = 1           # replace with actual value
preamplifier_noise_figure_db = 1   # replace with actual value
loss_between_preamplifier_and_receiver_db = 1  # replace with actual value
receiver_noise_figure_db = 1       # replace with actual value

# Calculate receiver system noise figure
receiver_system_noise_figure = calculate_receiver_noise_figure(loss_before_preamplifier_db, 
                                                              preamplifier_gain_db, 
                                                              preamplifier_noise_figure_db, 
                                                              loss_between_preamplifier_and_receiver_db, 
                                                              receiver_noise_figure_db)
receiver_system_noise_figure
