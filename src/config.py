# --- config.py ---
# Description: Configuration file for the forecast project.

# --- File Paths ---
DATA_FILE = 'Monthly_Modal_Time_Series.csv'
OUTPUT_DIR = 'plots'

# --- Analysis Parameters ---
AGENCY_NAME = 'Riverside Transit Agency'
MODE_TO_ANALYZE = 'MB'  # 'MB' (Motorbus), 'CB' (Commuter Bus), 'DR' (Demand Response)
METRIC_TO_ANALYZE = 'Unlinked Passenger Trips'
PRE_COVID_YEAR = 2019

# --- Model & Forecast Parameters ---
FORECAST_PERIOD = 90
CONFIDENCE_LEVEL = 0.05

# --- Secondary Plot Parameters ---
# Metrics to plot in the original analysis loop
SECONDARY_METRICS = ['Vehicle Revenue Miles', 'VOMS']