"""generate_report.py
_summary_

_extended_summary_

Returns:
    _type_: _description_
"""

import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from jinja2 import Environment, FileSystemLoader

# Set the style for seaborn
sns.set_theme(style="whitegrid")

# Directory to save the generated images
IMAGE_DIR = "report_images"
os.makedirs(IMAGE_DIR, exist_ok=True)


def save_plot(fig, filename):
    filepath = os.path.join(IMAGE_DIR, filename)
    fig.savefig(filepath)
    plt.close(fig)
    return filepath


def generate_summary(df):
    total_sales = df["sales_amount_squared"].sum()
    total_profit = df["profit"].sum()
    summary = (
        f"Total sales (squared): {total_sales:.2f}\nTotal profit: {total_profit:.2f}"
    )
    return summary


def generate_plots(df):
    # Monthly Sales Trend
    df["date"] = pd.to_datetime(df["date"])
    monthly_sales = df.resample("M", on="date").sum()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(monthly_sales.index, monthly_sales["sales_amount_squared"], marker="o")
    ax.set_title("Monthly Sales Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Sales (Squared)")
    monthly_sales_trend_img = save_plot(fig, "monthly_sales_trend.png")

    # Average Monthly Sales
    df["month"] = df["date"].dt.month
    seasonal_sales = df.groupby("month")["sales_amount_squared"].mean()

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(
        x=seasonal_sales.index, y=seasonal_sales.values, ax=ax, palette="viridis"
    )
    ax.set_title("Average Monthly Sales")
    ax.set_xlabel("Month")
    ax.set_ylabel("Average Sales (Squared)")
    average_monthly_sales_img = save_plot(fig, "average_monthly_sales.png")

    # Top-selling Products
    top_products = (
        df.groupby("product_category")["sales_amount_squared"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=top_products.index, y=top_products.values, ax=ax, palette="viridis")
    ax.set_title("Top-selling Products")
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Total Sales (Squared)")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    top_products_img = save_plot(fig, "top_products.png")

    # Top-selling Regions
    top_regions = (
        df.groupby("region")["sales_amount_squared"].sum().sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=top_regions.index, y=top_regions.values, ax=ax, palette="viridis")
    ax.set_title("Top-selling Regions")
    ax.set_xlabel("Region")
    ax.set_ylabel("Total Sales (Squared)")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    top_regions_img = save_plot(fig, "top_regions.png")

    return (
        monthly_sales_trend_img,
        average_monthly_sales_img,
        top_products_img,
        top_regions_img,
    )


def render_report(df, template_path, output_path):
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(template_path)

    summary = generate_summary(df)
    (
        monthly_sales_trend_img,
        average_monthly_sales_img,
        top_products_img,
        top_regions_img,
    ) = generate_plots(df)

    html_content = template.render(
        date=datetime.now().strftime("%Y-%m-%d"),
        summary=summary,
        monthly_sales_trend_img=monthly_sales_trend_img,
        average_monthly_sales_img=average_monthly_sales_img,
        top_products_img=top_products_img,
        top_regions_img=top_regions_img,
    )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)


if __name__ == "__main__":
    # Load the combined dataframe (for demonstration, using a small sample DataFrame)
    data = {
        "date": pd.date_range(start="1/1/2020", periods=100, freq="D"),
        "sales_amount_squared": pd.np.random.rand(100) * 1000,
        "profit": pd.np.random.rand(100) * 500,
        "product_category": pd.np.random.choice(["A", "B", "C", "D"], 100),
        "region": pd.np.random.choice(["North", "South", "East", "West"], 100),
    }
    df = pd.DataFrame(data)

    render_report(df, "report_template.html", "sales_report.html")
