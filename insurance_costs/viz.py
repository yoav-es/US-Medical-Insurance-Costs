from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns


def plot_correlation(df, out_path: Path | str = None):
    '''Plot correlation heatmap for numeric columns. Returns the figure.'''
    fig, ax = plt.subplots(figsize=(8, 5))
    corr = df.select_dtypes(include=["number"]).corr()
    sns.heatmap(corr, annot=True, fmt=".2f", ax=ax)
    if out_path:
        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_path, bbox_inches="tight")
    return fig


def plot_region_bars(region_stats, out_path: Path | str = None):
    """Plot mean charges by region (bar chart)."""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(region_stats["region"], region_stats["mean_charge"], color="skyblue")
    ax.set_ylabel("Mean Charges (USD)")
    ax.set_xlabel("Region")
    ax.set_title("Average Yearly Charges by Region")
    fig.tight_layout()
    if out_path:
        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_path, bbox_inches="tight")
    return fig


def plot_charges_distribution(df, q1=None, q3=None, median=None, out_path: Path | str = None):
    """Plot histogram of charges with median and IQR shading."""
    if median is None:
        median = df["charges"].median()
    if q1 is None or q3 is None:
        q1, q3 = df["charges"].quantile([0.25, 0.75])
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df["charges"], bins=30, color="skyblue", edgecolor="black", alpha=0.7)
    ax.axvline(median, color="red", linestyle="--", label="Median")
    ax.axvspan(q1, q3, color="orange", alpha=0.2, label="IQR")
    ax.set_xlabel("Yearly Insurance Charges (USD)")
    ax.set_ylabel("Patient Count")
    ax.set_title("Distribution of Yearly Medical Charges")
    ax.legend()
    fig.tight_layout()
    if out_path:
        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_path, bbox_inches="tight")
    return fig


def plot_bmi_stats(bmi_stats, out_path: Path | str = None):
    """Plot BMI class counts and mean charges (bar + pointplot)."""
    fig, ax1 = plt.subplots(figsize=(8, 5))
    sns.barplot(data=bmi_stats.reset_index(), x="bmi_class", y="count", color="skyblue", ax=ax1)
    ax1.set_ylabel("Count of Records", color="skyblue")
    ax1.set_xlabel("BMI Class (Patient Count)")
    ax2 = ax1.twinx()
    sns.pointplot(data=bmi_stats.reset_index(), x="bmi_class", y="mean_charge", color="crimson", marker="o", ax=ax2)
    ax2.set_ylabel("Average Charges (USD)")
    fig.tight_layout()
    if out_path:
        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_path, bbox_inches="tight")
    return fig


def plot_bmi_smoker(mean_table, out_path: Path | str = None):
    """Plot mean charges by BMI class and smoker status (bar chart)."""
    fig, ax = plt.subplots(figsize=(8, 5))
    mean_table[["no", "yes"]].plot(kind="bar", figsize=(8, 5), color=["skyblue", "crimson"], ax=ax)
    ax.set_ylabel("Mean Charges (USD)")
    ax.set_title("Mean Charges by BMI Class and Smoker Status")
    ax.set_xticklabels(mean_table.index, rotation=0)
    fig.tight_layout()
    if out_path:
        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(out_path, bbox_inches="tight")
    return fig
