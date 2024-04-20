# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 03:40:03 2024

@author: Jeremy Hong
"""

# Function to calculate second and third order spurious free dynamic range
def calculate_dynamic_ranges(sensitivity_dbm, gain_db, ip2_dbm, ip3_dbm):
    # Calculate second order spurious free dynamic range
    sfdr2 = (ip2_dbm - sensitivity_dbm - gain_db) / 2
    
    # Calculate third order spurious free dynamic range
    sfdr3 = 2 * (ip3_dbm - sensitivity_dbm - gain_db) / 3
    
    return sfdr2, sfdr3

# Example usage:
sensitivity_dbm = -120  # replace with user input
gain_db = 10            # replace with user input
ip2_dbm = -30           # replace with user input
ip3_dbm = -40           # replace with user input

calculate_dynamic_ranges(sensitivity_dbm, gain_db, ip2_dbm, ip3_dbm)
