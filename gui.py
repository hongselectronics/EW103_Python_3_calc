"""Simple GUI wrapper for EW103 calculator functions."""

import tkinter as tk
from tkinter import ttk, messagebox

from _2ray import two_ray_path_loss
from ADR import calculate_dynamic_ranges
from CEP_EEP import calculate_cep
from CEP_RMS import calculate_cep_from_rms
from DDR import calculate_dynamic_range
from EffRng import calculate_effective_range
from FZ import calculate_fresnel_zone_distance
from JtoS import calculate_jsr
from KED import knife_edge_diffraction_loss
from LOS import calculate_line_of_sight_loss
from NF import calculate_receiver_noise_figure
from PBJ import calculate_jamming_parameters
from RcvPwr import calculate_received_signal_power
from Sens import calculate_receiver_sensitivity


CALCULATORS = [
    {
        "name": "Line of Sight Loss",
        "fields": [
            ("distance_km", "Distance (km)", "10"),
            ("frequency_mhz", "Frequency (MHz)", "300"),
        ],
        "calculate": lambda v: calculate_line_of_sight_loss(v["distance_km"], v["frequency_mhz"]),
        "format_result": lambda r: f"Path loss: {r:.2f} dB",
    },
    {
        "name": "Two-Ray Path Loss",
        "fields": [
            ("link_distance_km", "Link distance (km)", "10"),
            ("tx_ant_height_m", "Tx antenna height (m)", "30"),
            ("rx_ant_height_m", "Rx antenna height (m)", "30"),
        ],
        "calculate": lambda v: two_ray_path_loss(
            v["link_distance_km"], v["tx_ant_height_m"], v["rx_ant_height_m"]
        ),
        "format_result": lambda r: f"Path loss: {r:.2f} dB",
    },
    {
        "name": "Knife Edge Diffraction",
        "fields": [
            ("dist_tx_to_knife_km", "Tx to knife (km)", "5"),
            ("dist_knife_to_rx_km", "Knife to Rx (km)", "5"),
            ("height_m", "Knife height vs LoS (m)", "-5"),
            ("frequency_mhz", "Frequency (MHz)", "900"),
        ],
        "calculate": lambda v: knife_edge_diffraction_loss(
            v["dist_tx_to_knife_km"],
            v["dist_knife_to_rx_km"],
            v["height_m"],
            v["frequency_mhz"],
        ),
        "format_result": lambda r: f"Diffraction loss: {r:.2f} dB",
    },
    {
        "name": "Fresnel Zone Distance",
        "fields": [
            ("tx_height_m", "Tx antenna height (m)", "30"),
            ("rx_height_m", "Rx antenna height (m)", "30"),
            ("frequency_mhz", "Frequency (MHz)", "2400"),
        ],
        "calculate": lambda v: calculate_fresnel_zone_distance(
            v["tx_height_m"], v["rx_height_m"], v["frequency_mhz"]
        ),
        "format_result": lambda r: f"Fresnel zone distance: {r:.2f} km",
    },
    {
        "name": "Receiver Sensitivity",
        "fields": [
            ("bandwidth_mhz", "Bandwidth (MHz)", "1"),
            ("noise_figure_db", "Noise figure (dB)", "5"),
            ("required_snr_db", "Required SNR (dB)", "10"),
        ],
        "calculate": lambda v: calculate_receiver_sensitivity(
            v["bandwidth_mhz"], v["noise_figure_db"], v["required_snr_db"]
        ),
        "format_result": lambda r: f"Sensitivity: {r:.2f} dBm",
    },
    {
        "name": "Receiver Noise Figure",
        "fields": [
            ("loss_before_preamplifier_db", "Loss before preamp (dB)", "1"),
            ("preamplifier_gain_db", "Preamplifier gain (dB)", "20"),
            ("preamplifier_noise_figure_db", "Preamplifier NF (dB)", "2"),
            (
                "loss_between_preamplifier_and_receiver_db",
                "Loss preamp to receiver (dB)",
                "1",
            ),
            ("receiver_noise_figure_db", "Receiver NF (dB)", "5"),
        ],
        "calculate": lambda v: calculate_receiver_noise_figure(
            v["loss_before_preamplifier_db"],
            v["preamplifier_gain_db"],
            v["preamplifier_noise_figure_db"],
            v["loss_between_preamplifier_and_receiver_db"],
            v["receiver_noise_figure_db"],
        ),
        "format_result": lambda r: f"System noise figure: {r:.2f} dB",
    },
    {
        "name": "Analog Receiver Dynamic Range",
        "fields": [
            ("sensitivity_dbm", "Sensitivity (dBm)", "-110"),
            ("gain_db", "Gain (dB)", "20"),
            ("ip2_dbm", "IP2 (dBm)", "-20"),
            ("ip3_dbm", "IP3 (dBm)", "-10"),
        ],
        "calculate": lambda v: calculate_dynamic_ranges(
            v["sensitivity_dbm"], v["gain_db"], v["ip2_dbm"], v["ip3_dbm"]
        ),
        "format_result": lambda r: f"SFDR2: {r[0]:.2f} dB\nSFDR3: {r[1]:.2f} dB",
    },
    {
        "name": "Digital Receiver Dynamic Range",
        "fields": [("bits", "Quantizing bits", "12")],
        "calculate": lambda v: calculate_dynamic_range(v["bits"]),
        "format_result": lambda r: f"Dynamic range: {r:.2f} dB",
    },
    {
        "name": "CEP from EEP",
        "fields": [
            ("long_axis_km", "Long axis (km)", "10"),
            ("short_axis_km", "Short axis (km)", "5"),
        ],
        "calculate": lambda v: calculate_cep(v["long_axis_km"], v["short_axis_km"]),
        "format_result": lambda r: f"CEP: {r:.3f} km",
    },
    {
        "name": "CEP from RMS",
        "fields": [
            ("rms_error_degrees", "RMS error (deg)", "5"),
            ("range_km", "Range (km)", "100"),
        ],
        "calculate": lambda v: calculate_cep_from_rms(v["rms_error_degrees"], v["range_km"]),
        "format_result": lambda r: f"CEP: {r:.3f} km",
    },
    {
        "name": "Communication J/S",
        "fields": [
            ("erp_desired_dBm", "ERP desired (dBm)", "50"),
            ("erp_jammer_dBm", "ERP jammer (dBm)", "60"),
            ("dist_jammer_receiver_km", "Jam to Rx distance (km)", "100"),
            ("dist_signal_receiver_km", "Sig to Rx distance (km)", "100"),
            ("tx_signal_height_m", "Tx signal height (m)", "30"),
            ("jammer_height_m", "Jammer height (m)", "30"),
            ("receiver_height_m", "Receiver height (m)", "30"),
            ("frequency_mhz", "Frequency (MHz)", "2400"),
            ("gain_toward_signal_dB", "Gain toward signal (dB)", "10"),
            ("gain_toward_jammer_dB", "Gain toward jammer (dB)", "10"),
        ],
        "calculate": lambda v: calculate_jsr(
            v["erp_desired_dBm"],
            v["erp_jammer_dBm"],
            v["dist_jammer_receiver_km"],
            v["dist_signal_receiver_km"],
            v["tx_signal_height_m"],
            v["jammer_height_m"],
            v["receiver_height_m"],
            v["frequency_mhz"],
            v["gain_toward_signal_dB"],
            v["gain_toward_jammer_dB"],
        ),
        "format_result": lambda r: (
            f"J/S: {r[0]:.2f} dB\n"
            f"J (jammer level): {r[1]:.2f} dB\n"
            f"S (signal level): {r[2]:.2f} dB\n"
            f"Jam FZ: {r[3]:.2f} km\n"
            f"Sig FZ: {r[4]:.2f} km"
        ),
    },
    {
        "name": "Partial Band Jamming",
        "fields": [
            ("info_bandwidth_khz", "Info bandwidth (kHz)", "25"),
            ("hopping_range_mhz", "Hopping range (MHz)", "100"),
            ("single_channel_js_db", "Single-channel J/S (dB)", "10"),
        ],
        "calculate": lambda v: calculate_jamming_parameters(
            v["info_bandwidth_khz"], v["hopping_range_mhz"], v["single_channel_js_db"]
        ),
        "format_result": lambda r: (
            f"Optimum jamming BW: {r[0]:.3f} MHz\n"
            f"Jamming duty cycle: {r[1]:.4f}"
        ),
    },
    {
        "name": "Received Power",
        "fields": [
            ("tx_power_dbm", "Tx power (dBm)", "30"),
            ("tx_gain_db", "Tx gain (dB)", "14"),
            ("rx_gain_db", "Rx gain (dB)", "14"),
            ("distance_km", "Link distance (km)", "5"),
            ("tx_height_m", "Tx height (m)", "30"),
            ("rx_height_m", "Rx height (m)", "30"),
            ("frequency_mhz", "Frequency (MHz)", "2400"),
        ],
        "calculate": lambda v: calculate_received_signal_power(
            v["tx_power_dbm"],
            v["tx_gain_db"],
            v["rx_gain_db"],
            v["distance_km"],
            v["tx_height_m"],
            v["rx_height_m"],
            v["frequency_mhz"],
        ),
        "format_result": lambda r: f"Received power: {r:.2f} dBm",
    },
    {
        "name": "Effective Range",
        "fields": [
            ("tx_power_dbm", "Tx power (dBm)", "30"),
            ("tx_gain_db", "Tx gain (dB)", "15"),
            ("rx_gain_db", "Rx gain (dB)", "15"),
            ("tx_height_m", "Tx height (m)", "30"),
            ("rx_height_m", "Rx height (m)", "30"),
            ("frequency_mhz", "Frequency (MHz)", "2400"),
            ("rx_sensitivity_dbm", "Rx sensitivity (dBm)", "-100"),
        ],
        "calculate": lambda v: calculate_effective_range(
            v["tx_power_dbm"],
            v["tx_gain_db"],
            v["rx_gain_db"],
            v["tx_height_m"],
            v["rx_height_m"],
            v["frequency_mhz"],
            v["rx_sensitivity_dbm"],
        ),
        "format_result": lambda r: (
            f"Two-ray distance: {r[0]:.2f} km\n"
            f"LOS distance: {r[1]:.2f} km\n"
            f"Fresnel zone: {r[2]:.2f} km\n"
            f"Effective range: {r[3]:.2f} km"
        ),
    },
]


def parse_inputs(field_entries):
    values = {}
    for key, entry in field_entries.items():
        raw_value = entry.get()
        try:
            values[key] = float(raw_value)
        except ValueError as exc:
            messagebox.showerror(
                "Input error",
                f"Could not parse '{raw_value}' for {entry.label_text}. Please enter a number.\n\n{exc}",
            )
            return None
    return values


def build_calculator_tab(notebook, calculator):
    frame = ttk.Frame(notebook, padding=12)
    frame.columnconfigure(1, weight=1)

    field_entries = {}
    for row_index, (_, label_text, default) in enumerate(calculator["fields"]):
        label = ttk.Label(frame, text=label_text)
        label.grid(row=row_index, column=0, sticky=tk.W, pady=2)

        entry = ttk.Entry(frame)
        entry.insert(0, default)
        entry.grid(row=row_index, column=1, sticky=tk.EW, pady=2)

        # Store the label text on the widget for friendly error messages
        entry.label_text = label_text
        field_entries[calculator["fields"][row_index][0]] = entry

    result_var = tk.StringVar(value="Enter values and press Calculate.")
    result_label = ttk.Label(frame, textvariable=result_var, justify=tk.LEFT)
    result_label.grid(row=len(calculator["fields"]) + 1, column=0, columnspan=2, sticky=tk.W, pady=(8, 0))

    def on_calculate():
        values = parse_inputs(field_entries)
        if values is None:
            return
        result = calculator["calculate"](values)
        result_var.set(calculator["format_result"](result))

    button = ttk.Button(frame, text="Calculate", command=on_calculate)
    button.grid(row=len(calculator["fields"]), column=0, columnspan=2, pady=(8, 0))

    notebook.add(frame, text=calculator["name"])


def main():
    root = tk.Tk()
    root.title("EW103 Calculators")

    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

    for calc in CALCULATORS:
        build_calculator_tab(notebook, calc)

    root.mainloop()


if __name__ == "__main__":
    main()
