import regex
import requests
import pandas as pd
from io import StringIO
from sys import argv
from datetime import datetime
from rich.console import Console


console = Console()


def colect_data(ticker: str, start_timestamp: int, end_timestamp: int, interval: str):
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0'
    } 

    url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}.SA?period1={start_timestamp}&period2={end_timestamp}&interval={interval}"
    content = requests.get(url=url, headers=hdr).text.strip()

def convert_data_to_timestamp(start_data: str, end_data: str):
    start_data_timestamp = int(datetime.strptime(start_data, "%d/%m/%Y").timestamp())
    end_data_timestamp = int(datetime.strptime(end_data, "%d/%m/%Y").timestamp())

    return start_data_timestamp, end_data_timestamp


if __name__ == "__main__":
    if "--start_data" in argv and "--end_data" in argv and "--file" in argv:
        param_1 = argv.index('--start_data')
        param_2 = argv.index('--end_data')
        param_3 = argv.index('--file')

        start_timestamp, end_timestamp = convert_data_to_timestamp(start_data=argv[param_1+1], end_data=argv[param_2+1])
        colect_data(ticker='PETR4', start_timestamp=start_timestamp, end_timestamp=end_timestamp, interval='1d')
    
    else:
        console.print(f"\nComo usar: python [italic bold yellow]{argv[0]}[/] [green]--file[/] ativos.txt [green]--start_data[/] 01/01/2020 [green]--end_data[/] 01/01/2024\n")

