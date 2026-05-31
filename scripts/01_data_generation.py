"""
Script 1: Data Generation

Generates synthetic ESG (Environmental, Social, Governance) data
and saves it to CSV file.

Usage:
    python scripts/01_data_generation.py
"""

import sys
import os
from datetime import datetime

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.data_generator import ESGDataGenerator
from src import config


def main():
    """Generate synthetic ESG data."""
    
    print("\n" + "="*70)
    print("STEP 1: SYNTHETIC ESG DATA GENERATION")
    print("="*70)
    
    # Create data directory
    os.makedirs(config.PATHS['data_raw'], exist_ok=True)
    
    # Generate data
    generator = ESGDataGenerator(
        n_periods=config.DATA_GENERATION['n_periods'],
        start_date=config.DATA_GENERATION['start_date'],
        missing_rate=config.DATA_GENERATION['missing_rate'],
        seed=config.DATA_GENERATION['seed']
    )
    
    df = generator.generate()
    
    # Save to CSV
    df.to_csv(config.PATHS['sample_data'], index=False)
    
    print(f"\n✓ Data saved to: {config.PATHS['sample_data']}")
    print(f"\nDataFrame Summary:")
    print(f"  Rows: {len(df)}")
    print(f"  Columns: {list(df.columns)}")
    print(f"  Date Range: {df['Date'].min().date()} to {df['Date'].max().date()}")
    print(f"  Missing Values: {df.isnull().sum().sum()}")
    
    return df


if __name__ == "__main__":
    try:
        main()
        print("\n✓ Data generation completed successfully!")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
