"""
Script 2: Data Processing

Loads ESG data, analyzes missing values, and performs interpolation.

Usage:
    python scripts/02_data_processing.py
"""

import sys
import os
import pandas as pd

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.data_processor import DataProcessor
from src.interpolation import InterpolationHandler
from src import config


def main():
    """Process and clean ESG data."""
    
    print("\n" + "="*70)
    print("STEP 2: DATA PROCESSING & INTERPOLATION")
    print("="*70)
    
    # Load data
    print("\nLoading data...")
    if os.path.exists(config.PATHS['sample_data']):
        df = pd.read_csv(config.PATHS['sample_data'])
        print(f"✓ Data loaded from: {config.PATHS['sample_data']}")
    else:
        print("❌ Data file not found. Run 01_data_generation.py first.")
        return None
    
    # Create processor
    processor = DataProcessor(df)
    
    # Analyze missing values
    print("\n" + "-"*70)
    missing_info = processor.analyze_missing_values()
    
    # Data quality report
    print("\n" + "-"*70)
    quality_report = processor.get_data_quality_report()
    
    # Handle missing values
    print("\n" + "-"*70)
    df_processed = processor.handle_missing_values(
        method=config.INTERPOLATION['method']
    )
    
    # Summary statistics
    print("\n" + "-"*70)
    summary = processor.get_summary_statistics()
    
    # Before/after comparison
    print("\n" + "-"*70)
    comparison = processor.compare_before_after()
    
    # Save processed data
    os.makedirs(config.PATHS['data_processed'], exist_ok=True)
    output_path = os.path.join(config.PATHS['data_processed'], 'processed_esg_data.csv')
    df_processed.to_csv(output_path, index=False)
    print(f"\n✓ Processed data saved to: {output_path}")
    
    return df_processed


if __name__ == "__main__":
    try:
        df = main()
        print("\n✓ Data processing completed successfully!")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
