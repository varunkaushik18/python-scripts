import yfinance as yf

debug_print_enable = 0

company_name_index = 0
previous_close_index = 1
day_low_index = 2
day_high_index = 3
ask_price_index = 4
bid_price_index = 5

file_header = ["Company Name", "Previous Close", "Day Low", "Day High", "Ask", "Bid"]
ticker_list = ["", "", "", "", "", ""]

myStocks = [yf.Ticker('ASIANPAINT.NS'), yf.Ticker('RELIANCE.NS'), yf.Ticker('HDFCBANK.NS'), yf.Ticker('INFY.NS'), yf.Ticker('HINDUNILVR.NS'), yf.Ticker('ITC.NS'), yf.Ticker('TITAN.NS'), yf.Ticker('BHARTIARTL.NS'), yf.Ticker('HDFCLIFE.NS'), yf.Ticker('IRCTC.NS')]

def _debug_print(line):
    if debug_print_enable == 1:
        print(line)

def write_line_to_csv(line):
    csv_file = open("Stock-O-Meter.csv", "a+")
    csv_file.write(line)
    csv_file.close()


if __name__ == "__main__":
    csv_file = open("Stock-O-Meter.csv", "w+")
    csv_file.close()
    line_to_file = ""
    for j in file_header:
        line_to_file = line_to_file + str(j)+","
    line_to_file = line_to_file + "\n"
    write_line_to_csv(line_to_file)

    for i in myStocks:
        stockinfo = i.info

        for key,value in stockinfo.items():
            #_debug_print(str(key) +" : "+ str(value))
            if key == "shortName":
                _debug_print(str(value))
                ticker_list[company_name_index] = str(value)
            elif key == "previousClose":
                _debug_print("Previous close = "+str(value))
                ticker_list[previous_close_index] = str(value)
            elif key == "bid":
                _debug_print("bid = "+str(value))
                ticker_list[bid_price_index] = str(value)
            elif key == "ask":
                _debug_print("ask = "+str(value))
                ticker_list[ask_price_index] = str(value)
            elif key == "dayHigh":
                _debug_print("Day High = "+str(value))
                ticker_list[day_high_index] = str(value)
            elif key == "dayLow":
                _debug_print("Day Low = "+str(value))
                ticker_list[day_low_index] = str(value)
        line_to_file = ""
        for j in ticker_list:
            line_to_file = line_to_file + j+","
        line_to_file = line_to_file + "\n"
        write_line_to_csv(line_to_file)