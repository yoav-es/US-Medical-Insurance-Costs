__version__ = "1.0.0"

from .data_io import load_data, save_report
from .processing import preprocess
from .analysis import (
    summary_stats,
    group_by_smoker_charges,
    compute_region_stats,
    compute_bmi_stats,
    compute_smoker_bmi_stats,
)
from .viz import (
    plot_correlation,
    plot_region_bars,
    plot_charges_distribution,
    plot_bmi_stats,
    plot_bmi_smoker,
)

__all__ = [
    "load_data",
    "save_report",
    "preprocess",
    "summary_stats",
    "group_by_smoker_charges",
    "compute_region_stats",
    "compute_bmi_stats",
    "compute_smoker_bmi_stats",
    "plot_correlation",
    "plot_region_bars",
    "plot_charges_distribution",
    "plot_bmi_stats",
    "plot_bmi_smoker",
]
