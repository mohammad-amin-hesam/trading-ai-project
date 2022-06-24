import pandas as pd
import tpqoa

api = tpqoa.tpqoa("oanda.cfg")

# Long
api.create_order(instrument = "EUR_USD", units = 1000, sl_distance = 0.1)


# Short
api.create_order(instrument = "EUR_USD", units = -1000, sl_distance = 0.1)


# Short and Longs can be used for close an open order