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
    """Læser hele logfilen og returnerer en liste med én ordbog pr. linje."""
    rows = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()             # fjern linjeskift i enderne
            if line == "":
                continue                    # spring tomme linjer over
            rows.append(parse_line(line))
    return rows