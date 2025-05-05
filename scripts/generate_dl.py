#!/usr/bin/env python3
import random
import json
import re
import string

# ----------------------------
# 1. Driving License generators & validators
# ----------------------------
DL_REGEX = re.compile(r'^(?i:DL)\d{13}$')

def gen_base_dl():
    """Generate a valid DL: 'DL' + 13 digits."""
    rto   = f"{random.randint(1, 99):02d}"
    year  = str(random.randint(1980, 2025))
    uniq  = f"{random.randint(0, 9999999):07d}"
    return "DL" + rto + year + uniq

def is_valid_dl(value):
    """Valid if matches modern DL format, case-insensitive."""
    clean = value.replace(" ", "").replace("-", "")
    return bool(DL_REGEX.fullmatch(clean))

# ----------------------------
# 2. Variation functions
# ----------------------------
def plain(dl):         return dl
def lowercase(dl):     return dl.lower()
def with_space(dl):    return dl[:2] + " " + dl[2:]
def with_dashes(dl):   return dl[:2] + "-" + dl[2:]
def old_format(dl):    return random.choice(["MH","KA","TN","UP","GJ"]) + dl[2:]
def embedded(dl):      return dl
def alt_label(dl):     return dl

VARIATIONS = {
    "plain":       plain,
    "lowercase":   lowercase,
    "with_space":  with_space,
    "with_dashes": with_dashes,
    "old_format":  old_format,
    "embedded":    embedded,
    "alt_label":   alt_label,
}

# ----------------------------
# 3. Sentence templates covering all context terms:
# driving license, dl, license number, license no,
# driver's license, motor vehicle license, rto id,
# road transport license, driving permit, vehicle license,
# learner's license, driver identification,
# transport license number, license card
# ----------------------------
TEMPLATES = {
    "plain": [
        "Her driving license {v} is valid for the driving permit record",
        "Please verify motor vehicle license {v} before issuing a road transport license",
        "The rto id {v} is on file under driver identification",
    ],
    "lowercase": [
        "The dl {v} appears in lowercase in the license card system",
        "Your license number {v} is stored under license no {v}",
        "The license card {v} detail is up to date",
    ],
    "with_space": [
        "Enter the road transport license as {v} in the online form",
        "Vehicle license entry reads {v} on the smart card",
        "The rto id recorded is {v} in the database",
    ],
    "with_dashes": [
        "Use transport license number {v} for verification at checkpoints",
        "Learner's license issued with code {v} expires next year",
        "The road transport license appears as {v} on the permit",
    ],
    "old_format": [
        "Old format detected {v} suggests an outdated driving license",
        "This appears to be a state DL code {v} rather than a modern license number",
        "Invalid vehicle license {v} likely from an old licensing system",
    ],
    "embedded": [
        "Driver's license {v} must be presented at the airport for travel",
        "Present your driver identification {v} when renewing the DL",
        "Show your driver's license {v} to access the government portal",
    ],
    "alt_label": [
        "License card {v} on file with the transport department",
        "Transport license number {v} was issued last month",
        "Vehicle license ID: {v} recorded in your profile",
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_dl_variations(count=50):
    records = []
    keys = list(VARIATIONS.keys())
    while len(records) < count:
        base    = gen_base_dl()
        key     = random.choice(keys)
        variant = VARIATIONS[key](base)
        text    = random.choice(TEMPLATES[key]).format(v=variant)
        records.append({
            "text":      text,
            "dl":        variant,
            "variation": key,
            "is_valid":  is_valid_dl(variant)
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_dl_variations(count=50)
    with open("driving_licenses.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ driving_licenses.json generated with all context terms included.")
