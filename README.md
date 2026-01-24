# He-Kelly-Manela Factors Pipeline

This pipeline downloads and processes the intermediary capital risk factors from He, Kelly, and Manela (2017).

## Data Source

The data is publicly available from [Asaf Manela's website](https://asaf.manela.org/papers/hkm/intermediarycapitalrisk/).

## Reference

He, Zhiguo, Bryan Kelly, and Asaf Manela. "Intermediary asset pricing: New evidence from many asset classes." Journal of Financial Economics 126.1 (2017): 1-35.

## Outputs

- `ftsfr_he_kelly_manela_factors_monthly.parquet`: Monthly intermediary capital risk factors
- `ftsfr_he_kelly_manela_factors_daily.parquet`: Daily intermediary capital risk factors
- `ftsfr_he_kelly_manela_all.parquet`: All factors and test assets

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the pipeline:
   ```bash
   doit
   ```

3. View the generated documentation in `docs/index.html`

## Factors Included

- `intermediary_capital_ratio`: Capital ratio of primary dealers
- `intermediary_capital_risk_factor`: Innovation in capital ratio (risk factor)
- `intermediary_value_weighted_investment_return`: Value-weighted investment return
- `intermediary_leverage_ratio_squared`: Squared leverage ratio

## Academic References

### Primary Paper

- **He, Kelly, and Manela (2017)** - "Intermediary Asset Pricing: New Evidence from Many Asset Classes"
  - Journal of Financial Economics 126.1 (2017): 1-35
  - DOI: [10.1016/j.jfineco.2017.08.002](https://doi.org/10.1016/j.jfineco.2017.08.002)

### Key Findings

- Shocks to intermediary capital ratios explain cross-sectional variation in expected returns
- Intermediary capital risk is procyclical
- Primary dealers act as marginal investors across asset classes
- The intermediary capital risk factor prices assets across equities, bonds, commodities, and currencies
