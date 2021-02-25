import pandas as pd

path_gabarito = 'csv/csv1.csv'
path_backtest = 'csv/csv2.csv'
get_columns_from_gabarito = ['a', 'e']

""""
    keys não correspondentes no gabarito são deletadas no backteste
    se não existir a coluna no gabarito o programa crasha
"""
def permuta(from_gabarito, to_backtest, columns):
    df_gabarito = pd.read_csv(from_gabarito)
    df_backtest = pd.read_csv(to_backtest)

    primary_key = ['ndoc', 'dt_t0']
    if primary_key[1] not in df_backtest.columns or primary_key[1] not in df_gabarito.columns:
        primary_key = ['ndoc']



    print(df_backtest)


if __name__ == '__main__':
    permuta(path_gabarito, path_backtest, get_columns_from_gabarito)
