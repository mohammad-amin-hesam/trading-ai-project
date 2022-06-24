# import pandas as pd
import tpqoa

api = tpqoa.tpqoa("oanda.cfg")

print(api.get_history(instrument = "EUR_USD", start = "2020-07-01", end = "2020-07-31", granularity = "D", price = "A"))