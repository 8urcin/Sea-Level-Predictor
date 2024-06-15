import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    plt.figure(figsize=(10, 5))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extend = pd.Series([i for i in range(1880, 2051)])
    plt.plot(years_extend, intercept + slope * years_extend, 'r', label='Fit Line 1880-2050')

    recent_df = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    recent_years_extend = pd.Series([i for i in range(2000, 2051)])
    plt.plot(recent_years_extend, intercept_recent + slope_recent * recent_years_extend, 'g', label='Fit Line 2000-2050')

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    plt.savefig('sea_level_plot.png')
    return plt.gca()
