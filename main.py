with open("data/cyber_security_log_sample.txt", "r", encoding="utf-8") as fil:
    for i, linje in enumerate(fil):
        print(linje)
        if i == 4:
            break