import pandas as pd
import tpqoa

api = tpqoa.tpqoa("oanda.cfg")

# api.stream_data("EUR_USD", stop=10)
api.stream_data("EUR_USD")

# api.stop_stream()