import pandas as pd

from log_loader import load_log
from log_table import create_table, filter_by_level
from log_plots import plot_scatter


# Vis alle kolonner og brug en bred visning i stedet for at skjule dem med "..."
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

# Indlæs hele logfilen i programmets hukommelse
logs = load_log("data/cyber_security_log_sample.txt")

# Lav data om til en tabel og vis de første 10 rækker
table = create_table(logs)
print(table.head(10))
print("Antal rækker og kolonner:", table.shape)

# Vis kun alarmerne
alerts = filter_by_level(table, "ALERT")
print("Antal ALERT-hændelser:", len(alerts))
print(alerts)

# Første forsøg: hvilke porte bliver brugt over tid?
plot_scatter(table, "timestamp", "dest_port")