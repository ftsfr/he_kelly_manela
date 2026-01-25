"""Generate interactive HTML chart for He-Kelly-Manela Factors."""

import pandas as pd
import plotly.express as px
import os
from pathlib import Path

# Get the project root (one level up from src/)
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "_data"
OUTPUT_DIR = PROJECT_ROOT / "_output"


def generate_hkm_chart():
    """Generate He-Kelly-Manela intermediary capital factors time series chart."""
    # Load HKM factors data
    df = pd.read_parquet(DATA_DIR / "ftsfr_he_kelly_manela_factors_monthly.parquet")

    # Create line chart
    fig = px.line(
        df.sort_values("ds"),
        x="ds",
        y="y",
        color="unique_id",
        title="Intermediary Capital Risk Factors (He, Kelly, Manela 2017)",
        labels={
            "ds": "Date",
            "y": "Factor Value",
            "unique_id": "Factor"
        }
    )

    # Update layout
    fig.update_layout(
        template="plotly_white",
        hovermode="x unified"
    )

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Save chart
    output_path = OUTPUT_DIR / "hkm_factors_replication.html"
    fig.write_html(str(output_path))
    print(f"Chart saved to {output_path}")

    return fig


if __name__ == "__main__":
    generate_hkm_chart()
