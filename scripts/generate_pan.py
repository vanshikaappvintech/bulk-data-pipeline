#!/usr/bin/env python3
import random
import json
import re
from stdnum.in_.pan import is_valid as pan_is_valid

# ----------------------------
# 1. PAN generators & validators
# ----------------------------
PAN_REGEX = re.compile(r'^[A-Z]{5}[0-9]{4}[A-Z]$')

def gen_base_pan():
    """Generate a valid uppercase PAN: 5 letters, 4 digits, 1 letter."""
    letters = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5))
    digits  = ''.join(str(random.randint(0,9)) for _ in range(4))
    last    = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return letters + digits + last

def is_valid_pan(value):
    """
    Validate using python-stdnum.  This applies the same
    format/structure checks (no check-digit) but via stdnum.
    """
    return pan_is_valid(value)

# ----------------------------
# 2. Variation functions
# ----------------------------
def plain(pan):
    return pan

def lowercase(pan):
    return pan.lower()

def mixed_case(pan):
    return ''.join(ch.lower() if random.random()<0.5 else ch for ch in pan)

def embedded(pan):
    return pan  # sentence will prepend context

def with_spaces(pan):
    # AB CDE 1234 F
    return f"{pan[0:2]} {pan[2:5]} {pan[5:9]} {pan[9]}"

def wrong_format(pan):
    # shuffle last five to break pattern
    core = list(pan[5:])
    random.shuffle(core)
    return pan[:5] + ''.join(core)

def with_dash(pan):
    # AB-CDE-1234-F
    return f"{pan[0:2]}-{pan[2:5]}-{pan[5:9]}-{pan[9]}"

def alt_label(pan):
    return pan  # label added in template

VARIATIONS = {
    "plain":       plain,
    "lowercase":   lowercase,
    "mixed_case":  mixed_case,
    "embedded":    embedded,
    "with_spaces": with_spaces,
    "wrong_format":wrong_format,
    "with_dash":   with_dash,
    "alt_label":   alt_label,
}

# ----------------------------
# 3. Real-world sentence templates
#    Must include at least one of your context keywords:
#      pan, permanent account number, tax id, income tax, e-pan,
#      taxpayer id, taxpayer identification number, tax identification number
# ----------------------------
TEMPLATES = {
    "plain": [
        "Her permanent account number for income tax filing is {v}",
        "Please verify PAN {v} with the Income Tax Department",
        "This e-PAN reference {v} is saved under your tax id",
    ],
    "lowercase": [
        "We record your pan in lowercase as {v} in the system",
        "User entered taxpayer id in lowercase as {v}",
    ],
    "mixed_case": [
        "The taxpayer identification number appears as {v} in your dashboard",
        "Your tax identification number is stored as {v}",
    ],
    "embedded": [
        "PAN: {v} must match your permanent account number on record",
        "Your tax id number is {v} according to income tax records",
    ],
    "with_spaces": [
        "Enter your permanent account number like {v} without dashes",
        "System expects tax id in this spaced format {v}",
    ],
    "wrong_format": [
        "The value {v} is not a valid PAN or taxpayer id format",
        "Please correct your tax identification number from {v}",
    ],
    "with_dash": [
        "Some forms show e-PAN as {v}, please remove dashes",
        "Alternate PAN format seen {v} for your Income Tax profile",
    ],
    "alt_label": [
        "pan number {v} added to your profile as your tax id",
        "taxpayer identification number {v} is registered under your name",
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_pan_variations(count=50):
    records = []
    keys = list(VARIATIONS.keys())

    while len(records) < count:
        base    = gen_base_pan()
        key     = random.choice(keys)
        variant = VARIATIONS[key](base)
        text    = random.choice(TEMPLATES[key]).format(v=variant)

        records.append({
            "text":      text,
            "pan":       variant,
            "variation": key,
            "is_valid":  is_valid_pan(variant)
        })

    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_pan_variations(count=50)
    with open("pan_numbers.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ pan_numbers.json generated with realistic sentences and full context coverage.")
