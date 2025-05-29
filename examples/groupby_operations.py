"""
Advanced GroupBy operations in pandas.

This module demonstrates various advanced GroupBy operations,
including custom aggregations, transformations, and time-based analysis.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def create_sample_data(n_records=1000):
    """
    Create a sample dataset with sales information.

    Parameters:
    -----------
    n_records : int, default 1000
        Number of records to generate

    Returns:
    --------
    pandas.DataFrame
        A DataFrame containing sample sales data
    """
    np.random.seed(42)
    dates = pd.date_range(start='2023-01-01', periods=n_records, freq='h')
    categories = ['Electronics', 'Clothing', 'Food', 'Books']
    regions = ['North', 'South', 'East', 'West']
    
    data = {
        'date': dates,
        'category': np.random.choice(categories, n_records),
        'region': np.random.choice(regions, n_records),
        'sales': np.random.uniform(10, 1000, n_records).round(2),
        'units': np.random.randint(1, 50, n_records),
        'returns': np.random.randint(0, 5, n_records)
    }
    
    return pd.DataFrame(data)

def perform_basic_aggregations(df):
    """
    Perform basic GroupBy aggregations with multiple metrics.

    Parameters:
    -----------
    df : pandas.DataFrame
        Input DataFrame with sales data

    Returns:
    --------
    pandas.DataFrame
        Aggregated results
    """
    return df.groupby('category').agg({
        'sales': ['sum', 'mean', 'std'],
        'units': ['sum', 'mean'],
        'returns': ['sum', 'mean']
    }).round(2)

def calculate_profit_margins(df):
    """
    Calculate profit margins using custom aggregation.

    Parameters:
    -----------
    df : pandas.DataFrame
        Input DataFrame with sales data

    Returns:
    --------
    pandas.DataFrame
        Profit margin calculations
    """
    def profit_margin(series):
        """Calculate profit margin assuming 30% cost"""
        return (series.sum() * 0.7).round(2)

    return df.groupby('category').sales.agg([
        ('total_sales', 'sum'),
        ('profit_margin', profit_margin),
        ('avg_sale', 'mean')
    ]).round(2)

def calculate_sales_percentages(df):
    """
    Calculate sales percentages within categories.

    Parameters:
    -----------
    df : pandas.DataFrame
        Input DataFrame with sales data

    Returns:
    --------
    pandas.DataFrame
        DataFrame with added sales percentage column
    """
    df = df.copy()
    df['sales_pct'] = df.groupby('category')['sales'].transform(
        lambda x: (x / x.sum() * 100).round(2)
    )
    return df

def main():
    """Main function to demonstrate GroupBy operations."""
    # Create sample dataset
    df = create_sample_data()

    # Perform various analyses
    print("\n1. Basic Aggregations:")
    print(perform_basic_aggregations(df))

    print("\n2. Profit Margins:")
    print(calculate_profit_margins(df))

    print("\n3. Sales Percentages:")
    result_df = calculate_sales_percentages(df)
    print(result_df[['category', 'sales', 'sales_pct']].head(10))

    # Additional analyses can be added here

if __name__ == "__main__":
    main()

