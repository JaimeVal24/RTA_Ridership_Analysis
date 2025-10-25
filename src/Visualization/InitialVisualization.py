import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import matplotlib.dates as mdates
import os

try:
    # Load the full dataset from the CSV file
    df = pd.read_csv('Monthly_Modal_Time_Series.csv')
except FileNotFoundError:
    print("Error: Make sure 'Monthly_Modal_Time_Series.csv' is in the same folder as this script.")
    exit()

df_agency = df[df['Agency'] == 'Riverside Transit Agency'].copy()

# Create a proper 'Date' column by combining 'Year' and 'Month'
df_agency['Date'] = pd.to_datetime(df_agency['Year'].astype(str) + '-' + df_agency['Month'].astype(str),
                                   errors='coerce')

# Drop any rows where the date could not be created
df_agency.dropna(subset=['Date'], inplace=True)

unique_modes = df_agency['Mode'].unique()
print(f"Found modes for Riverside Transit Agency: {unique_modes}")

metrics_to_plot = ['Vehicle Revenue Miles', 'Unlinked Passenger Trips', 'VOMS']

for mode in unique_modes:
    print(f"\n{'=' * 20} Processing Mode: {mode} {'=' * 20}")

    # Filter the data for the current mode just once
    df_mode = df_agency[df_agency['Mode'] == mode]

    # The inner loop processes each metric for the current mode
    for metric in metrics_to_plot:
        print(f"\n--- Analyzing Metric: {metric} ---")

        df_monthly = df_mode.groupby('Date')[metric].sum().reset_index()

        print(f"Aggregated Monthly Data Table for {mode} - {metric}:")
        print(tabulate(df_monthly, headers='keys', tablefmt='psql', showindex=False))

        safe_metric_name = metric.replace(' ', '_').replace('(', '').replace(')', '')
        output_filename = f'riverside_transit_{mode}_{safe_metric_name}_plot.png'

        if os.path.exists(output_filename):
            print(f"Plot '{output_filename}' already exists. Skipping.")
        else:
            print(f"Generating plot...")
            fig, ax = plt.subplots(figsize=(14, 8))
            ax.plot(df_monthly['Date'], df_monthly[metric], marker='o', linestyle='-', markersize=5)

            ax.set_title(f'Monthly {metric} for Riverside Transit Agency ({mode})', fontsize=16)
            ax.set_xlabel('Date', fontsize=12)
            ax.set_ylabel(f'Total {metric}', fontsize=12)
            ax.grid(True, which='both', linestyle='--', linewidth=0.5)

            ax.xaxis.set_major_locator(mdates.YearLocator())
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
            plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

            fig.tight_layout()

            plt.savefig(output_filename)
            print(f"Plot saved as '{output_filename}'")
            plt.close(fig)

