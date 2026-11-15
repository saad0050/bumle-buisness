import re

# Mønster der finder par af typen key=value.
# Værdien er enten tekst i citationstegn (fx msg="...") eller ét ord uden mellemrum.
PATTERN = re.compile(r'(\w+)=("[^"]*"|\S+)')


def parse_line(line):
    """Laver én logline om til en ordbog med navn og værdi."""
    timestamp, rest = line.split(" ", 1)   # første ord er tidspunktet
    row = {"timestamp": timestamp}
    for key, value in PATTERN.findall(rest):
        row[key] = value.strip('"')         # fjern citationstegn om msg
    return row




def load_log(file_path):
    """Læser logfilen og håndterer fejl, hvis filen mangler."""
    rows = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                # Kontrollér om loglinjen indeholder de nødvendige felter
                if not all(field + "=" in line for field in ["level", "event", "user", "src_ip"]):
                    print("ADVARSEL: Springer en loglinje over med forkert format.")
                    continue

                rows.append(parse_line(line))

    except FileNotFoundError:
        print("FEJL: Logfilen blev ikke fundet.")
        return []

    return rows

