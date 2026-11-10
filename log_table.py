import pandas as pd


def create_table(rows):
    """Laver listen af ordbøger om til en pandas-tabel (DataFrame)."""
    table = pd.DataFrame(rows)
    # Gør tidspunktet til rigtigt tidspunkt, så vi kan sortere og plotte på det senere
    table["timestamp"] = pd.to_datetime(table["timestamp"])
    # Gør porten til et tal, så den kan bruges på en akse
    table["dest_port"] = pd.to_numeric(table["dest_port"])
    return table
def filter_by_level(table, level):
    """Returnerer kun de rækker, hvor level matcher, fx 'ALERT'."""
    return table[table["level"] == level]

def count_per_hour(table):
    """Tæller antal rækker pr. time og returnerer tallene som en serie."""
    # floor("h") runder hvert tidspunkt ned til hele timer, fx 08:03 bliver 08:00
    return table.groupby(table["timestamp"].dt.floor("h")).size()