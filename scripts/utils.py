"""
Utility Functions

Helper functions for ESG forecasting scripts.
"""

import os
import pandas as pd
from datetime import datetime


def create_output_directories():
    """Create necessary output directories."""
    dirs = [
        'data/raw',
        'data/processed',
        'outputs/reports',
        'outputs/visualizations'
    ]
    
    for directory in dirs:
        os.makedirs(directory, exist_ok=True)
        print(f"✓ Created/verified directory: {directory}")


def load_esg_data(filepath):
    """
    Load ESG data from CSV file.
    
    Parameters
    ----------
    filepath : str
        Path to CSV file
    
    Returns
    -------
    pd.DataFrame
        Loaded ESG data
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Data file not found: {filepath}")
    
    df = pd.read_csv(filepath)
    print(f"✓ Loaded data from: {filepath}")
    print(f"  Shape: {df.shape}")
    print(f"  Columns: {list(df.columns)}")
    
    return df


def save_results(df, filepath, description=""):
    """
    Save results to CSV file.
    
    Parameters
    ----------
    df : pd.DataFrame
        Data to save
    filepath : str
        Output file path
    description : str
        Description of saved data
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)
    print(f"✓ Saved {description} to: {filepath}")


def print_section(title):
    """Print formatted section header."""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)


def print_subsection(title):
    """Print formatted subsection header."""
    print("\n" + "-"*70)
    print(f"  {title}")
    print("-"*70)


def format_timestamp():
    """Return formatted timestamp."""
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def print_dataframe_info(df, name="DataFrame"):
    """Print DataFrame information."""
    print(f"\n{name} Info:")
    print(f"  Shape: {df.shape}")
    print(f"  Columns: {list(df.columns)}")
    print(f"  Missing values: {df.isnull().sum().sum()}")
    print(f"  Data types:")
    for col, dtype in df.dtypes.items():
        print(f"    {col}: {dtype}")


def get_statistics_summary(series):
    """
    Get summary statistics for a series.
    
    Parameters
    ----------
    series : pd.Series
        Input series
    
    Returns
    -------
    dict
        Summary statistics
    """
    return {
        'count': series.count(),
        'mean': series.mean(),
        'std': series.std(),
        'min': series.min(),
        'max': series.max(),
        'median': series.median(),
        'q1': series.quantile(0.25),
        'q3': series.quantile(0.75),
        'missing': series.isnull().sum(),
    }


def print_statistics(series, name="Series"):
    """Print statistics for a series."""
    stats = get_statistics_summary(series)
    
    print(f"\n{name} Statistics:")
    print(f"  Count: {stats['count']}")
    print(f"  Mean: {stats['mean']:.4f}")
    print(f"  Std Dev: {stats['std']:.4f}")
    print(f"  Min: {stats['min']:.4f}")
    print(f"  Max: {stats['max']:.4f}")
    print(f"  Median: {stats['median']:.4f}")
    print(f"  Q1 (25%): {stats['q1']:.4f}")
    print(f"  Q3 (75%): {stats['q3']:.4f}")
    print(f"  Missing: {stats['missing']}")


if __name__ == "__main__":
    print("Utility functions for ESG forecasting")
    create_output_directories()
    print("\n✓ All utility functions are ready to use!")
    