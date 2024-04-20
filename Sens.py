# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 04:08:26 2024

@author: Jeremy Hong
"""
import numpy as np

# Function to calculate receiver system sensitivity
def calculate_receiver_sensitivity(bandwidth_mhz, noise_figure_db, required_snr_db):
    # Calculate sensitivity
    sensitivity_dbm = -114 + 10 * np.log10(bandwidth_mhz) + noise_figure_db + required_snr_db
    
    return sensitivity_dbm

# Example usage with placeholders for input values
bandwidth_mhz = 1     # replace with actual value
noise_figure_db = 1   # replace with actual value
required_snr_db = 1   # replace with actual value

# Calculate receiver system sensitivity
receiver_sensitivity = calculate_receiver_sensitivity(bandwidth_mhz, noise_figure_db, required_snr_db)
receiver_sensitivity
