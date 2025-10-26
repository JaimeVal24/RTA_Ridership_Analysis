# --- data_loader.py ---
# Description: Functions for loading and preparing time series data.

import pandas as pd
from tabulate import tabulate


def load_and_prepare_data(file_path, agency_name):
    """
    Loads the CSV, filters for the specified agency,
    and converts date columns.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: Data file not found at '{file_path}'")
        return None

    df_agency = df[df['Agency'] == agency_name].copy()

    if df_agency.empty:
        print(f"Error: No data found for agency '{agency_name}'")
        return None

    df_agency['Date'] = pd.to_datetime(
        df_agency['Year'].astype(str) + '-' + df_agency['Month'].astype(str),
        errors='coerce'
    )

    df_agency.dropna(subset=['Date'], inplace=True)

    print(f"Successfully loaded data for {agency_name}.")
    return df_agency


def get_timeseries(df_agency, mode, metric):
    """
    Filters the agency data for a specific mode and metric,
    then returns a clean, indexed time series.
    """
    df_mode = df_agency[
        (df_agency['Mode'] == mode) &
        (df_agency[metric].notna())
        ].copy()

    if df_mode.empty:
        print(f"Error: No data found for Mode '{mode}' and Metric '{metric}'.")
        return None

    df_ts = df_mode.groupby('Date')[metric].sum().reset_index()
    df_ts = df_ts.set_index('Date')
    df_ts.index.freq = 'MS'  # 'MS' = Month Start frequency

    print(f"Time Series Data (last 5 rows for {mode} - {metric}):")
    print(tabulate(df_ts.tail(), headers='keys', tablefmt='psql'))

    return df_ts