# Advanced GroupBy Operations Guide

This guide provides detailed explanations and examples of advanced pandas GroupBy operations.

## Table of Contents

- [Basic GroupBy Operations](#basic-groupby-operations)
- [Custom Aggregations](#custom-aggregations)
- [Complex Transformations](#complex-transformations)
- [Time-based Grouping](#time-based-grouping)
- [Performance Optimization](#performance-optimization)

## Basic GroupBy Operations

GroupBy operations in pandas allow you to split your data into groups and perform operations on each group. Here's a comprehensive overview of basic operations:

```python
import pandas as pd

# Basic grouping with multiple aggregations
df.groupby('category').agg({
    'sales': ['sum', 'mean', 'std'],
    'units': ['sum', 'mean'],
    'returns': ['sum', 'mean']
})
```

## Custom Aggregations

You can create custom aggregation functions to perform specific calculations:

```python
def profit_margin(series):
    """Calculate profit margin assuming 30% cost"""
    return (series.sum() * 0.7).round(2)

# Using custom aggregation
df.groupby('category').sales.agg([
    ('total_sales', 'sum'),
    ('profit_margin', profit_margin),
    ('avg_sale', 'mean')
])
```

## Complex Transformations

Transformations allow you to perform operations that return data in the same shape as the input:

```python
# Calculate percentage of total sales
df['sales_pct'] = df.groupby('category')['sales'].transform(
    lambda x: (x / x.sum() * 100).round(2)
)
```

## Time-based Grouping

Time-based grouping is essential for analyzing temporal data:

```python
# Daily sales by category
df.groupby([pd.Grouper(freq='D'), 'category'])['sales'].sum()

# Rolling averages by group
df['rolling_avg_sales'] = df.groupby('category')['sales'].transform(
    lambda x: x.rolling(window=24, min_periods=1).mean()
)
```

## Performance Optimization

Tips for optimizing GroupBy operations:

1. Use appropriate data types
2. Filter data before grouping when possible
3. Use numeric datatypes instead of objects
4. Consider using categoricals for group keys

Example of optimized grouping:

```python
# Convert to categorical for better performance
df['category'] = df['category'].astype('category')

# Pre-filter data
filtered_df = df[df['sales'] > 0]
result = filtered_df.groupby('category')['sales'].sum()
```

For more examples and detailed explanations, check the [example scripts](../examples/) in the repository.

