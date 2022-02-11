import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,5))
    plt.scatter(x, y)

    # Create first line of best fit
    res = linregress(x,y)
    print(res)
    x_pred = pd.Series([i for i in range(1880,2051)])
    y_pred = res.slope * x_pred + res.intercept
    plt.plot(x_pred, y_pred, 'r')

    # Create second line of best fit
    df2 = df.loc[df['Year'] >= 2000]
    df2_x = df2['Year']
    df2_y = df2['CSIRO Adjusted Sea Level']

    res2 = linregress(df2_x,df2_y)

    x_pred2 = pd.Series([i for i in range(2000,2051)])
    y_pred2 = res2.slope * x_pred2 + res2.intercept
    plt.plot(x_pred2, y_pred2, 'g')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_xlabel('Year')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()