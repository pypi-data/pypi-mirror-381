import os
import pandas as pd

def get_dfs(ohlc_path: str, period: str, interval: str) -> dict[pd.DataFrame]:
    """
    Retrieves OHLC DataFrame from main ohlc folder (ohlc_csv). Returns dictionary of DataFrames 
    matching specific period and interval
    """
    dfs = {}
    for file in os.listdir(f'{ohlc_path}/{interval}/'):

        split = file.split('_')
        symbol = split[0]
        datetime_col = 'Datetime' if 'd' not in interval else 'Date'
        
        if len(split) > 3:
            if period != split[1:3] and interval != split[-1]:
                continue
        elif len(split) < 3:
            if period != split[1] and interval != split[-1]:
                continue

        df = pd.read_csv(f'{ohlc_path}/{interval}/{symbol}_{period}_{interval}.csv')
        df = df.set_index(datetime_col)
        df.index = pd.to_datetime(df.index)

        dfs[symbol] = df
        # dfs[split[0]] = pd.read_csv(f'{ohlc_path}/{interval}/{split[0]}_{period}_{interval}.csv')

    return dfs


def get_line_numbers(path: str, target_lines: list[str]):
    """
    Read a text or py file and return the line numbers for target lines.
    """
    target_line_numbers = []
    with open(path, 'r', encoding='utf-8') as file:
        for target in target_lines:
            file.seek(0)
            for line_num, line in enumerate(file, 1):
                if target in line:
                    target_line_numbers.append(line_num)


    return target_line_numbers

