# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 03:52:27 2024

@author: Jeremy Hong
"""

# Function to calculate the Fresnel Zone distance
def calculate_fresnel_zone_distance(tx_height_m, rx_height_m, frequency_mhz):
    # Calculate the Fresnel Zone distance in km
    fz_distance_km = (tx_height_m * rx_height_m * frequency_mhz) / 24000
    return fz_distance_km

# Example usage:
tx_height_m = 30    # replace with user input
rx_height_m = 30    # replace with user input
frequency_mhz = 2400 # replace with user input (example: 2.4 GHz)

# Calculate Fresnel zone distance
fresnel_zone_distance = calculate_fresnel_zone_distance(tx_height_m, rx_height_m, frequency_mhz)
fresnel_zone_distance
