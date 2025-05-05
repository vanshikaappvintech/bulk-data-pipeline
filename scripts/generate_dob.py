#!/usr/bin/env python3
import random
import json
from datetime import datetime, timedelta

# ----------------------------
# 1. DOB generator & validator
# ----------------------------
START_DATE = datetime(1950, 1, 1)
END_DATE   = datetime(2005, 12, 31)

def gen_random_dob():
    """Pick a random date between START_DATE and END_DATE."""
    delta = END_DATE - START_DATE
    return START_DATE + timedelta(days=random.randint(0, delta.days))

ACCEPTED_FORMATS = [
    "%d/%m/%Y",    # 01/01/1990
    "%d-%m-%Y",    # 01-01-1990
    "%Y-%m-%d",    # 1990-01-15
    "%d %b %Y",    # 01 Jan 1990
]

def is_valid_dob(s):
    """Attempt to parse s using each accepted format."""
    for fmt in ACCEPTED_FORMATS:
        try:
            datetime.strptime(s, fmt)
            return True
        except ValueError:
            continue
    return False

# ----------------------------
# 2. Variation functions
# ----------------------------
def plain(dt):        return dt.strftime("%d/%m/%Y")
def with_space(dt):   return dt.strftime("%d %m %Y")
def with_dashes(dt):  return dt.strftime("%d-%m-%Y")
def iso(dt):          return dt.strftime("%Y-%m-%d")
def words(dt):        return dt.strftime("%d %b %Y").lower()
def embedded(dt):     return dt.strftime("%d/%m/%Y")
def alt_label(dt):    return dt.strftime("%d-%m-%Y")

VARIATIONS = {
    "plain":       plain,
    "with_space":  with_space,
    "with_dashes": with_dashes,
    "iso":         iso,
    "words":       words,
    "embedded":    embedded,
    "alt_label":   alt_label,
}

# ----------------------------
# 3. Real-world sentence templates
#    Must include each context at least once across templates
# ----------------------------
TEMPLATES = {
    "plain": [
        "My date of birth is {v}.",
        "DOB recorded as {v}.",
        "I was born on {v}.",
        "My birth date is {v}.",
        "Year of birth: {v}.",
        "Month of birth and year: {v}.",
    ],
    "with_space": [
        "My birth day entry shows {v}.",
        "I entered my birth date as {v}.",
        "Birthdate entered: {v}.",
    ],
    "with_dashes": [
        "Her date of birth is {v}.",
        "Please verify my date of birth {v}.",
        "Date of birth: {v}.",
    ],
    "iso": [
        "My DOB in ISO format is {v}.",
        "I was born on {v}.",
        "Birthdate formatted as {v}.",
    ],
    "words": [
        "My birthday is {v}.",
        "I celebrate my anniversary of birth on {v}.",
        "Born on {v}.",
    ],
    "embedded": [
        "Her date of birth is {v} according to her records.",
        "Please check that she was born on {v}.",
        "The birth date listed is {v}.",
    ],
    "alt_label": [
        "Date of Birth: {v}.",
        "Birthdate: {v}.",
        "DOB: {v}.",
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_dob_variations(count=50):
    records = []
    keys = list(VARIATIONS.keys())
    while len(records) < count:
        dt      = gen_random_dob()
        key     = random.choice(keys)
        variant = VARIATIONS[key](dt)
        template= random.choice(TEMPLATES[key])
        text    = template.format(v=variant)
        records.append({
            "text":      text,
            "dob":       variant,
            "variation": key,
            "is_valid":  is_valid_dob(variant)
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_dob_variations(count=50)
    with open("dobs.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ dobs.json generated with full-context, real-world sentences.")
