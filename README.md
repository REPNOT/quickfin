# Quick Fin &nbsp; [![PyPI version](https://badge.fury.io/py/quickfin.svg)](https://badge.fury.io/py/quickfin)


### [Docs](https://quickfin.techbyderek.com/) &nbsp; [Code Examples](https://quickfin.techbyderek.com/main/examples.html) &nbsp; [Data](https://gist.githubusercontent.com/REPNOT/6bffda0dd727d63a0bd727d4ff1c890a/raw/ec1ea323068b45739ddd595dfab897cc5f7c6487/fin_data.json) &nbsp; [Github Repo](https://github.com/REPNOT/quickfin) &nbsp; 


## Description

Quickfin is a [Python](https://www.python.org/) module providing instant access to live and historical stock market price data, automated [Plotly](https://github.com/plotly/plotly.py) data visualization generators and a metadata catalog for referencing equities, stock symbols, sector, and industry information.


## Dependencies

| Library   | Language | Link                                                               |
| --------- | -------- | ------------------------------------------------------------------ |
| Plotly    | Python   | https://github.com/plotly/plotly.py                                |



## Installation

    pip install quickfin


## Upgrade

    pip install --upgrade quickfin


## Quickstart

Retrieve a data payload containing the most recent stock price data available for the stock symbol passed to the `symbol` parameter. Method will return live market price quotes during trading hours. 

### Input:

    from quickfin import *

    price_data = PriceData()

    print(price_data.current("SNOW"))

### Output:

    {
      'current': {
        'Adj Close': 161.6,
        'Change Amount': 2.42,
        'Change Rate': 0.01,
        'Close': 161.6,
        'Date': '2024-03-28',
        'Day Range': 4.89,
        'High': 165.89,
        'Low': 161.0,
        'Open': 164.02,
        'Volume': 10106900
      },
      'info': {
        'industry': 'Software - Application',
        'name': 'Snowflake Inc.',
        'sector': 'Technology',
        'symbol': 'SNOW'
      }
    }
