# --- forecasting.py ---
# Description: Core functions for SARIMA modeling and forecasting.

import pmdarima as pm
import pandas as pd


def calculate_pre_covid_level(df_ts, metric_name, year):
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


def run_sarima_forecast(df_ts, metric_name, n_periods, confidence_level):
    """
    Uses auto_arima to fit a SARIMA model
    """
    print("\nFinding best SARIMA model using auto_arima...")
    auto_model = pm.auto_arima(
        df_ts[metric_name],
        start_p=1, start_q=1,
        test='adf',  # Use ADF test to find 'd'
        max_p=3, max_q=3,
        m=12,  # 12 months in a year
        start_P=0,
        seasonal=True,  # Account for seasonality
        d=None,  # Let the test find 'd'
        D=1,  # Default seasonal differencing
        trace=True,
        error_action='ignore',
        suppress_warnings=True,
        stepwise=True
    )

    print("\n--- Model Summary ---")
    print(auto_model.summary())

    print(f"\nGenerating forecast for {n_periods} months...")
    forecast, conf_int = auto_model.predict(
        n_periods=n_periods,
        return_conf_int=True,
        alpha=confidence_level
    )

    # Create a date range for the forecast
    forecast_index = pd.date_range(
        start=df_ts.index[-1] + pd.DateOffset(months=1),
        periods=n_periods,
        freq='MS'
    )

    # Combine forecast and confidence intervals into DataFrames
    forecast_df = pd.DataFrame(forecast, index=forecast_index, columns=['Forecast'])
    conf_int_df = pd.DataFrame(conf_int,
                               index=forecast_index,
                               columns=['Lower CI', 'Upper CI'])

    return forecast_df, conf_int_df


def find_recovery_date(forecast_df, pre_covid_level, n_periods):
    """
    Finds the first date the forecast crosses the pre-COVID level.
    """
    if pre_covid_level is None:
        return None

    # Find all dates where the forecast is *above* the target
    recovery_dates = forecast_df[forecast_df['Forecast'] > pre_covid_level]

    if not recovery_dates.empty:
        recovery_date = recovery_dates.index[0]
        print(f"\n*** FORECAST ***")
        print(f"Model predicts ridership may return to pre-COVID levels by: {recovery_date.strftime('%B %Y')}")
        print(f"*** ***")
        return recovery_date
    else:
        print(f"\n*** FORECAST ***")
        print(f"Model does NOT predict a return to pre-COVID levels within the next {n_periods} months.")
        print(f"*** ***")
        return None