from datetime import datetime
from json import load
from tqdm import tqdm
from pandas import read_excel, isna, to_numeric, ExcelWriter
from yfinance import Ticker
from sys import argv, exit
# check for if price[today] is numeric
# check if today and yesterday works as inputs



"""
    import data
"""

with open('config.json', 'r') as f: config = load(f)
df = read_excel(config["workbook-path"], sheet_name=config["main"]).set_index("Ticker")
df.sort_index(inplace=True)

"""
    Make a list of old dates for the newly added tickers
"""

newTickers = []

for ticker, values in df[df.isnull().any(axis=1)].iterrows():
    dates = values[values.isnull()].index.to_list()
    newTickers.extend([(ticker, i) for i in dates])



"""
    set config data
"""

dated = argv[1]
if dated not in ["today", "yesterday"]:
    try:
        weekend = False
        if datetime.strptime(dated, '%Y-%m-%d').weekday() not in [0, 1, 2, 3, 4]: weekend = True
    except: raise Exception("Date is not is the correct format")
    if weekend: raise Exception("Date is a weekend")

bse = config["BSE"]
index = config["Index"]



"""
    function to apply new prices on tickers
"""

def fetchPrices(ticker: str, dated: str) -> float:

    if ticker in bse:
        ticker = f"{ticker}.BO"
    elif ticker in index:
        ticker = f"^{ticker}"
    elif isna(ticker):
        return "ERROR: no ticker found"
    else:
        ticker = f"{ticker}.NS"
    
    price = Ticker(ticker).history(start=dated)["Close"]

    if price.size == 0: return "ERROR: no data for this ticker found"
    if dated not in price.index: return "ERROR: no data for this date found"

    return round(price[dated], 2)


for (ticker, dated) in tqdm(newTickers, desc="Fetching for new Tickers"):
    df.loc[ticker, dated] = fetchPrices(ticker, dated)

tqdm.pandas(desc=f"Fetching Stock Prices for {dated}")
df[dated] = df.index.to_series().progress_apply(lambda ticker: fetchPrices(ticker, dated))



"""
    Calculating cost price
"""

pnl = read_excel(config["workbook-path"], sheet_name=config["purchase-history"]).set_index("Ticker").iloc[:, :2]
pnl = pnl.merge(
            df[max(df.columns)],
            how="left",
            left_index=True, right_index=True,
)
pnl[max(df.columns)] = to_numeric(pnl[max(df.columns)], errors="coerce")
pnl["PnL per share"] = pnl[max(df.columns)] - pnl["Price"]
pnl["Total PnL"] = pnl["PnL per share"] * pnl["Quantity"]



"""
    write the final output
"""

order = sorted(df.columns)

with ExcelWriter(config["workbook-path"], engine='openpyxl', mode='a', if_sheet_exists="replace") as writer:
    df[order].to_excel(writer, sheet_name=config["main"])
    pnl.to_excel(writer, sheet_name=config["purchase-history"])
print("Executed Successfully")


