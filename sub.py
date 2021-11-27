import pandas as pd


def get_csv(csv_file):
    df_csv = pd.read_csv(csv_file)
    return df_csv


def say_hello(name):
    return f"Hi,{name}. How are you ?"
