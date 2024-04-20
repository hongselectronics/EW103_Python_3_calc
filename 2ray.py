# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 03:35:19 2024

@author: Jeremy Hong
"""

import numpy as np

# Function to calculate two-ray path loss
def two_ray_path_loss(link_distance_km, tx_ant_height_m, rx_ant_height_m):
    # Convert distances to float for log calculation
    link_distance_km = float(link_distance_km)
    tx_ant_height_m = float(tx_ant_height_m)
    rx_ant_height_m = float(rx_ant_height_m)
    
    # Calculate the two-ray path loss
    path_loss_db = 120 + 40 * np.log10(link_distance_km) - 20 * np.log10(tx_ant_height_m) - 20 * np.log10(rx_ant_height_m)
    
    return path_loss_db

# Example usage:
link_distance_km = 5  # replace with user input
tx_ant_height_m = 10  # replace with user input
rx_ant_height_m = 10  # replace with user input

two_ray_path_loss(link_distance_km, tx_ant_height_m, rx_ant_height_m)
