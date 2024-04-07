# -*- coding: utf-8 -*-
"""
Quick Fin

A Python module providing instant access to live
and historical stock market price data, automated
Plotly data visualization generators, live stock ticker 
visualization for Streamlit applications and a data 
catalog for referencing equities, stock symbols, sectors, 
and industry information.
"""

__version__ = "1.15.0"
__author__ = "Derek Evans <https://github.com/REPNOT>"
__date__ = "28 March 2024"

import json
from pprint import pprint
import requests
import datetime
from datetime import datetime
from urllib.request import Request, urlopen
import plotly.graph_objects as go
import streamlit as st
from pathlib import Path
import os


class FinInfo():

    """
    A class for accessing a metadata catalog for referencing. 
    equities, stock symbols, sectors, and industry information.

    THE FOLLOWING APPLIES TO ALL FinInfo METHOD:

    If the value is set to `False`
    for the `payload` parameter, this method
    will `pretty print` the requested data omitting
    a return value.  Otherwise, the value assigned to the
    `payload` parameter is set to `True` by default, and
    the method will return a data payload.
    """


    def __init__(self):

        """
        Initialize the FinInfo class and retreive metadata catalog.
        """

        self.url = "https://gist.githubusercontent.com/REPNOT/6bffda0dd727d63a0bd727d4ff1c890a/raw/5228da45d64741489973b8e05a0abf3d2a3957c1/fin_data.json"
        self.data = requests.get(self.url).json()


    def equity(self, symbol, payload=True):

        """
        Return object containing the symbol, company name,
        sector, and industry for the stock symbol passed to
        the `symbol` parameter.
        """

        self.symbol = symbol

        if payload == True:

            return self.data["equities"][self.symbol]

        else:

            pprint(self.data["equities"][self.symbol])
            return


    def equities(self, payload=True):

        """
        Return data payload containing the symbol, company name,
        sector, and industry for all equities included in the
        metadata catalog.

        PAYLOAD CONTENTS:

        An array of objects.
        """

        self.payload = []

        for symbol in self.data["equities"].keys():

            self.payload.append(self.data["equities"][symbol])

        if payload == True:

            return self.payload

        else:

            pprint(self.payload)
            return


    def industries(self, payload=True):

        """
        Return data payload containing a list
        of all industries available in the metadata
        catalog.

        PAYLOAD CONTENTS:

        An array of strings.
        """

        if payload == True:

            return self.data["meta_data"]["industries"]

        else:

            pprint(self.data["meta_data"]["industries"])
            return

    def sectors(self, payload=True):

        """
        Return data payload containing a list
        of all sectors available in the metadata
        catalog.

        PAYLOAD CONTENTS:

        An array of strings.
        """

        if payload == True:

            return self.data["meta_data"]["sectors"]

        else:

            pprint(self.data["meta_data"]["sectors"])
            return

    def sector_industries(self, sector=None, payload=True):

        """
        Return data payload containing a list
        of all industries belonging to the sector
        passed to the `sector` parameter. 

        PAYLOAD CONTENTS:

        An array of strings.

        By default, the return value will include an 
        object containing all sectors and associated industries.
        """

        try:
            self.sector = sector.title()
        except:
            return '===  ERROR: DATA TYPE - SECTOR MUST BE STRING  ==='

        try:
            if payload == True and self.sector != None:
                return self.data["meta_data"]["sector-industries"][self.sector]
            elif payload != True and self.sector != None:
                pprint(self.data["meta_data"]["sector-industries"][self.sector])
            elif payload != True and self.sector == None:
                pprint(self.data["meta_data"]["sector-industries"])
            else:
                return self.data["meta_data"]["sector-industries"]
        except:
            return '===  ERROR: INVALID SECTOR ENTRY  ==='


    def sector_equities(self, sector=None, payload=True):

        """
        Return data payload containing a list
        of all equities belonging to the sector
        passed to the `sector` parameter. 

        PAYLOAD CONTENTS:

        An array of objects.

        By default, the return value will include an 
        object containing all sectors and associated 
        equity data.
        """

        try:
            self.sector = sector.title()
        except:
            return '===  ERROR: DATA TYPE - SECTOR MUST BE STRING  ==='

        try:
            if payload == True and self.sector != None:
                return self.data["sectors"][self.sector]
            elif payload != True and self.sector != None:
                pprint(self.data["sectors"][self.sector])
            elif payload != True and self.sector == None:
                pprint(self.data["sectors"])
            else:
                return self.data["sectors"]
        except:
            return '===  ERROR: INVALID SECTOR ENTRY  ==='


    def industry_equities(self, industry=None, payload=True):

        """
        Return data payload containing a list
        of all equities belonging to the industry
        passed to the `industry` parameter. 

        PAYLOAD CONTENTS:

        An array of objects.

        By default, the return value will include an 
        object containing all industries and associated 
        equity data.
        """

        try:
            self.industry = industry.title()
        except:
            return '===  ERROR: DATA TYPE - INDUSTRY MUST BE STRING  ==='

        try:
            if payload == True and self.industry != None:
                return self.data["industries"][self.industry]
            elif payload != True and self.industry != None:
                pprint(self.data["industries"][self.industry])
            elif payload != True and self.industry == None:
                pprint(self.data["industries"])
            else:
                return self.data["industries"]
        except:
            return '===  ERROR: INVALID INDUSTRY ENTRY  ==='


    def symbols(self, payload=True):

        """
        Return data payload containing a list
        of all stock symbols available in the
        metadata catalog. 

        PAYLOAD CONTENTS:

        An array of strings.
        """

        if payload == True:

            return list(self.data["equities"].keys())

        else:

            pprint(list(self.data["equities"].keys()))
            return

    def industry_symbols(self, industry=None, payload=True):

        """
        Return data payload containing a list
        of all stock symbols belonging to the
        industry passed to the `industry` parameter
        available in the metadata catalog. 

        PAYLOAD CONTENTS:

        An array of strings.

        By default, the return value will include an 
        object containing all industries and associated 
        symbols.
        """

        try:
            self.industry = industry.title()
        except:
            return '===  ERROR: DATA TYPE - INDUSTRY MUST BE STRING  ==='

        try:
            if payload == True and self.industry != None:
                return self.data["meta_data"]["industry-symbols"][self.industry]
            elif payload != True and self.industry != None:
                pprint(self.data["meta_data"]["industry-symbols"][self.industry])
            elif payload != True and self.industry == None:
                pprint(self.data["meta_data"]["industry-symbols"])
            else:
                return self.data["meta_data"]["industry-symbols"]
        except:
            return '===  ERROR: INVALID INDUSTRY ENTRY  ==='


    def sector_symbols(self, sector=None, payload=True):

        """
        Return data payload containing a list
        of all stock symbols belonging to the
        sector passed to the `sector` parameter
        available in the metadata catalog. 

        PAYLOAD CONTENTS:

        An array of strings.

        By default, the return value will include an 
        object containing all sectors and associated 
        symbols.
        """

        try:
            self.sector = sector.title()
        except:
            return '===  ERROR: DATA TYPE - SECTOR MUST BE STRING  ==='

        try:
            if payload == True and self.sector != None:
                return self.data["meta_data"]["sector-symbols"][self.sector]
            elif payload != True and self.sector != None:
                pprint(self.data["meta_data"]["sector-symbols"][self.sector])
            elif payload != True and self.sector == None:
                pprint(self.data["meta_data"]["sector-symbols"])
            else:
                return self.data["meta_data"]["sector-symbols"]
        except:
            return '===  ERROR: INVALID SECTOR ENTRY  ==='


class PriceData():

    """
    A class providing instant access to live 
    and historical stock market price data and
    automated Plotly data visualization generators.
    """

    def __init__(self):
        """
        Initialize the PriceData class and assign values to global
        variables.
        """
        start_target = datetime.strptime("1-21-1972", "%m-%d-%Y")
        cur_date = datetime.strptime(datetime.now().strftime("%m-%d-%Y"), "%m-%d-%Y")
        days = (cur_date - start_target).days
        epoch_start = 76204800
        epoch_target = (days * 86400) + 86400 + 1710979200
        self.base_url = "https://query1.finance.yahoo.com/v7/finance/download/"
        self.tail_url = f"?period1={str(epoch_start)}&period2={str(epoch_target)}&interval=1d&events=history&includeAdjustedClose=true"

    def current(self, symbol):

        """
        Return the most recent stock price data available
        for the stock symbol passed to the `symbol`
        parameter.  Method will return live market
        price quotes during trading hours.

        PAYLOAD CONTENTS:

        Object
        """

        self.symbol = symbol
        info = FinInfo()
        self.info = info.equity(symbol)

        try:
            url = self.base_url + self.symbol + self.tail_url
            self.rawData = urlopen(Request(url)).readlines()
        except:
            return '===  ERROR: GET REQUEST FAILED  ==='

        try:
            self.current_price = self.rawData[-1].decode().split(",")
        except:
            return '===  ERROR: DATA ERROR  ==='

        self.data = {"info":self.info}
        self.data["current"] = {}

        try:
            self.data["current"]['Date'] = str(self.current_price[0])
        except:
            self.data["current"]['Date'] = ''

        try:
            self.data["current"]['Open'] = round(float(self.current_price[1]), 2)
        except:
            self.data["current"]['Open'] = ''

        try:
           self.data["current"]['High'] = round(float(self.current_price[2]), 2)
        except:
            self.data["current"]['High'] = ''

        try:
            self.data["current"]['Low'] = round(float(self.current_price[3]), 2)
        except:
            self.data["current"]['Low'] = ''

        try:
           self.data["current"]['Close'] = round(float(self.current_price[4]), 2)
        except:
            self.data["current"]['Close'] = ''

        try:
            self.data["current"]['Adj Close'] = round(float(self.current_price[5]), 2)
        except:
            self.data["current"]['Adj Close'] = ''

        try:
            self.data["current"]['Volume'] = int(self.current_price[6])
        except:
            self.data["current"]['Volume'] = ''

        try:
            self.data["current"]['Change Amount'] = round((self.data["current"]['Close'] - self.data["current"]['Open']), 2)
        except:
            self.data["current"]['Change Amount'] = ''

        try:
            if self.data["current"]['Change Amount'] != 0:
                self.data["current"]['Change Rate'] = round((self.data["current"]['Change Amount'] / self.data["current"]['Open']), 4)
            else:
                self.data["current"]['Change Rate'] = 0
        except:
            self.data["current"]['Change Rate'] = ''

        try:
            self.data["current"]['Day Range'] = round((self.data["current"]['Low'] - self.data["current"]['High']), 2)
        except:

            self.data["current"]['Day Range'] = ''

        try:
            return self.data
        except:
            return '===  SYMBOL DATA TYPE ERROR OR SYMBOL UNAVAILABLE  ==='

    def history(self, symbol, days=None, date=None, date_start=None, date_end=None):

        """
        Return all historical stock price data available 
        for the stock symbol passed to the `symbol` parameter.
        
        Passing a positive integer value to the `days` 
        parameter will filter the historical data to include
        records for the number of most recent days 
        represented by the parameter value.

        Passing a date to the `date` parameter
        using the 'YYYY-DD-MM' format
        will filter the historical data to include
        a single record for the value 
        assigned to the parameter.

        Passing a date to both the `date_start` 
        and the `date_end` parameter
        using the 'YYYY-DD-MM' format
        will filter the historical data to include
        multiple records for the date range
        represented by both values.  Values must 
        be passed to both the date_start and 
        date_end parameter for date ranges to be returned.

        PAYLOAD CONTENTS:

        Object containing equity metadata,
        current price data, and an array
        of objects consisting of daily price
        data for all available dates.

        """

        self.symbol = symbol

        try:
            url = self.base_url + self.symbol + self.tail_url
            self.rawData = urlopen(Request(url)).readlines()
        except:
            return '===  ERROR: GET REQUEST FAILED  ==='

        self.data = self.current(self.symbol)
        self.data["history"] = []

        try:
            self.raw_data = self.rawData[1:][::-1]
        except:
            return '===  ERROR: DATA ERROR  ==='

        for row in self.raw_data:

            self.row_data = {}

            try:
                self.price = row.decode().split(",")
            except:
                return '===  ERROR: DATA ERROR  ==='

            try:
                self.row_data['Date'] = str(self.price[0])
            except:
                self.row_data['Date'] = ''

            try:
                self.row_data['Open'] = round(float(self.price[1]), 2)
            except:
                self.row_data['Open'] = ''

            try:
                self.row_data['High'] = round(float(self.price[2]), 2)
            except:
                self.row_data['High'] = ''

            try:
                self.row_data['Low'] = round(float(self.price[3]), 2)
            except:
                self.row_data['Low'] = ''

            try:
                self.row_data['Close'] = round(float(self.price[4]), 2)
            except:
                self.row_data['Close'] = ''

            try:
                self.row_data['Adj Close'] = round(float(self.price[5]), 2)
            except:
                self.row_data['Adj Close'] = ''

            try:
                self.row_data['Volume'] = int(self.price[6])
            except:
                self.row_data['Volume'] = ''

            try:
                self.row_data['Change Amount'] = round((self.row_data['Close'] - self.row_data['Open']), 2)
            except:
                self.row_data['Change Amount'] = ''

            try:
                if self.row_data['Change Amount'] != 0:
                    self.row_data['Change Rate'] = round((self.row_data['Change Amount'] / self.row_data['Open']), 4)
                else:
                    self.row_data['Change Rate'] = 0
            except:
                self.row_data['Change Rate'] = ''

            try:

                self.row_data['Day Range'] = round((self.row_data['Low'] - self.row_data['High']), 2)

                if self.row_data['Day Range'] < 0:
                    self.row_data['Day Range'] = self.row_data['Day Range'] * -1
                else:
                    pass

            except:

                self.row_data['Day Range'] = ''

            self.data["history"].append(self.row_data)

        if days == None and date == None and date_start == None and date_end == None:

            return self.data

        elif date != None:

            try:

                self.data["history"] = [row for row in self.data["history"] if row["Date"] == date]

                return self.data

            except:

                return '===  DATE SELECTION NOT AVAILABLE  ==='

        elif days != None:

            if type(days) is int and days >= 1:

                self.data["history"] = self.data["history"][0:days]

                return self.data

            else:

                return '===  ERROR: DATA TYPE - DAYS MUST BE INT  ==='

        elif date_start != None and date_end != None:

            self.data["history"] = [row for row in self.data["history"] if row["Date"] >= date_start and row["Date"] <= date_end]

            return self.data

        else:

            return self.data

    def candlestick(self, symbol, days):

        """
        Will generate a Plotly Candlestick
        plot for the most recent total
        number of days represented by the
        value passed to the `days` parameter.

        Executing this method will automatically
        open the data visualization in the 
        default web browser.

        PAYLOAD CONTENTS:

        Plotly Visualization

        """

        if type(days) is not int or days < 1:
            return f'===  DATA TYPE ERROR - DAYS MUST BE INTEGER VALUE GREATER THAN OR EQUAL TO 1  ==='
        else:
            pass

        self.symbol = symbol
        self.days = days
        self.data = self.history(symbol, self.days)
        self.info = self.data["info"]
        self.current = self.data["current"]
        self.history = self.data["history"]

        open_price = [row["Open"] for row in self.history]
        close_price = [row["Close"] for row in self.history]
        low_price = [row["Low"] for row in self.history]
        high_price = [row["High"] for row in self.history]
        dates = [f'{str(row["Date"]).split("-")[1]}-{str(row["Date"]).split("-")[-1]}-{str(row["Date"]).split("-")[0][2:]}' for row in self.history]

        fig = go.Figure(
            data=[go.Candlestick(
                x=dates,
                open=open_price,
                high=high_price,
                low=low_price, 
                close=close_price,
                increasing_line_color= 'green', 
                decreasing_line_color= 'red'
            )]
        )

        fig.update_layout(xaxis_rangeslider_visible=False)
        fig.update_xaxes(type="category", tickangle=60, automargin="height+width", autorange="reversed")

        try:
            fig.show()
            return self.history
        except:
            return f'===  SYMBOL DATA TYPE ERROR OR INVALID SYMBOL  ==='

    def line(self, symbol, days, param):

        """
        Will generate a Plotly Line
        plot for the most recent total
        number of days represented by the
        value passed to the `days` parameter
        for the specified data column passed
        to the `param` parameter.

        Executing this method will automatically
        open the data visualization in the 
        default web browser.

        `param` OPTIONS:

            - Change Amount
            - Change Rate
            - Day Range
            - Volume
            - Adj Close
            - Close
            - Low
            - High
            - Open

        PAYLOAD CONTENTS:

        Plotly Visualization

        """

        param_options = [
            "Change Amount",
            "Change Rate",
            "Day Range",
            "Volume",
            "Adj Close",
            "Close",
            "Low",
            "High",
            "Open"
        ]

        if type(days) is not int or days >= 0:
            return f'===  DATA TYPE ERROR - DAYS MUST BE INTEGER VALUE GREATER THAN OR EQUAL TO 1  ==='
        elif param not in param_options:
            return f'===  INVALID OPTION - PLEASE USE ONE OF THE FOLLOWING {param_options}  ==='
        else:
            pass

        self.symbol = symbol
        self.days = days
        self.data = self.history(symbol, self.days)
        self.info = self.data["info"]
        self.current = self.data["current"]
        self.history = self.data["history"]
        self.param = param.title()

        quote_data = [row[self.param] for row in self.history]
        dates = [f'{str(row["Date"]).split("-")[1]}-{str(row["Date"]).split("-")[-1]}-{str(row["Date"]).split("-")[0][2:]}' for row in self.history]

        fig = go.Figure([go.Scatter(x=dates, y=quote_data)])

        fig.update_layout(xaxis_rangeslider_visible=False)
        fig.update_xaxes(type="category", tickangle=60, automargin="height+width", autorange="reversed")

        try:
            fig.show()
            return self.history
        except:
            return f'===  SYMBOL DATA TYPE ERROR OR INVALID SYMBOL  ==='

    def table(self, symbol, days):

        """
        Will generate a Plotly Table
        for the most recent total
        number of days represented by the
        value passed to the `days` parameter.

        Executing this method will automatically
        open the data visualization in the 
        default web browser.

        PAYLOAD CONTENTS:

        Plotly Visualization

        """

        if type(days) is not int or days >= 0:
            return f'===  DATA TYPE ERROR - DAYS MUST BE INTEGER VALUE GREATER THAN OR EQUAL TO 1  ==='
        else:
            pass

        self.symbol = symbol
        self.days = days
        self.data = self.history(symbol, self.days)
        self.info = self.data["info"]
        self.current = self.data["current"]
        self.history = self.data["history"]


        dates = [f'{str(row["Date"]).split("-")[1]}-{str(row["Date"]).split("-")[-1]}-{str(row["Date"]).split("-")[0][2:]}' for row in self.history]
        open_price = [row["Open"] for row in self.history]
        high_price = [row["High"] for row in self.history]
        low_price = [row["Low"] for row in self.history]
        close_price = [row["Close"] for row in self.history]
        adj_price = [row["Adj Close"] for row in self.history]
        volume = [row["Volume"] for row in self.history]
        change_amount = [row["Change Amount"] for row in self.history]
        change_rate = [row["Change Rate"] for row in self.history]
        day_range = [row["Day Range"] for row in self.history]

        dates = [f'{str(row["Date"]).split("-")[1]}-{str(row["Date"]).split("-")[-1]}-{str(row["Date"]).split("-")[0][2:]}' for row in self.history]

        columns = list(self.data["history"][0].keys())

        fig = go.Figure(data=[go.Table(
                header=dict(values=columns,
                    line_color='darkslategray',
                    fill_color='lightskyblue',
                    align='left'
                ),
                cells=dict(values=[
                        dates, 
                        open_price, 
                        high_price, 
                        low_price, 
                        close_price, 
                        adj_price, 
                        volume, 
                        change_amount, 
                        change_rate, 
                        day_range
                    ],
                    line_color='darkslategray',
                    fill_color='lightcyan',
                    align='left'
                )
            )
        ])

        try:
            fig.show()
            return self.history
        except:
            return f'===  SYMBOL DATA TYPE ERROR OR INVALID SYMBOL  ==='


class Ticker(PriceData):

    """
    The Ticker class is to generate live stock ticker
    visualizations for Streamlit applications.

    Please note that this class will only work in
    Streamlit applications.
    """

    def __init__(self):

        self.price_data = PriceData()

    @st.experimental_fragment()
    def get_quotes_temp(self, sym_lst):

        """
        The `get_quotes_temp` method is used to initiate
        the stock ticker by collecting a partial
        list of price quotes and writing the data to a JSON
        file named quotes.json saved to the ticker_data directory.
        If the ticker_data directory doesn't exist prior to the 
        method being ran, it will automatically create the directory.
        """

        self.sym_lst = sym_lst[0:3]

        self.priceData = [self.price_data.current(symbol) for symbol in self.sym_lst]

        self.priceData = (
            {
                "name":equity["info"]["name"], 
                "symbol":equity["info"]["symbol"],
                "close":equity["current"]["Close"],
                "change_amount":equity["current"]["Change Amount"],
                "change_rate":equity["current"]["Change Rate"]   
            } 
            for equity in self.priceData
        )

        self.symbol_color = "#1D99EB"
        self.name_color = "#ffffff"
        self.close_color = "#ffffff"
        self.lag_color = "#F20505"
        self.gain_color = "#84BF04"
        self.even_color = "#ffffff"

        self.quote_data = []

        for quote in list(self.priceData):

            payload = {}

            payload["symbol"] = f'<span id="symbol" style="color:{self.symbol_color};">&nbsp;&nbsp;&nbsp;&nbsp;{quote["symbol"]}</span>'
            payload["name"] = f'<span id="name" style="color:{self.name_color};">{quote["name"]}</span>'
            payload["close"] = f'<span id="close" style="color:{self.close_color};">$ {str(quote["close"])}</span>'
            payload["change_amount"] = quote["change_amount"]

            try:
                payload["change_rate"] = str(round((quote["change_rate"] * 100), 3))
            except:
                payload["change_rate"] = '- null -'

            if float(payload["change_amount"]) < 0:
                payload["change_amount"] = f'<span class="lag" style="color:{self.lag_color};">$ {str(payload["change_amount"])}</span>'
                payload["change_rate"] = f'<span class="lag" style="color:{self.lag_color};">{str(payload["change_rate"])}%</span>'
            elif float(payload["change_amount"]) > 0:
                payload["change_amount"] = f'<span class="gain" style="color:{self.gain_color};">$ {str(payload["change_amount"])}</span>'
                payload["change_rate"] = f'<span class="gain" style="color:{self.gain_color};">{str(payload["change_rate"])}%</span>'
            else:
                payload["change_amount"] = f'<span class="even" style="color:{self.even_color};">$ {str(payload["change_amount"])}</span>'
                payload["change_rate"] = f'<span class="even" style="color:{self.even_color};">{str(payload["change_rate"])}%</span>'

            self.quote_data.append(payload)

        try:
            os.makedirs(f"{str(Path.cwd())}/ticker_data")
        except:
            pass

        file_str = f"{str(Path.cwd())}/ticker_data/quotes.json"

        with open(file_str, "w") as fileObj:
            json.dump(self.quote_data, fileObj, indent=4)

        return

    @st.experimental_fragment(run_every=600)
    def get_quotes(self, sym_lst):

        """
        The `get_quotes` is used to collect a full list
        of price quotes and writing the data to a JSON
        file named quotes.json saved to the ticker_data directory.  
        If the ticker_data directory doesn't exist prior to the 
        method being ran, it will automatically create
        the directory.  The method will automatically rerun every
        600 seconds to retrieve the latest price quotes available.
        """

        self.sym_lst = sym_lst

        self.priceData = [self.price_data.current(symbol) for symbol in self.sym_lst]

        self.priceData = (
            {
                "name":equity["info"]["name"], 
                "symbol":equity["info"]["symbol"],
                "close":equity["current"]["Close"],
                "change_amount":equity["current"]["Change Amount"],
                "change_rate":equity["current"]["Change Rate"]   
            } 
            for equity in self.priceData
        )

        self.symbol_color = "#1D99EB"
        self.name_color = "#ffffff"
        self.close_color = "#ffffff"
        self.lag_color = "#F20505"
        self.gain_color = "#84BF04"
        self.even_color = "#ffffff"

        self.quote_data = []

        for quote in list(self.priceData):

            payload = {}

            payload["symbol"] = f'<span id="symbol" style="color:{self.symbol_color};">&nbsp;&nbsp;&nbsp;&nbsp;{quote["symbol"]}</span>'
            payload["name"] = f'<span id="name" style="color:{self.name_color};">{quote["name"]}</span>'
            payload["close"] = f'<span id="close" style="color:{self.close_color};">$ {str(quote["close"])}</span>'
            payload["change_amount"] = quote["change_amount"]

            try:
                payload["change_rate"] = str(round((quote["change_rate"] * 100), 3))
            except:
                payload["change_rate"] = '- null -'

            if float(payload["change_amount"]) < 0:
                payload["change_amount"] = f'<span class="lag" style="color:{self.lag_color};">$ {str(payload["change_amount"])}</span>'
                payload["change_rate"] = f'<span class="lag" style="color:{self.lag_color};">{str(payload["change_rate"])}%</span>'
            elif float(payload["change_amount"]) > 0:
                payload["change_amount"] = f'<span class="gain" style="color:{self.gain_color};">$ {str(payload["change_amount"])}</span>'
                payload["change_rate"] = f'<span class="gain" style="color:{self.gain_color};">{str(payload["change_rate"])}%</span>'
            else:
                payload["change_amount"] = f'<span class="even" style="color:{self.even_color};">$ {str(payload["change_amount"])}</span>'
                payload["change_rate"] = f'<span class="even" style="color:{self.even_color};">{str(payload["change_rate"])}%</span>'

            self.quote_data.append(payload)

        try:
            os.makedirs(f"{str(Path.cwd())}/ticker_data")
        except:
            pass

        file_str = f"{str(Path.cwd())}/ticker_data/quotes.json"

        with open(file_str, "w") as fileObj:
            json.dump(self.quote_data, fileObj, indent=4)

        return

    @st.experimental_fragment(run_every=45)
    def ticker(self):

        """
        The `ticker` class generates a live stock
        ticker in Streamlit applications by reading
        the JSON file saved to the ticker_data directory.
        The ticker will automatically rerun every 45 seconds
        to get price updates from the quotes.json file.
        """

        try:
            file_str = f"{str(Path.cwd())}/ticker_data/quotes.json"

            with open(file_str, "r") as fileObj:
                self.ticker_data = json.load(fileObj)
        except:
            print("=====   TICKER DATA UNAVAILABLE   =====")
            return

        self.ticker_height = str(round((2.5 * .85), 2))
        self.top_padding = str(round((.5 * .6), 2))
        self.font_size = str(round((2.75 * .6), 2))

        self.brkt_open = "{"
        self.brkt_close = "}"

        self.style = f"""
            <style>
                marquee {self.brkt_open}
                    background-color:#000000;
                    color:#000000;
                    height:{self.ticker_height}em;
                    padding-top:{self.top_padding}em;
                    font-size:{self.font_size}em;
                    font-weight:800;
                    font-family:Helvetica;
                    box-shadow:rgba(0, 0, 0, .35) 0px 6px 6px 0px;
                    border-radius:5px;
                {self.brkt_close}
            </style>
        """

        st.html(f"""
            <div>
                {self.style}
                <div>
                    <marquee direction="left" scrollamount="2">
                        {["&nbsp;&nbsp;&nbsp;".join([payload[quote] for quote in payload.keys()]) for payload in self.ticker_data]}
                    </marquee>
                </div>
            </div>
        """)

        return

    @st.experimental_fragment()
    def start(self, syms):

        """
        The `start` class is used to initiate all processes
        required to the generate a live stock ticker in a Streamlit
        application.  Its primary purpose is to ensure processes
        are executed in the correct order for the purpose of generating 
        the visualization in a Streamlit application with acceptable
        amount of delay.
        """

        self.syms = syms

        if self.syms == None and type(self.syms) is not list:
            print("=====   ERROR: UNKNOWN ERROR   ===")
            return
        else:
            pass

        if len(self.syms) >= 5:
            self.get_quotes_temp(self.syms)
            self.ticker()
            self.get_quotes(self.syms)
            return
        elif len(self.syms) > 100:
            print("=====   ERROR: STOCK SYMBOLS EXCEEDS LIMIT OF 100 SYMBOLS - REDUCE LIST SIZE AND TRY AGAIN   =====")
            return
        else:
            self.get_quotes(self.syms)
            self.ticker()
            return
