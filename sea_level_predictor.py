import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")

    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Original Data", color="blue")

    result_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_all = pd.Series(range(1880, 2051))
    y_all = result_all.slope * x_all + result_all.intercept
    plt.plot(x_all, y_all, 'r', label="Best Fit Line (1880-2050)")

    df_recent = df[df["Year"] >= 2000]
    result_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = result_recent.slope * x_recent + result_recent.intercept
    plt.plot(x_recent, y_recent, 'green', label="Best Fit Line (2000-2050)")

    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    plt.tight_layout()
    plt.savefig('sea_level_plot.png')
    return plt.gcf()
