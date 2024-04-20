# Equations for Radio Communication Analysis

## Line of Sight Loss -- One Way Link Equation
$$
\[ \text{LOS Loss (dB)} = 32.44 + 20 \cdot \log_{10}(\text{distance in km}) + 20 \cdot \log_{10}(\text{frequency in MHz}) \]
$$
## Two-ray Loss -- One Way Link Equation
$$
\[ \text{2-Ray Loss (dB)} = 120 + 40 \cdot \log_{10}(\text{distance in km}) - 20 \cdot \log_{10}(\text{Tx height in m}) - 20 \cdot \log_{10}(\text{Rx height in m}) \]
$$
## Knife Edge Diffraction Loss
$$
\[ \text{Diffraction Loss (dB)} = \text{Dependent on the diffraction parameter 'v'} \]
$$
## Fresnel Zone Distance
$$
\[ \text{Fresnel Zone Distance (km)} = \frac{\text{Tx antenna height (m)} \times \text{Rx antenna height (m)} \times \text{frequency (MHz)}}{24000} \]
$$
## Receiver Sensitivity
$$
\[ \text{Sensitivity (dBm)} = -114 + 10 \cdot \log_{10}(\text{bandwidth in MHz}) + \text{Noise Figure (dB)} + \text{Required SNR (dB)} \]
$$
## Receiver System Noise Figure
$$
\[ \text{Noise Figure (dB)} = \text{Function of various noise sources and gains} \]
$$
## Analog Receiver Dynamic Range
$$
\[ \text{SFDR (dB)} = \text{Function of intercept points and gains} \]
$$
## Digital Receiver Dynamic Range
$$
\[ \text{Dynamic Range (dB)} = 6.02 \times \text{number of quantizing bits} + 1.76 \text{ dB} \]
$$
## CEP from RMS Error
$$
\[ \text{CEP (km)} = \text{Function of RMS error and other parameters} \]
$$
## CEP from EEP
$$
\[ \text{CEP (km)} = 0.75 \cdot \sqrt{\left(\frac{\text{long axis (km)}}{2}\right)^2 + \left(\frac{\text{short axis (km)}}{2}\right)^2} \]
$$
## Communication J/S
$$
\[ \text{J/S (dB)} = \text{Jamming Power (dB)} - \text{Signal Power (dB)} \]
$$
## Frequency Spread for Partial Band Jamming
$$
\[ \text{Optimum Jamming Bandwidth (MHz)} = \text{Function of J/S and signal bandwidth} \]
$$
## Received Power in One Way Link
$$
\[ \text{Received Power (dBm)} = \text{Tx Power (dBm)} + \text{Tx Gain (dB)} + \text{Rx Gain (dB)} - \text{Loss (dB)} \]
$$
## Effective Range in One Way Link
$$
\[ \text{Effective Range (km)} = \text{Max of LOS or 2-Ray Distance} \]
$$
