#!/usr/bin/env python3
import random
import json
import re

# ----------------------------
# 1. IFSC generators & validators
# ----------------------------
BANK_CODES = ["SBIN", "HDFC", "ICIC", "AXIS", "PNB", "KARB"]
IFSC_REGEX = re.compile(r"^[A-Z]{4}0\d{6}$")

def gen_base_ifsc():
    """Generate a valid IFSC: 4 uppercase letters + '0' + 6 digits."""
    code = random.choice(BANK_CODES)
    digits = "".join(str(random.randint(0, 9)) for _ in range(6))
    return code + "0" + digits

def is_valid_ifsc(value):
    """Check uppercase‐normalized against the IFSC pattern."""
    v = value.replace(" ", "").replace("-", "")
    return bool(IFSC_REGEX.fullmatch(v.upper()))

# ----------------------------
# 2. Variation functions
# ----------------------------
def plain(code):          return code
def lowercase(code):      return code.lower()
def mixed_case(code):     
    return "".join(ch.upper() if random.random() < 0.5 else ch.lower() for ch in code)
def with_space(code):     return code[:4] + " " + code[4:]
def with_dash(code):      return code[:4] + "-" + code[4:]
def embedded(code):       return code
def missing_zero(code):   return code[:4] + code[5:]
def misplaced_sep(code):
    return code[:4] + "-" + code[5:8] + "-" + code[8:]
def alt_label(code):      return code

VARIATIONS = {
    "plain":        plain,
    "lowercase":    lowercase,
    "mixed_case":   mixed_case,
    "with_space":   with_space,
    "with_dash":    with_dash,
    "embedded":     embedded,
    "missing_zero": missing_zero,
    "misplaced_sep":misplaced_sep,
    "alt_label":    alt_label,
}

# ----------------------------
# 3. Real-world sentence templates using **all** IFSC contexts
#
# Context keywords:
#   "ifsc code", "bank branch code", "ifsc",
#   "bank", "indian financial system code",
#   "bank code", "india bank code", "branch code",
#   "neft code", "rtgs code", "imps code"
# ----------------------------
TEMPLATES = {
    "plain": [
        "The IFSC code for this bank branch is {v}",
        "Use {v} as the NEFT code when you transfer funds to this bank",
        "Enter this bank code {v} into the RTGS code field",
    ],
    "lowercase": [
        "Some systems list ifsc code in lowercase as {v}",
        "Your india bank code appears as {v}",
    ],
    "mixed_case": [
        "The Indian Financial System Code stored here is {v}",
        "Our records show the branch code as {v}",
    ],
    "with_space": [
        "Please enter the bank branch code with a space like {v}",
        "Your IMPS code is displayed as {v}",
    ],
    "with_dash": [
        "When formatting rtgs code you might see {v}",
        "The imps code for our bank appears as {v}",
    ],
    "embedded": [
        "IFSC is {v} and this is the official bank code you must verify",
        "We display your branch code as {v} for india bank code checks",
    ],
    "missing_zero": [
        "This entry {v} is invalid because it lacks the zero in IFSC",
        "Check your neft code it should not be {v}",
    ],
    "misplaced_sep": [
        "This rtgs code {v} has misplaced separators and will be rejected",
        "Your branch code format {v} is incorrect for IMPS transfers",
    ],
    "alt_label": [
        "ifsc code {v} is on file for your account",
        "bank code {v} verified by the system",
        "branch code {v} will be used for NEFT and RTGS",
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_ifsc_variations(count=50):
    records = []
    keys = list(VARIATIONS.keys())
    while len(records) < count:
        base    = gen_base_ifsc()
        key     = random.choice(keys)
        variant = VARIATIONS[key](base)
        text    = random.choice(TEMPLATES[key]).format(v=variant)
        records.append({
            "text":      text,
            "ifsc":      variant,
            "variation": key,
            "is_valid":  is_valid_ifsc(variant)
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_ifsc_variations(count=50)
    with open("ifsc_codes.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ ifsc_codes.json generated with all context keywords in real-world sentences")

