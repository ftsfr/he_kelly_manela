# %%
"""
# He-Kelly-Manela Intermediary Capital Risk Factors

This notebook provides summary statistics and visualizations for the He, Kelly, and Manela (2017)
intermediary capital risk factors dataset.

## Reference

He, Zhiguo, Bryan Kelly, and Asaf Manela. "Intermediary asset pricing: New evidence from many
asset classes." Journal of Financial Economics 126.1 (2017): 1-35.

## Data Source

Data is publicly available from [Asaf Manela's website](https://asaf.manela.org/papers/hkm/intermediarycapitalrisk/).
"""

# %%
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

import chartbook

BASE_DIR = chartbook.env.get_project_root()
DATA_DIR = BASE_DIR / "_data"

warnings.filterwarnings("ignore")

# %%
"""
## Load the Datasets

We have three datasets:
1. **Monthly factors**: Core intermediary capital risk factors at monthly frequency
2. **Daily factors**: Core intermediary capital risk factors at daily frequency
3. **All factors and test assets**: Extended dataset including test portfolios
"""

# %%
# Load monthly factors
monthly_df = pd.read_parquet(DATA_DIR / "ftsfr_he_kelly_manela_factors_monthly.parquet")
print(f"Monthly factors shape: {monthly_df.shape}")
monthly_df.head()

# %%
# Load daily factors
daily_df = pd.read_parquet(DATA_DIR / "ftsfr_he_kelly_manela_factors_daily.parquet")
print(f"Daily factors shape: {daily_df.shape}")
daily_df.head()

# %%
# Load all factors and test assets
all_df = pd.read_parquet(DATA_DIR / "ftsfr_he_kelly_manela_all.parquet")
print(f"All factors shape: {all_df.shape}")
all_df.head()

# %%
"""
## Summary Statistics - Monthly Factors

The monthly dataset contains four key factors:
- `intermediary_capital_ratio`: Capital ratio of primary dealers
- `intermediary_capital_risk_factor`: Innovation in capital ratio (the risk factor)
- `intermediary_value_weighted_investment_return`: Value-weighted investment return
- `intermediary_leverage_ratio_squared`: Squared leverage ratio
"""

# %%
# Pivot monthly data to wide format for statistics
monthly_wide = monthly_df.pivot(index='ds', columns='unique_id', values='y')

# Calculate summary statistics
summary_stats = monthly_wide.describe().T
summary_stats['skewness'] = monthly_wide.skew()
summary_stats['kurtosis'] = monthly_wide.kurtosis()
summary_stats

# %%
"""
## Time Series Plot - Monthly Factors
"""

# %%
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

factors = monthly_wide.columns.tolist()
for i, factor in enumerate(factors):
    ax = axes[i]
    monthly_wide[factor].plot(ax=ax, linewidth=0.8)
    ax.set_title(factor.replace('_', ' ').title(), fontsize=10)
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.suptitle('He-Kelly-Manela Monthly Factors', y=1.02, fontsize=14)
plt.show()

# %%
"""
## Correlation Matrix - Monthly Factors
"""

# %%
# Calculate correlation matrix
corr_matrix = monthly_wide.corr()

# Create heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".3f",
    cmap="coolwarm",
    center=0,
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink": 0.8}
)
plt.title('Correlation Matrix: He-Kelly-Manela Monthly Factors', fontsize=12)
plt.tight_layout()
plt.show()

# %%
"""
## Summary Statistics - Daily Factors
"""

# %%
# Pivot daily data to wide format
daily_wide = daily_df.pivot(index='ds', columns='unique_id', values='y')

# Calculate summary statistics
daily_summary = daily_wide.describe().T
daily_summary['skewness'] = daily_wide.skew()
daily_summary['kurtosis'] = daily_wide.kurtosis()
daily_summary

# %%
"""
## Data Coverage

Let's examine the date range and data availability for each dataset.
"""

# %%
# Monthly data coverage
print("Monthly Factors:")
print(f"  Date range: {monthly_wide.index.min()} to {monthly_wide.index.max()}")
print(f"  Number of observations: {len(monthly_wide)}")
print(f"  Missing values per column:")
print(monthly_wide.isnull().sum())

# %%
# Daily data coverage
print("\nDaily Factors:")
print(f"  Date range: {daily_wide.index.min()} to {daily_wide.index.max()}")
print(f"  Number of observations: {len(daily_wide)}")
print(f"  Missing values per column:")
print(daily_wide.isnull().sum())

# %%
"""
## Distribution Analysis
"""

# %%
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for i, factor in enumerate(factors):
    ax = axes[i]
    monthly_wide[factor].hist(ax=ax, bins=50, edgecolor='black', alpha=0.7)
    ax.axvline(monthly_wide[factor].mean(), color='red', linestyle='--', label=f'Mean: {monthly_wide[factor].mean():.4f}')
    ax.axvline(monthly_wide[factor].median(), color='green', linestyle='--', label=f'Median: {monthly_wide[factor].median():.4f}')
    ax.set_title(factor.replace('_', ' ').title(), fontsize=10)
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.suptitle('Distribution of He-Kelly-Manela Monthly Factors', y=1.02, fontsize=14)
plt.show()

# %%
"""
## Conclusion

This dataset provides intermediary capital risk factors that can be used for asset pricing studies.
The factors capture the risk-bearing capacity of financial intermediaries and their role in
determining asset prices across multiple asset classes.
"""
