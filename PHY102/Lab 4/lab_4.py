# lab_4.py
#
# Author:He Bai
# Student ID:997677931
#
# This library was written as part of Physics 102: Computational Laboratory
# in Physics, Fall 2014.

# import required libraries
import datetime
import numpy as np
import matplotlib.finance as finance
import matplotlib.pyplot as plt

# Exercise 1
def stock_monthly_returns():
    """create a plot of the monthly returns for a stock
    Arguments
    =========
    None

    Prompts the user for a stock ticker

    Returns
    ======
    None

    Saves plot to 'TICKER_monthly_returns.pdf'
    """
    # start your code here
    stock = raw_input('Input a stock ticker: ')
    now = datetime.datetime.now()
    sp = finance.quotes_historical_yahoo(stock, (1900, 1, 1), (now.year, now.month, now.day), asobject=True, adjusted=False)
    graphDate = sp.date[30:]
    graphPrice = [0] * (len(sp.date) - 30)
    for idx, val in enumerate(graphPrice):
        graphPrice[idx] = (sp.close[idx + 30] - sp.close[idx]) / sp.close[idx]
    plt.plot(graphDate, graphPrice)
    plt.xlabel('Dates')
    plt.ylabel('Returns')
    plt.title('Monthy return for stock ' + stock)
    plt.savefig(stock + '_monthly_returns.pdf')
    return None

def cc_decode(file_name):
    """Decodes a text file which has been encoded using a Ceasar Cipher
    Arguments
    =========
    file_name: string containing the name of the file to decode

    Returns
    ======
    None

    Writes decoded text to 'file_name_decoded.txt'
    """
    # start your code here
    file = open(file_name, 'r')
    encoded = file.read()
    bias = ord('a')
    eNum = 4
    counter = [0] * 26
    for item in encoded:
        if item.isalpha():
            item = item.lower()
            # print item
            counter[ord(item) - bias] = counter[ord(item) - bias] + 1
    counter = np.array(counter)
    n = counter.argmax(axis=0) - eNum
    decoded = ""
    for key, item in enumerate(encoded):
        if item.isalpha():
            decodedAscii = ord(item) - bias - n
            if decodedAscii < 0:
                decodedAscii = decodedAscii + 26
            decoded += chr(decodedAscii + bias)
        else:
            decoded += item
    result = open("decoded_" + file_name, 'w')
    result.write(decoded)
    return None
