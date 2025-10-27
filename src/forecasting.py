# --- forecasting.py ---
# Description: Core functions for SARIMA modeling and forecasting.

import pmdarima as pm
from pmdarima import ARIMA
import pandas as pd


def calculate_pre_covid_level(df_ts, metric_name, year):
    """
    Calculates the average pre-COVID level from the given year.
    """
    try:
        pre_covid_data = df_ts.loc[f'{year}-01-01':f'{year}-12-31']

        if pre_covid_data.empty:
            print(f"Warning: No data found for baseline year {year}.")
            return None

        pre_covid_level = pre_covid_data[metric_name].mean()
        print(f"Calculated Pre-COVID Level (avg {year}): {pre_covid_level:,.0f}")
        return pre_covid_level

    except Exception as e:
        print(f"Error calculating pre-COVID level: {e}")
        return None


def run_sarima_forecast(df_ts, metric_name, n_periods, train_start_date, confidence_level):
    """
    Finds the best SARIMA model using auto_arima and returns the forecast.
    Trains *only* on data from train_start_date onwards.
    """

    print(f"\nFinding best SARIMA model using data from {train_start_date} onwards...")

    try:
        train_series = df_ts.loc[train_start_date:][metric_name]
        if train_series.empty:
            print(f"Error: No training data found after {train_start_date}.")
            return None, None

        print(f"Training data shape: {train_series.shape[0]} rows.")

    except Exception as e:
        print(f"Error selecting training data: {e}")
        return None, None

    try:
        # --- Automatically finding the best model ---
        print("Searching for best model (this may take a moment)...")

        # auto_arima will find the best (p,d,q) and (P,D,Q,m)
        auto_model = pm.auto_arima(
            train_series,
            start_p=1, start_q=1,
            max_p=3, max_q=3,  # Keep p and q low to prevent overfitting
            m=12,  # 12 months in a year
            seasonal=True,  # Yes, look for seasonality

            # --- THESE ARE THE NEW "GUARDRAIL" CONSTRAINTS ---
            d=1,  # FORCE d=1 (linear trend). Prevents the nosedive.
            with_intercept=True,  # FORCE a "drift" term. This models the steady upward recovery.
            D=0,  # FORCE D=0. Prevents unstable seasonal differencing.
            # --- End of new constraints ---

            trace=True,  # Print models as it finds them
            error_action='ignore',
            suppress_warnings=True,
            stepwise=True
        )

        # Note: auto_arima returns a *fitted* model,
        # so you do not need to call .fit() separately.

        print("\n--- Best Model Found ---")
        print(auto_model.summary())

        # --- End of new auto_arima section ---

    except Exception as e:
        print(f"Error during auto_arima model fitting: {e}")
        return None, None

    # Generate forecast
    print(f"\nGenerating forecast for {n_periods} months...")
    forecast, conf_int = auto_model.predict(
        n_periods=n_periods,
        return_conf_int=True,
        alpha=(1 - confidence_level)  # Note: auto_arima uses alpha, not 1-alpha
    )

    forecast_index = pd.date_range(
        start=train_series.index[-1] + pd.DateOffset(months=1),
        periods=n_periods,
        freq='MS'
    )

    forecast_df = pd.DataFrame(forecast, index=forecast_index, columns=['Forecast'])
    conf_int_df = pd.DataFrame(conf_int,
                               index=forecast_index,
                               columns=['Lower CI', 'Upper CI'])

    return forecast_df, conf_int_df


def find_recovery_date(df_ts, forecast_df, pre_covid_level, n_periods, metric_name):
    """
    Finds the first date the forecast crosses the pre-COVID level.
    """
    if pre_covid_level is None:
        return None

    recovery_dates = forecast_df[forecast_df['Forecast'] > pre_covid_level]

    if not recovery_dates.empty:
        recovery_date = recovery_dates.index[0]
        print(f"\n*** FORECAST ***")
        print(f"Model predicts ridership may return to pre-COVID levels by: {recovery_date.strftime('%B %Y')}")
        print(f"*** ***")
        return recovery_date
    else:
        historical_recovery = df_ts[df_ts[metric_name] > pre_covid_level]
        if not historical_recovery.empty:
            print(f"\n*** NOTE ***")
            print(
                f"Historical data already crossed the pre-COVID level (e.g., on {historical_recovery.index[-1].strftime('%B %Y')}).")
            print(f"The *forecast* does not predict a *sustained* return.")
            print(f"*** ***")
            return None

        print(f"\n*** FORECAST ***")
        print(f"Model does NOT predict a return to pre-COVID levels within the {n_periods}-month forecast.")
        print(f"*** ***")
        return None