#!/usr/bin/env python3
import random
import json
import re

# ----------------------------
# 1. Gender options & validator
# ----------------------------
VALID_GENDERS = {"male", "female", "other"}
ABBREV_MAP   = {"male": "M", "female": "F", "other": "O"}

def gen_base_gender():
    """Randomly pick one of the canonical genders."""
    return random.choice(list(VALID_GENDERS)).capitalize()

def is_valid_gender(value):
    """Valid only if it exactly matches ‘Male’, ‘Female’, or ‘Other’."""
    return value.strip().lower() in VALID_GENDERS

# ----------------------------
# 2. Variation functions
# ----------------------------
def plain(g):        return g
def abbreviated(g):  return ABBREV_MAP[g.lower()]
def alt_phrasing(g):return f"Gender: {g}"
def with_prefix(g):  return "Mr." if g.lower()=="male" else "Ms."
def lowercase(g):    return g.lower()

VARIATIONS = {
    "plain":       plain,
    "abbreviated": abbreviated,
    "alt_phrasing":alt_phrasing,
    "with_prefix": with_prefix,
    "lowercase":   lowercase,
}

# ----------------------------
# 3. Sentence templates with full context coverage
# ----------------------------
TEMPLATES = {
    "plain": [
        "Your gender identity is recorded as {v} in the profile settings",
        "The sex category field shows {v} for your sexual identity",
        "The gender type for this user is {v} under gender expression",
    ],
    "abbreviated": [
        "System code for gender shows {v} for device registration",
        "The sex identity stored is abbreviated to {v}",
        "Your gender-specific code is {v} in the database",
    ],
    "alt_phrasing": [
        "Transgender users or cisgender users see entry Gender: {v}",
        "Non-binary or gender fluid options include {v} as a label",
        "Your documented gender preference is {v}",
    ],
    "with_prefix": [
        "The salutation prefix {v} implies your gender role",
        "Use prefix {v} when addressing this person in official forms",
        "Driver’s license shows prefix {v} for the gender category",
    ],
    "lowercase": [
        "The form field ‘sex’ shows {v} in lowercase",
        "Your gender fluid identity appears as {v}",
        "The profile’s gender expression is logged as {v}",
    ],
}

# ----------------------------
# 4. Bulk generator
# ----------------------------
def generate_gender_variations(count=50):
    records = []
    keys = list(VARIATIONS.keys())
    while len(records) < count:
        base    = gen_base_gender()
        key     = random.choice(keys)
        variant = VARIATIONS[key](base)
        text    = random.choice(TEMPLATES[key]).format(v=variant)
        records.append({
            "text":      text,
            "gender":    variant,
            "variation": key,
            "is_valid":  is_valid_gender(variant)
        })
    return records

# ----------------------------
# 5. Write JSON output
# ----------------------------
if __name__ == "__main__":
    out = generate_gender_variations(count=50)
    with open("genders.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("✅ genders.json generated with all context terms included.")
