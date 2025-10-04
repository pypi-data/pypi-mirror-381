"""Definitions used in data processing."""

import polars as pl

# Dictionary mapping Status integer to string
state_dict = {
    1: "CC_Chg",
    2: "CC_DChg",
    3: "CV_Chg",
    4: "Rest",
    5: "cycle_count",
    7: "CCCV_Chg",
    8: "CP_DChg",
    9: "CP_Chg",
    10: "CR_DChg",
    13: "Pause",
    16: "Pulse",
    17: "SIM",
    19: "CV_DChg",
    20: "CCCV_DChg",
    21: "Control",
    22: "OCV",
    26: "CPCV_DChg",
    27: "CPCV_Chg",
}

# Define fields and their data types (not aux)
dtype_dict = {
    "index": pl.UInt32,
    "voltage_V": pl.Float32,
    "current_mA": pl.Float32,
    "unix_time_s": pl.Float64,
    "step_time_s": pl.Float64,
    "timestamp": pl.Datetime("us", time_zone="UTC"),
    "cycle_count": pl.UInt32,
    "step_count": pl.UInt32,
    "step_index": pl.UInt32,
    "status": pl.Enum(state_dict.values()),
    "capacity_mAh": pl.Float32,
    "energy_mWh": pl.Float32,
}


# Define field scaling based on instrument Range setting
multiplier_dict = {
    -100000000: 1e1,
    -200000: 1e-2,
    -100000: 1e-2,
    -60000: 1e-2,
    -30000: 1e-2,
    -50000: 1e-2,
    -40000: 1e-2,
    -20000: 1e-2,
    -12000: 1e-2,
    -10000: 1e-2,
    -6000: 1e-2,
    -5000: 1e-2,
    -3000: 1e-2,
    -2000: 1e-2,
    -1000: 1e-2,
    -500: 1e-3,
    -100: 1e-3,
    -50: 1e-4,
    -25: 1e-4,
    -20: 1e-4,
    -10: 1e-4,
    -5: 1e-5,
    -2: 1e-5,
    -1: 1e-5,
    0: 0.0,
    1: 1e-4,
    2: 1e-4,
    5: 1e-4,
    10: 1e-3,
    20: 1e-3,
    25: 1e-3,
    50: 1e-3,
    100: 1e-2,
    200: 1e-2,
    250: 1e-2,
    500: 1e-2,
    1000: 1e-1,
    6000: 1e-1,
    10000: 1e-1,
    12000: 1e-1,
    20000: 1e-1,
    30000: 1e-1,
    40000: 1e-1,
    50000: 1e-1,
    60000: 1e-1,
    100000: 1e-1,
    200000: 1e-1,
}

# Renaming aux columns by ChlType
aux_chl_type_columns = {
    103: "temperature_degC",
    335: "temperature_setpoint_degC",
    345: "humidity_%",
}
