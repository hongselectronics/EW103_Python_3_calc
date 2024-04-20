# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 04:05:26 2024

@author: Jeremy Hong
"""

# Function to calculate the optimum jamming bandwidth and jamming duty cycle
def calculate_jamming_parameters(info_bandwidth_khz, hopping_range_mhz, single_channel_js_db):
    # Calculate the optimum jamming bandwidth in MHz
    optimum_jamming_bandwidth_mhz = (10 ** (single_channel_js_db / 10)) * (info_bandwidth_khz / 1000)
    
    # Calculate the jamming duty cycle
    jamming_duty_cycle = optimum_jamming_bandwidth_mhz / hopping_range_mhz
    
    return optimum_jamming_bandwidth_mhz, jamming_duty_cycle

# Example usage with placeholders for input values
info_bandwidth_khz = 1               # replace with actual value
hopping_range_mhz = 1                # replace with actual value
single_channel_js_db = 1             # replace with actual value

# Calculate optimum jamming bandwidth and jamming duty cycle
optimum_jamming_bandwidth_mhz, jamming_duty_cycle = calculate_jamming_parameters(info_bandwidth_khz, 
                                                                                  hopping_range_mhz, 
                                                                                  single_channel_js_db)
optimum_jamming_bandwidth_mhz, jamming_duty_cycle
