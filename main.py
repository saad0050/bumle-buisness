
import pandas as pd

from log_loader import load_log
from log_table import create_table, filter_by_level, count_per_hour, count_events, count_levels
from log_plots import plot_scatter, plot_bar


# Gør tabellerne mere overskuelige i terminalen
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)


# 1. INDLÆSNING AF LOGDATA

print("\n=== BUMLE BUSINESS – VPN-LOGOVERVÅGNING ===")

logs = load_log("data/cyber_security_log_sample.txt")

# Stop programmet, hvis logfilen mangler eller er tom
if not logs:
    print("Programmet afsluttes, fordi der ikke er nogen logdata.")
    exit()

table = create_table(logs)

print("\n=== OVERSIGT OVER LOGDATA ===")
print("Antal rækker og kolonner:", table.shape)
print(table.head(10))


# 2. KONTROL AF LOGDATA

print("\n=== KONTROL AF LOGDATA ===")
print("Ugyldige portnumre:", table["dest_port"].isna().sum())
print("Ugyldige tidspunkter:", table["timestamp"].isna().sum())


# 3. SIKKERHEDSALARMER

alerts = filter_by_level(table, "ALERT")

print("\n=== SIKKERHEDSALARMER ===")
print("Antal ALERT-hændelser:", len(alerts))
print(alerts)


# 4. ANALYSE AF MISTÆNKELIGE IP-ADRESSER

print("\n=== MISTÆNKELIGE IP-ADRESSER ===")

rare_ips = ["203.0.113.250", "198.51.100.200"]
print(table[table["src_ip"].isin(rare_ips)])

# Analyse af scatter-plots:
# De fleste IP-adresser har aktiviteter fordelt over hele tidsperioden.
# IP-adressen 203.0.113.250 har 18 mislykkede loginforsøg på kort tid.
# IP-adressen 198.51.100.200 har 3 malware-alarmer på forskellige servere.
# Hændelserne ligger tæt på hinanden tidsmæssigt og er mistænkelige.
# Scatter-plots viser mønstrene, men beviser ikke, at et angreb lykkedes.


# 5. OPTÆLLING AF HÆNDELSER

event_counts = count_events(table)
level_counts = count_levels(table)

print("\n=== HÆNDELSER EFTER TYPE ===")
print(event_counts)

print("\n=== FORDELING AF SIKKERHEDSNIVEAUER ===")
print(level_counts)


# 6. TEST AF OPTÆLLINGER

assert event_counts.sum() == len(table)
print("TEST BESTÅET: Alle event-typer er talt korrekt.")

assert level_counts.sum() == len(table)
print("TEST BESTÅET: Alle sikkerhedsniveauer er talt korrekt.")


# 7. FORBEREDELSE AF DIAGRAMMER

failed_logins = table[table["event"] == "LOGIN_FAILED"]
failed_per_hour = count_per_hour(failed_logins)

malware_events = table[table["event"] == "MALWARE_SIGNATURE_MATCH"]
malware_counts = malware_events["src_ip"].value_counts()

top_ips = table["src_ip"].value_counts().head(10)


# 8. VISUALISERING AF LOGDATA

print("\n=== DIAGRAMMER ===")
print("Luk det aktuelle diagramvindue for at se det næste.")


# Diagram 1: Scatter-plot over IP-adresser og tidspunkt
plot_scatter(table, "timestamp", "src_ip")


# Diagram 2: Mislykkede loginforsøg pr. time
# Vi bruger søjlediagram, fordi det gør det nemt at sammenligne
# antallet af mislykkede loginforsøg og opdage usædvanlig aktivitet.

plot_bar(
    failed_per_hour,
    "Mislykkede logins pr. time",
    "Time",
    "Antal LOGIN_FAILED"
)


# Diagram 3: Malware-alarmer efter IP-adresse
plot_bar(
    malware_counts,
    "Sikkerhedsadvarsel: Registreret malware fordelt på IP-adresser",
    "IP-adresse",
    "Antal malware-alarmer"
)


# Diagram 4: Fordeling af sikkerhedsniveauer
plot_bar(
    level_counts,
    "Fordeling af sikkerhedsniveauer",
    "Sikkerhedsniveau",
    "Antal hændelser"
)


# Diagram 5: De 10 mest aktive IP-adresser
plot_bar(
    top_ips,
    "De 10 mest aktive IP-adresser",
    "IP-adresse",
    "Antal registreringer"
)


# Diagram 6: Fordeling af hændelsestyper
plot_bar(
    event_counts,
    "Fordeling af hændelsestyper",
    "Hændelsestype",
    "Antal registreringer"
)


print("\n=== PROGRAMMET ER AFSLUTTET ===")
