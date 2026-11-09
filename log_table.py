import pandas as pd


def create_table(rows):
    #Laver listen af ordbøger om til en pandas-tabel (DataFrame)."""
    table = pd.DataFrame(rows)
    # Gør tidspunktet til rigtigt tidspunkt, så vi kan sortere og plotte på det senere
    table["timestamp"] = pd.to_datetime(table["timestamp"])
    return table