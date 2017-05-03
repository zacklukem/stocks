#!/usr/bin/env python3
from datetime import datetime
from pynet.network import *
from stockmanager.Portfolio import *
from stockmanager.Slot import *
from stockmanager.Util import *

NETWORK_HIDDEN_WIDTH = 3
NETWORK_HIDDEN_HEIGHT = 10

NETWORK_INPUTS = 120 + 4 # 120 days, balance, quartarly earning * 2, currentStocks

NETWORK_OUTPUTS = 1 # number of stocks to buy

STARTING_BALANCE = 10000

___network_hidden___ = []
for _ in range(NETWORK_HIDDEN_WIDTH):
    ___network_hidden___.append(NETWORK_HIDDEN_HEIGHT)

network = Network(NETWORK_INPUTS, ___network_hidden___, NETWORK_OUTPUTS)

balance = STARTING_BALANCE

stocks = getStockPrice("AAPL", datetime(2017, 4, 1), datetime(2017, 5, 1))
