# --- plotting.py ---
# Description: Functions for generating and saving plots.

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
from tabulate import tabulate


def plot_forecast(df_ts, forecast_df, conf_int_df, pre_covid_level,
                  recovery_date, mode, metric, output_dir, baseline_year):
    """
    Generates and saves the main forecast plot.
    """
    print("Generating forecast plot...")
    fig, ax = plt.subplots(figsize=(15, 8))

    # Plot historical data
    ax.plot(df_ts.index, df_ts[metric], label='Historical Data', color='blue')

    # Plot forecast
    ax.plot(forecast_df.index, forecast_df['Forecast'], label='Forecast', color='red', linestyle='--')

    # Plot confidence interval
    ax.fill_between(
        conf_int_df.index,
        conf_int_df['Lower CI'],
        conf_int_df['Upper CI'],
        color='red', alpha=0.1, label='95% Confidence Interval'
    )

    # Plot Pre-COVID Level
    if pre_covid_level is not None:
        ax.axhline(
            y=pre_covid_level,
            color='green',
            linestyle='--',
            label=f'Pre-COVID Level ({baseline_year} Avg): {pre_covid_level:,.0f}'
        )

    # Plot Recovery Date
    if recovery_date is not None:
        ax.axvline(
            x=recovery_date,
            color='purple',
            linestyle=':',
            label=f'Est. Recovery: {recovery_date.strftime("%Y-%m")}'
        )

    ax.set_title(f'Ridership Forecast for RTA ({mode}) - {metric}', fontsize=16)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel(metric, fontsize=12)
    ax.legend()
    ax.grid(True)

    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    fig.tight_layout()

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    safe_metric = metric.replace(' ', '_')
    output_filename = os.path.join(output_dir, f'RTA_{mode}_{safe_metric}_FORECAST.png')
    plt.savefig(output_filename)
    print(f"Forecast plot saved as '{output_filename}'")
    plt.close(fig)


def generate_secondary_plots(df_agency, metrics_to_plot, output_dir):
    """
    Generates the original summary plots for other metrics.
    """
    print("\n--- Generating plots for other metrics ---")
    unique_modes = df_agency['Mode'].unique()

    for mode in unique_modes:
        print(f"\n{'=' * 20} Processing Mode: {mode} {'=' * 20}")
        df_mode_loop = df_agency[df_agency['Mode'] == mode]

        for metric in metrics_to_plot:
            print(f"\n--- Analyzing Metric: {metric} ---")
            df_monthly = df_mode_loop.groupby('Date')[metric].sum().reset_index()

            if df_monthly.empty:
                print(f"No data for {mode} - {metric}. Skipping plot.")
                continue

            print(f"Aggregated Monthly Data Table for {mode} - {metric}:")
            print(tabulate(df_monthly.tail(), headers='keys', tablefmt='psql', showindex=False))

            safe_metric = metric.replace(' ', '_').replace('(', '').replace(')', '')
            output_filename = os.path.join(output_dir, f'RTA_{mode}_{safe_metric}_plot.png')

            if os.path.exists(output_filename):
                print(f"Plot '{output_filename}' already exists. Skipping.")
            else:
                print(f"Generating plot...")
                fig, ax = plt.subplots(figsize=(14, 8))
                ax.plot(df_monthly['Date'], df_monthly[metric], marker='o', linestyle='-', markersize=5)
                ax.set_title(f'Monthly {metric} for RTA ({mode})', fontsize=16)
                ax.set_xlabel('Date', fontsize=12)
                ax.set_ylabel(f'Total {metric}', fontsize=12)
                ax.grid(True, which='both', linestyle='--', linewidth=0.5)
                ax.xaxis.set_major_locator(mdates.YearLocator())
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
                plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
                fig.tight_layout()

                # Create output directory if it doesn't exist
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                plt.savefig(output_filename)
                print(f"Plot saved as '{output_filename}'")
                plt.close(fig)