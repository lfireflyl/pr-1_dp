import csv
import re

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.csv"

ALLOWED_DOMAINS = [
    "yandex.ru",
    "mail.ru",
    "mirea.ru",
    "edu.mirea.ru",
    "bk.ru",
]

COLUMN_INDEX = 6


def is_allowed_email(email):
    email = email.strip().lower()

    if "@" not in email:
        return False

    domain = email.rsplit("@", 1)[1]

    return domain in {d.lower().lstrip("@") for d in ALLOWED_DOMAINS}


with open(INPUT_FILE, "r", encoding="utf-8-sig", newline="") as infile:
    reader = csv.reader(infile)

    rows = list(reader)


for row in rows[1:]:
    if len(row) <= COLUMN_INDEX:
        continue

    emails = row[COLUMN_INDEX].split(",")

    allowed_emails = [
        email.strip()
        for email in emails
        if is_allowed_email(email)
    ]

    row[COLUMN_INDEX] = ", ".join(allowed_emails)


with open(OUTPUT_FILE, "w", encoding="utf-8-sig", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerows(rows)

print(f"Готово. Результат сохранён в {OUTPUT_FILE}")