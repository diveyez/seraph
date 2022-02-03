# Charts Grabber Code
# Author: @diveyez
# without the time.sleep(30) or time.sleep(60)
# this module consumes lots of API uses at TwelveData
#
from seraph_vars import TOKEN1
from seraph_vars import *
import plotly.graph_objects as go  # or plotly.express as px
import nasdaqdatalink
import mplfinance as mf
import pandas as pd
from twelvedata import TDClient
import plotly.express as px
import plotly
import plotly.io as pio
import twelvedata
from json import loads
import json
import requests
import os
import time
import sys
###########################################
###########################################
# Symbol Selection
###########################################
ticker_symbol = input("What Ticker:")
# WRITE TO FILE
f = open('seraph_pid.txt', "w")
f.write(
        ticker_symbol
)
f.close()
#print(ticker_symbol)  # DO NOT UNCOMMENT
print("Ticker is:" + ticker_symbol)
############################################
# Twelvedata Token
token_selected = input("What Token (TOKEN1,TOKEN2,TOKEN3,TOKEN4)?:")
## WRITE TO FILE
f = open('selected_token.txt', "w")
f.write(
        token_selected
)
#print(token_selected)  # DO NOT UNCOMMENT
f.close()
print("Token Selected:" + token_selected)
## READING THE SELECTED TOKEN
f = open('selected_token.txt', 'r')
f.read()
print("Token Selected:",
      tok_sel
      )
# define which token
td = TDClient(apikey=tok_sel)

###################################################################
print("Imported API key....")
###################################################################
###################################################################
# There is 8 charts, 4 sets being made
# 1,5,15,30 minutes
# two of each with different strategies and indicators
# The files are renamed after the write
# This set of charts is meant to be simple, and used for small detail images
# in things like blog posts or articles and not intended for usage trading
# Charts are as a Time Series in Plotly Figures
# Source: twelvedata-client
# Time Series Documentation: https://twelvedata.com/docs#time-series
ts = td.time_series(
              symbol=ticker_symbol,
              interval="1min",
              outputsize=120,).with_vwap().with_ema(time_period=24).with_floor().as_plotly_figure().write_image("data/images/time_series_plots/1min/chart_1min_1.png")
## Rename the image for organization
symbol = ticker_symbol
imagename = "%s_1min_1.png" % symbol
os.rename('data/images/time_series_plots/1min/chart_1min_1.png',
          "data/images/time_series_plots/1min/%s_1min_1.png" % symbol)
time.sleep(30)
# For Testing
# print(imagename)

# TIME SERIES CHAIN IMAGE CREATION
time.sleep(30)
ts = td.time_series(
        symbol=ticker_symbol,
        interval="1min",
        outputsize=120,).with_stochrsi().with_bbands().with_percent_b().as_plotly_figure().write_image("data/images/time_series_plots/1min/chart_1min_2.png")
time.sleep(30)
symbol = ticker_symbol
imagename = "%s_1min_2.png" % symbol
os.rename('data/images/time_series_plots/1min/chart_1min_2.png',
          "data/images/time_series_plots/1min/%s_1min_2.png" % symbol)
time.sleep(30)
# Construct the necessary time series
ts = td.time_series(
        symbol=ticker_symbol,
        interval="5min",
        outputsize=150,).with_vwap().with_ema(time_period=72).with_floor().as_plotly_figure().write_image("data/images/time_series_plots/1min/chart_5min_1.png")
symbol = ticker_symbol
imagename = "%s_5min_1.png" % symbol
os.rename('data/images/time_series_plots/5min/chart_5min_1.png',
          "data/images/time_series_plots/5min/%s_5min_1.png" % symbol)
time.sleep(30)
# Construct the necessary time series
ts = td.time_series(
        symbol=ticker_symbol,
        interval="5min",
        outputsize=150,).with_stochrsi().with_bbands().with_percent_b().as_plotly_figure().write_image("data/images/time_series_plots/1min/chart_5min_2.png")
symbol = ticker_symbol
imagename = "%s_5min_2.png" % symbol
os.rename('data/images/time_series_plots/5min/chart_5min_2.png',
          "data/images/time_series_plots/5min/%s_5min_2.png" % symbol)
time.sleep(30)
# Construct the necessary time series
ts = td.time_series(
        symbol=ticker_symbol,
        interval="15min",
        outputsize=45,).with_vwap().with_ema(time_period=128).with_floor().as_plotly_figure().write_image("data/images/time_series_plots/1min/chart_15min_1.png")
# Construct the necessary time series
ts = td.time_series(
        symbol=ticker_symbol,
        interval="15min",
        outputsize=45,).with_stochrsi().with_bbands().with_percent_b().as_plotly_figure().write_image("data/images/time_series_plots/1min/chart_15min_2.png")
time.sleep(30)
# Construct the necessary time series
ts = td.time_series(
        symbol=ticker_symbol,
        interval="30min",
        outputsize=45,).with_vwap().with_ema(time_period=24).with_floor().as_plotly_figure().write_image("data/images/time_series_plots/1min/chart_30min_1.png")
time.sleep(30)
# Construct the necessary time series
ts = td.time_series(
        symbol=ticker_symbol,
        interval="30min",
        outputsize=45,).with_stochrsi().with_bbands().with_percent_b().as_plotly_figure().write_image("data/images/time_series_plots/1min/chart_30min_2.png")
time.sleep(30)
print("Finished Plotting")
print("Image File can be located at data/images/time_series_plots")
f.close()
f.close()