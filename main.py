from log_loader import load_log

logs = load_log("data/cyber_security_log_sample.txt")

print("Antal linjer indlæst:", len(logs))
print(logs[0])
