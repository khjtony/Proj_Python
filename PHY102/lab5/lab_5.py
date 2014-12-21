# lab_5.py
#
# Author:He Bai
# Student ID:997677931
#
# This library was written as part of Physics 102: Computational Laboratory
# in Physics, Fall 2014.

# import required libraries
import datetime
import math
import numpy as np
import matplotlib.finance as finance
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit

# Exercise 1
def calc_stats(ticker):
    """calculates basic statistical quantites for the daily returns
    of the stock with ticker

    Arguments
    =========
    ticker: string containg the ticker

    Returns
    ======
    None

    Saves statistical quantities to 'TICKER_daily_returns_stats.txt'
    """
    # start your code here5
    now = datetime.datetime.now()
    sp = finance.quotes_historical_yahoo(ticker, (1900, 1, 1), (now.year, now.month, now.day), asobject=True, adjusted=False)
    returns = np.array([(sp.open[i+1] - sp.open[i]) / sp.open[i] for i in range(len(sp.open) - 1)])
    mean = np.mean(returns)
    median = np.median(returns)
    std = np.std(returns)
    skewness = stats.skew(returns)
    kurtosis = stats.kurtosis(returns)
    resultStr = "Statistical Properties of Daily Returns For: {0}\nMean = {1} Median = {2} Standard Deviation = {3} Skewness = {4} Kurtosis = {5}".format(*(ticker, mean, median, std, skewness, kurtosis))
    result = open(ticker + "_daily_returns_stats.txt", 'w')
    result.write(resultStr)
    return None

# Exercise 2
def gaussian(x, mu, sigma):
    """A python representation of a gaussian distribution with mean mu
    and standard deviation sigma

    Arguments
    =========
    x: float, independant variable for function
    mu: float giving the mean of the gaussian
    sigma: float giving the standard deviation of the gaussian

    Returns
    ======
    float: the value of the gaussian distribution at x
    """
    # start your code here
    term1 = 1 / (sigma * math.sqrt(2 * math.pi))
    term2 = 2 * sigma**2
    return [term1 * math.exp(-(i - mu)**2 / term2) for i in x]

# Exercise 3
def best_fit_gaussian(ticker):
    """determines the best fit gaussian for the distribution of daily
    returns for stock with ticker and makes a plot of the distribution
    and the best-fit gaussian

    =========
    ticker: string for the stock ticker

    Returns
    ======
    None

    Saves plot to 'TICKER_gaussian_fit.pdf'
    """
    # start your code here
    stock_data = finance.quotes_historical_yahoo(ticker, (1950, 1, 1), (2014, 9, 30), asobject=True, adjusted=True)
    returns = np.array([(stock_data.open[i+1] - stock_data.open[i]) / stock_data.open[i] for i in range(len(stock_data.open) - 1)])
    counts, bin_edges = np.histogram(returns, density=True, bins=200)
    bin_centers = bin_edges[:-1]+(bin_edges[1]-bin_edges[0])/2.0
    popt, pcov = curve_fit(gaussian, bin_centers, counts)
    counts_fit = gaussian(bin_centers, *popt)
    blue_dot = plt.plot(bin_centers, counts, label="Daily Returns", color = 'blue', linewidth = 0, marker = 'o', markersize=3, markeredgewidth = 0,  markeredgecolor='none')
    green_line = plt.plot(bin_centers, counts_fit, label="Gaussian", color='green')
    x_axis = plt.xticks()[0]
    text_x_pos = x_axis[math.ceil(len(x_axis) * 0.6)]
    y_axis = plt.yticks()[0]
    text_y_pos = y_axis[math.ceil(len(y_axis) * 0.4)]
    plt.legend(loc="upper right")
    plt.text(text_x_pos, text_y_pos, 'mu={0:.03f}\nsigma={1:.03f}'.format(*(popt[0], popt[1])))
    plt.xlabel('Daily Returns')
    plt.ylabel('Probability Density')
    plt.title(ticker)
    plt.savefig(ticker + '_gaussian_fit.pdf')
    return None
