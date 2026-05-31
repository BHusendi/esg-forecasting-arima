"""
Sample CSV file generator for ESG data

This creates a sample CSV file that can be used as reference.
Run this to generate sample_esg_data.csv in data/raw/ directory.
"""

import pandas as pd
import numpy as np
from datetime import datetime

# Create sample data
np.random.seed(42)
n_periods = 36
dates = pd.date_range('2021-01-01', periods=n_periods, freq='M')

# Generate synthetic data
t = np.arange(n_periods)
environmental = 60 + 0.5*t + 3*np.sin(2*np.pi*t/12) + np.random.normal(0, 2, n_periods)
social = 65 + 0.3*t + 2*np.cos(2*np.pi*t/12) + np.random.normal(0, 2, n_periods)
governance = 70 + 0.2*t + np.random.normal(0, 2.5, n_periods)

# Introduce missing values
environmental[[5, 15, 25]] = np.nan
social[[7, 18]] = np.nan
governance[[12, 24]] = np.nan

# Clip to valid range
environmental = np.clip(environmental, 0, 100)
social = np.clip(social, 0, 100)
governance = np.clip(governance, 0, 100)

# Create DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Environmental': environmental,
    'Social': social,
    'Governance': governance
})

# Display
print("Sample ESG Data (first 10 rows):")
print(df.head(10))
print(f"\nData Shape: {df.shape}")
print(f"\nMissing Values:\n{df.isnull().sum()}")
# Save to CSV
output_path = 'data/raw/sample_esg_data.csv'