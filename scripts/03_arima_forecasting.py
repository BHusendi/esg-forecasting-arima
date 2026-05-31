"""
Script 3: ARIMA Forecasting

Fits ARIMA model to ESG data and generates forecasts.

Usage:
    python scripts/03_arima_forecasting.py
"""

import sys
import os
import pandas as pd

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.arima_model import ARIMAForecaster
from src.diagnostics import ModelDiagnostics
from src import config


def main():
    """Fit ARIMA model and generate forecast."""
    
    print("\n" + "="*70)
    print("STEP 3: ARIMA MODELING & FORECASTING")
    print("="*70)
    
    # Load processed data
    print("\nLoading processed data...")
    processed_path = os.path.join(config.PATHS['data_processed'], 'processed_esg_data.csv')
    
    if os.path.exists(processed_path):
        df = pd.read_csv(processed_path)
        print(f"✓ Data loaded from: {processed_path}")
    else:
        print("❌ Processed data not found. Run 02_data_processing.py first.")
        return None
    
    # Use Environmental parameter for forecasting
    series = df['Environmental']
    
    # Create forecaster
    print("\n" + "-"*70)
    print("Creating ARIMA forecaster...")
    forecaster = ARIMAForecaster(series, name='Environmental')
    
    # Test stationarity
    print("\n" + "-"*70)
    stationarity = forecaster.test_stationarity(verbose=True)
    
    # Auto-fit ARIMA parameters
    print("\n" + "-"*70)
    print("Auto-fitting ARIMA parameters...")
    order = forecaster.auto_fit(verbose=True)
    
    # Fit model
    print("\n" + "-"*70)
    print("Fitting ARIMA model...")
    forecaster.fit_arima(verbose=True)
    
    # Model diagnostics
    print("\n" + "-"*70)
    print("Running model diagnostics...")
    diagnostics = ModelDiagnostics(forecaster.results, series)
    diagnostics.run_all_diagnostics(verbose=True)
    
    # Forecast
    print("\n" + "-"*70)
    print("Generating forecast...")
    forecast_result = forecaster.forecast(
        steps=config.FORECASTING['forecast_periods'],
        confidence=config.FORECASTING['confidence_level']
    )
    
    # Save forecast results
    os.makedirs(config.PATHS['reports'], exist_ok=True)
    forecast_df = forecast_result['forecast_df'].copy()
    forecast_path = os.path.join(config.PATHS['reports'], 'forecast_environmental.csv')
    forecast_df.to_csv(forecast_path)
    print(f"\n✓ Forecast saved to: {forecast_path}")
    
    return {
        'forecaster': forecaster,
        'diagnostics': diagnostics,
        'forecast': forecast_result,
        'series': series
    }


if __name__ == "__main__":
    try:
        results = main()
        print("\n✓ ARIMA forecasting completed successfully!")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
