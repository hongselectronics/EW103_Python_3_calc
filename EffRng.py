# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 03:46:16 2024

@author: Jeremy Hong
"""
import numpy as np
# Function to calculate the effective range of a one-way link using the 2ray and LOS models
def calculate_effective_range(tx_power_dbm, tx_gain_db, rx_gain_db, 
                              tx_height_m, rx_height_m, frequency_mhz, 
                              rx_sensitivity_dbm):
    # Calculate the 2ray dist
    two_ray_dist_km = 10 ** ((tx_power_dbm + tx_gain_db + rx_gain_db - 120 
                              + 20 * np.log10(tx_height_m) + 20 * np.log10(rx_height_m) 
                              + frequency_mhz - rx_sensitivity_dbm) / 40)

    # Calculate the LOS dist
    los_dist_km = 10 ** ((tx_power_dbm + tx_gain_db + rx_gain_db - 32.44 
                          - 20 * np.log10(frequency_mhz) + rx_gain_db 
                          - rx_sensitivity_dbm) / 20)

    # Calculate the Fresnel Zone (FZ)
    fz_km = tx_height_m * rx_height_m * frequency_mhz / 24000

    # Choose the effective range
    effective_range_km = max(two_ray_dist_km, los_dist_km)

    return two_ray_dist_km, los_dist_km, fz_km, effective_range_km

# Example usage:
tx_power_dbm = 30       # replace with user input
tx_gain_db = 15         # replace with user input
rx_gain_db = 15         # replace with user input
tx_height_m = 30        # replace with user input
rx_height_m = 30        # replace with user input
frequency_mhz = 2400    # replace with user input (example: 2.4 GHz)
rx_sensitivity_dbm = -100 # replace with user input

# Calculate effective range
calculate_effective_range(tx_power_dbm, tx_gain_db, rx_gain_db, 
                          tx_height_m, rx_height_m, frequency_mhz, 
                          rx_sensitivity_dbm)
