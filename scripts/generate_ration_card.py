#!/usr/bin/env python3
import random
import json
import re
import string

# ----------------------------
# 1. Ration Card generators & validators
# ----------------------------
# Assume valid format: 2 letters + 2 digits + 2 letters + 4 digits + 4 digits, e.g. MH12RT1234 5678
RC_REGEX = re.compile(r'^[A-Z]{2}\d{2}[A-Z]{2}\d{4}\d{4}$', re.IGNORECASE)

def gen_base_rc():
    """Generate a synthetic but well‐formed ration card number."""
    state = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
    part1 = f"{random.randint(0,99):02d}"
    part2 = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
    part3 = f"{random.randint(0,9999):04d}"
    part4 = f"{random.randint(0,9999):04d}"
    return f"{state}{part1}{part2}{part3}{part4}"

def is_valid_rc(value):
    """Valid only if it matches the assumed pattern exactly."""
    cleaned = value.replace("-", "").replace(" ", "")
    return bool(RC_REGEX.fullmatch(cleaned))

# ----------------------------
# 2. Variation functions
# ----------------------------
def alphanumeric(rc):
    return rc

def numeric_scientific(rc):
    # drop letters and render digits in scientific E notation
    digits = re.sub(r'\D', '', rc)
    num = int(digits)
    return f"{num:.5E}"

def embedded(rc):
    return rc

def with_dashes(rc):
    # split into state(2), part1(2), part2+part3(6), part4(4)
    s, p1, p2p3, p4 = rc[:2], rc[2:4], rc[4:10], rc[10:]
    return f"{s}{p1}-{p2p3[:2]}{p2p3[2:]}-{p4}"

def with_spaces(rc):
    s, p1, p2p3, p4 = rc[:2], rc[2:4], rc[4:10], rc[10:]
    return f"{s}{p1} {p2p3[:2]}{p2p3[2:]} {p4}"

def alt_label(rc):
    return rc

VARIATIONS = {
    "alphanumeric":      alphanumeric,
    "numeric_scientific":numeric_scientific,
    "embedded":          embedded,
    "with_dashes":       with_dashes,
    "with_spaces":       with_spaces,
    "alt_label":         alt_label,
}

# ----------------------------
# 3. Real‑world sentence templates
# ----------------------------
TEMPLATES = {
    "alphanumeric": [
        "Your new ration card number has been issued as {v}",
        "The department records your ration card ID as {v}"
    ],
    "numeric_scientific": [
        "In our ledger the numeric part appears as {v}",
        "Some systems log the card digits in scientific form {v}"
    ],
    "embedded": [
        "Please refer to ration card {v} in your application",
        "Ration card number {v} must be quoted on all forms"
    ],
    "with_dashes": [
        "For verification use the formatted card number {v}",
        "Officials often write your ration card as {v}"
    ],
    "with_spaces": [
        "When you read it aloud you may say {v}",
        "The UI shows spaces in the card code like {v}"
    ],
    "alt_label": [
        "R.C. No. {v} is registered to your household",
        "The local office has your card entry under R.C. No. {v}"
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_ration_card_variations(count=50):
    records = []
    keys = list(VARIATIONS.keys())
    while len(records) < count:
        base = gen_base_rc()
        key = random.choice(keys)
        variant = VARIATIONS[key](base)
        template = random.choice(TEMPLATES[key])
        text = template.format(v=variant)
        records.append({
            "text":       text,
            "ration_card":variant,
            "variation":  key,
            "is_valid":   is_valid_rc(variant)
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_ration_card_variations(count=50)
    with open("ration_card_variations.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ ration_card_variations.json generated with all permutations")
