import pandas as pd

from log_loader import load_log
from log_table import create_table, filter_by_level, count_per_hour
from log_plots import plot_scatter, plot_bar

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
#plot_scatter(table, "user", "event")

# Undersøg de to IP-adresser, der kun optræder ved port 443
rare_ips = ["203.0.113.250", "198.51.100.200"]
print(table[table["src_ip"].isin(rare_ips)])

# Hvor mange gange optræder hver IP?
#plot_scatter(table, "timestamp", "src_ip")
# Tæl mislykkede logins pr. time og vis som søjlediagram
failed_logins = table[table["event"] == "LOGIN_FAILED"]
failed_per_hour = count_per_hour(failed_logins)
#plot_bar(failed_per_hour, "Mislykkede logins pr. time", "Time", "Antal LOGIN_FAILED")

# Find hændelser, hvor malware er registreret
malware_events = table[table["event"] == "MALWARE_SIGNATURE_MATCH"]

print(malware_events)

malware_counts = malware_events["src_ip"].value_counts()

plot_bar(malware_counts, "Malware-hændelser pr. IP-adresse", "IP-adresse", "Antal malware-hændelser")
