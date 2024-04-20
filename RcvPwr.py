# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 04:07:11 2024

@author: Jeremy Hong
"""

import numpy as np

# Function to calculate received signal power
def calculate_received_signal_power(tx_power_dbm, tx_gain_db, rx_gain_db, 
                                   distance_km, tx_height_m, rx_height_m, frequency_mhz):
    # Calculate the Fresnel Zone to decide if LOS or 2-ray propagation is used
    fz = (tx_height_m * rx_height_m * frequency_mhz) / 24000

    # Determine the path loss based on whether LOS or 2-ray propagation is appropriate
    if distance_km > fz:  # If distance is greater than FZ, use 2-ray propagation loss
        loss_db = 120 + 40 * np.log10(distance_km) - 20 * np.log10(tx_height_m) - 20 * np.log10(rx_height_m)
    else:  # Otherwise, use LOS propagation loss
        loss_db = 32.44 + 20 * np.log10(distance_km) + 20 * np.log10(frequency_mhz)

    # Calculate received signal power
    received_power_dbm = tx_power_dbm + tx_gain_db + rx_gain_db - loss_db
    
    return received_power_dbm

# Example usage with placeholders for input values
tx_power_dbm = 30  # replace with actual value
tx_gain_db = 14    # replace with actual value
rx_gain_db = 14    # replace with actual value
distance_km = 5    # replace with actual value
tx_height_m = 30   # replace with actual value
rx_height_m = 30   # replace with actual value
frequency_mhz = 2400  # replace with actual value (example: 2.4 GHz)

# Calculate received signal power
received_signal_power = calculate_received_signal_power(tx_power_dbm, tx_gain_db, rx_gain_db, 
                                                       distance_km, tx_height_m, rx_height_m, 
                                                       frequency_mhz)
received_signal_power
