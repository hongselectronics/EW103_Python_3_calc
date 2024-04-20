# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 03:53:45 2024

@author: Jeremy Hong
"""

import numpy as np

# Function to calculate Jamming to Signal Ratio (JSR) for communication jamming
def calculate_jsr(erp_desired_dBm, erp_jammer_dBm, 
                  dist_jammer_receiver_km, dist_signal_receiver_km, 
                  tx_signal_height_m, jammer_height_m, receiver_height_m, 
                  frequency_mhz, gain_toward_signal_dB, gain_toward_jammer_dB):
    
    # Calculate Fresnel Zones for Jammer and Desired Signal
    jam_fz = jammer_height_m * receiver_height_m * frequency_mhz / 24000
    des_fz = tx_signal_height_m * receiver_height_m * frequency_mhz / 24000
    
    # Calculate J (jammer) using conditional logic based on Jam FZ
    if dist_jammer_receiver_km > jam_fz:
        J = erp_jammer_dBm - 120 - 40 * np.log10(dist_jammer_receiver_km) + 20 * np.log10(receiver_height_m) + 20 * np.log10(jammer_height_m) + gain_toward_jammer_dB
    else:
        J = erp_jammer_dBm - 32.44 - 20 * np.log10(frequency_mhz) - 20 * np.log10(dist_jammer_receiver_km) + gain_toward_jammer_dB
    
    # Calculate S (desired signal) using conditional logic based on Des FZ
    if dist_signal_receiver_km > des_fz:
        S = erp_desired_dBm - 120 - 40 * np.log10(dist_signal_receiver_km) + 20 * np.log10(receiver_height_m) + 20 * np.log10(tx_signal_height_m) + gain_toward_signal_dB
    else:
        S = erp_desired_dBm - 32.44 - 20 * np.log10(frequency_mhz) - 20 * np.log10(dist_signal_receiver_km) + gain_toward_signal_dB
    
    # Calculate JSR
    JSR = J - S
    
    return JSR, J, S, jam_fz, des_fz

# Example usage:
erp_desired_dBm = 50               # replace with user input
erp_jammer_dBm = 60                # replace with user input
dist_jammer_receiver_km = 100      # replace with user input
dist_signal_receiver_km = 100      # replace with user input
tx_signal_height_m = 30            # replace with user input
jammer_height_m = 30               # replace with user input
receiver_height_m = 30             # replace with user input
frequency_mhz = 2400               # replace with user input (example: 2.4 GHz)
gain_toward_signal_dB = 10         # replace with user input
gain_toward_jammer_dB = 10         # replace with user input

# Calculate JSR
calculate_jsr(erp_desired_dBm, erp_jammer_dBm, 
              dist_jammer_receiver_km, dist_signal_receiver_km, 
              tx_signal_height_m, jammer_height_m, receiver_height_m, 
              frequency_mhz, gain_toward_signal_dB, gain_toward_jammer_dB)
