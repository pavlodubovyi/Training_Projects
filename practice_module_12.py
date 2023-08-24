import csv

with open("eggs.csv", "w", newline="") as fh:
    spam_writer = csv.writer(fh)
    spam_writer.writerow(["Spam"] * 5 + ["Baked Beans"])
    spam_writer.writerow(["Spam", "Lovely Spam", "Wonderful Spam"])
