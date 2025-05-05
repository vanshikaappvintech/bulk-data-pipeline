#!/usr/bin/env python3
import random
import json
import string
import re

# ----------------------------
# 1. IMEI generators & validators
# ----------------------------
def gen_base_imei():
    """Generate 14 random digits; compute Luhn check digit for the 15th."""
    base = ''.join(str(random.randint(0, 9)) for _ in range(14))
    return base + str(calc_luhn_check(base))

def calc_luhn_check(digits):
    """Compute Luhn check digit for a string of numeric digits."""
    total = 0
    # IMEI uses right-to-left doubling starting from second-to-last
    for i, ch in enumerate(reversed(digits)):
        d = int(ch)
        if i % 2 == 0:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return (10 - (total % 10)) % 10

def is_valid_imei(s):
    """Strip non-digits, check length 15 and Luhn validity."""
    digits = ''.join(ch for ch in s if ch.isdigit())
    if len(digits) != 15:
        return False
    return calc_luhn_check(digits[:-1]) == int(digits[-1])

# ----------------------------
# 2. Variation functions
# ----------------------------
def plain_scientific(imei):
    return f"{int(imei):.5E}"

def with_spaces(imei):
    return ' '.join([imei[:2], imei[2:6], imei[6:10], imei[10:]])

def with_dashes(imei):
    return '-'.join([imei[:2], imei[2:6], imei[6:10], imei[10:]])

def grouped_5(imei):
    return '-'.join([imei[:5], imei[5:10], imei[10:]])

def with_label(imei):
    return f"IMEI: {imei}"

def embedded(imei):
    return imei

def short_scientific(imei):
    # first 13 digits scientific
    num = int(imei[:-1])
    return f"{num:.5E}"

def with_check_digit(imei):
    return f"{imei} (Luhn OK)"

def word_breaks(imei):
    # group of 4 then 4 then 4 then 3
    return ' '.join([imei[:4], imei[4:8], imei[8:12], imei[12:]])

def hex_hint(imei):
    return "0x" + imei

def imei_sv(imei):
    # scientific E+16
    num = int(imei)
    return f"{num:.5E}".replace('E+14','E+16')

VARIATIONS = {
    "plain_scientific": plain_scientific,
    "with_spaces":      with_spaces,
    "with_dashes":      with_dashes,
    "grouped_5":        grouped_5,
    "with_label":       with_label,
    "embedded":         embedded,
    "short_scientific": short_scientific,
    "with_check_digit": with_check_digit,
    "word_breaks":      word_breaks,
    "hex_hint":         hex_hint,
    "imei_sv":          imei_sv,
}

# ----------------------------
# 3. Contextual sentence templates
# ----------------------------
TEMPLATES = {
    "plain_scientific": [
        "Your mobile serial number in Excel shows as {v}.",
        "The device IMEI number appears as {v}.",
    ],
    "with_spaces": [
        "Please note the cellular device id {v}.",
        "Your unique device id is recorded as {v}.",
    ],
    "with_dashes": [
        "We have your device identifier logged as {v}.",
        "The IMEI for your mobile is {v}.",
    ],
    "grouped_5": [
        "For readability, the device address is {v}.",
        "Your device tracking id appears as {v}.",
    ],
    "with_label": [
        "IMEI: {v}",
        "Device IMEI is {v}",
    ],
    "embedded": [
        "My phone's IMEI is {v}.",
        "Please verify the IMEI number {v}.",
    ],
    "short_scientific": [
        "The client’s IMEI in E notation is {v}.",
        "Your cellular device id shows as {v}.",
    ],
    "with_check_digit": [
        "Confirm that {v} matches the device IMEI.",
        "Verified IMEI number is {v}.",
    ],
    "word_breaks": [
        "Enter the IMEI number as {v}.",
        "The device address field contains {v}.",
    ],
    "hex_hint": [
        "Hex hint for IMEI is {v}.",
        "Your device identifier in hex is {v}.",
    ],
    "imei_sv": [
        "The IMEI SV appears as {v}.",
        "Service version IMEI number is {v}.",
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_imei_variations(count=50):
    records = []
    keys = list(VARIATIONS.keys())
    while len(records) < count:
        imei = gen_base_imei()
        key  = random.choice(keys)
        variant = VARIATIONS[key](imei)
        tmpl    = random.choice(TEMPLATES[key])
        text    = tmpl.format(v=variant)
        records.append({
            "text":        text,
            "imei":        variant,
            "variation":   key,
            "is_valid":    is_valid_imei(variant)
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_imei_variations(count=50)
    with open("imei_numbers.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ imei_numbers.json generated with full-context, real-world sentences.")
