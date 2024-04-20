# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 04:00:49 2024

@author: Jeremy Hong
"""
from scipy.constants import speed_of_light
import numpy as np

# Function to calculate the knife-edge diffraction loss
def knife_edge_diffraction_loss(dist_tx_to_knife_km, dist_knife_to_rx_km, height_m, frequency_mhz):
    # Calculate the wavelength (lambda)
    wavelength_m = speed_of_light / (frequency_mhz * 1e6)

    # Calculate the diffraction parameter v
    v = height_m * np.sqrt(2 * (dist_tx_to_knife_km + dist_knife_to_rx_km) / (wavelength_m * dist_tx_to_knife_km * dist_knife_to_rx_km))

    # Calculate Gd based on the value of v
    if v > 1:
        Gd = 0
    elif 0 < v <= 1:
        Gd = 20 * np.log10(0.5 + (0.62 * v))
    elif -1 <= v < 0:
        Gd = 20 * np.log10(0.5 * np.exp(0.95 * v))
    elif -2.4 < v < -1:
        if v < -0.1:
            Gd = 20 * np.log10(0.4 - np.sqrt(0.1184 - (0.1 * v + 0.38)**2))
        else:
            Gd = 0
    elif v <= -2.4:
        Gd = 20 * np.log10(-0.225 / v)
    else:
        Gd = 0  # Handle the case when v equals exactly 0

    # Diffraction loss in dB is the negative of Gd
    diffraction_loss_dB = -Gd

    return diffraction_loss_dB

# Example usage with values replaced by '1' just as placeholders
dist_tx_to_knife_km = 1  # replace with actual value
dist_knife_to_rx_km = 1  # replace with actual value
height_m = 1             # replace with actual value (negative if the ridge line is above the line of sight)
frequency_mhz = 1        # replace with actual value

# Calculate knife-edge diffraction loss
knife_edge_diffraction_loss(dist_tx_to_knife_km, dist_knife_to_rx_km, height_m, frequency_mhz)

