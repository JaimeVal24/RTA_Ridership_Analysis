# --- main.py ---
# Description: Main entry point for the RTA forecast analysis.

import config as cfg
import data_loader as dl
import forecasting as fc
import plotting as pl
import sys


def main():
    print("=== Starting RTA Ridership Forecast Analysis ===")

    # 1. Load and Prepare Data
    df_agency = dl.load_and_prepare_data(cfg.DATA_FILE, cfg.AGENCY_NAME)
    if df_agency is None:
        sys.exit("Failed to load data. Exiting.")

    # 2. Get the specific time series for forecasting
    df_ts = dl.get_timeseries(df_agency, cfg.MODE_TO_ANALYZE, cfg.METRIC_TO_ANALYZE)
    if df_ts is None:
        sys.exit("Failed to create time series. Exiting.")

    # 3. Calculate Pre-COVID Baseline
    pre_covid_level = fc.calculate_pre_covid_level(df_ts, cfg.METRIC_TO_ANALYZE, cfg.PRE_COVID_YEAR)

    # 4. Run SARIMA Forecast
    forecast_df, conf_int_df = fc.run_sarima_forecast(
        df_ts,
        cfg.METRIC_TO_ANALYZE,
        cfg.FORECAST_PERIOD,
        cfg.CONFIDENCE_LEVEL
    )

    # 5. Find Recovery Date
    recovery_date = fc.find_recovery_date(forecast_df, pre_covid_level, cfg.FORECAST_PERIOD)

    # 6. Plot Forecast
    pl.plot_forecast(
        df_ts,
        forecast_df,
        conf_int_df,
        pre_covid_level,
        recovery_date,
        cfg.MODE_TO_ANALYZE,
        cfg.METRIC_TO_ANALYZE,
        cfg.OUTPUT_DIR,
        cfg.PRE_COVID_YEAR
    )

    # 7. Generate Secondary Plots
    pl.generate_secondary_plots(df_agency, cfg.SECONDARY_METRICS, cfg.OUTPUT_DIR)

    print("\n=== Analysis Complete ===")


if __name__ == "__main__":
    main()